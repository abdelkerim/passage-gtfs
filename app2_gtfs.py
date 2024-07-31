import sys  
import pandas as pd  
from datetime import datetime 

# Analyse des fichiers CSV
ligne_df = pd.read_csv("/Users/abdelkerimharoun/Desktop/Civilia/gtfs/routes.txt")
trajet_df = pd.read_csv("/Users/abdelkerimharoun/Desktop/Civilia/gtfs/trips.txt")
horaires_arret_df = pd.read_csv("/Users/abdelkerimharoun/Desktop/Civilia/gtfs/stop_times.txt")


def les_prochains_departs(numero_arret, heure_actuelle):

    #l'heure actuelle en objet datetime.time pour comparaison
    heure_actuelle = datetime.strptime(heure_actuelle, '%H:%M:%S').time()
    
    # Les horaires de passage pour l'arrêt spécifié
    horaires_passage = horaires_arret_df[horaires_arret_df['stop_id'] == numero_arret].copy()
    
    # Horaires en objet datetime.time pour comparaison
    horaires_passage['departure_time'] = pd.to_datetime(horaires_passage['departure_time'], format='%H:%M:%S').dt.time
    

    prochains_départ = horaires_passage[horaires_passage['departure_time'] > heure_actuelle]
    

    # Fusion de donnees
    prochains_départ = prochains_départ.merge(trajet_df, on='trip_id').merge(ligne_df, on='route_id')
    
    # L'output
    return prochains_départ[['stop_id','route_id', 'departure_time', 'route_short_name', 'trip_id']]

def main():
    # Nombre d'arguments passés
    if len(sys.argv) < 2:
        print("Usage: python prochains_départ.py <numero_arret> [<heure_actuelle>]")
        sys.exit(1)
    
    numero_arret = int(sys.argv[1])
    
    # Verfication Argument passée
    if len(sys.argv) == 3:
        heure_actuelle = sys.argv[2]
    else:
        # Heure si non spécifiée
        heure_actuelle = datetime.now().strftime('%H:%M:%S')
    
    prochains_départ = les_prochains_departs(numero_arret, heure_actuelle)
    

    # Titre 
    print(f"Le prochain passage à cet numéro d'arrêt ({numero_arret}) après {heure_actuelle}:")

    # Afficher les prochains départs
    print(prochains_départ)

if __name__ == '__main__':
    main()
