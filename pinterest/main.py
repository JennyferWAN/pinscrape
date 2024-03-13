import os
import datetime
from pinscrape import pinscrape

# Obtenir la date actuelle
current_date = datetime.datetime.now().strftime("%d%m%y")  # Format: JJMMAA

# Créer le nom du dossier principal avec la date actuelle
main_folder = current_date

# Créer les dossiers correspondant à chaque catégorie existante sur votre compte Pinterest
categories_from_pinterest = ["fashion week 2024", "old money aesthetic", "study"]
output_folders = [os.path.join(main_folder, category.replace(" ", "_")) for category in categories_from_pinterest]

# Assurez-vous que les dossiers de sortie existent, sinon créez-les
for folder in output_folders:
    os.makedirs(folder, exist_ok=True)

# Configuration de pinscrape
limit = 10

# Parcourir les catégories et télécharger les épingles correspondantes
for category, folder in zip(categories_from_pinterest, output_folders):
    details = pinscrape.scraper.scrape(category, folder, {}, limit, 30)
    if details["isDownloaded"]:
        print(f"Images téléchargées pour la catégorie '{category}' dans le dossier '{folder}'")
    else:
        print(f"Aucune image trouvée pour la catégorie '{category}'")

print("Téléchargement terminé!")
