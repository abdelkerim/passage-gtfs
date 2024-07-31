PROCHAIN PASSAGE - GTFS : Exercise 2

Description

Une application qui prend comme intrant un numéro d'arrêt et une date/heure puis retourne pour chaque ligne le prochain passage à cet arrêt. Si la date/heure n'est pas spécifiée, on prend l'heure système actuelle. Cette application est en ligne de commande.


Guide d'Installation

Les Prérequis sont:
- Python3
- pip
- Pandas

A. Les étapes pour installer  sur Ubuntu:

1. Installez les dépendances via un terminal en executant les lignes de commande suivantes:

    ```sh
    sudo apt update
    sudo apt install python3
    sudo apt install python3-pip
    pip3 install pandas
    ```
    
2. Clonez le dépôt GitHub via un terminal  utilisez la syntaxe suivante:

    ```sh
    git clone https://github.com/abdelkerim/passage-gtfs.git


3. Naviguer vers le dossier cloné passage-gtfs  et Vvérifiez que les fichiers GTFS sont présents dans le dossier `gtfs`

   ```sh
    cd passage-gtfs
    ```


B. Exécution avec la ligne de commande

Pour exécuter l'application depuis la ligne de commande, utilisez la syntaxe suivante :

```sh
python3 app2_gtfs.py <numero d'arret> <l'heure>

<numero d'arret> example 10000
<l'heure> en format HH:MM:SS example 10:02:10
