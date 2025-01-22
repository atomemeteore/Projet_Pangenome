from pathlib import Path
from collections import defaultdict

# Répertoire contenant les fichiers .fasta
chemin = Path("Projet_Pangenome/Chromosomes")

# Dictionnaire pour regrouper les fichiers par leur suffixe
groupes_fichiers = defaultdict(list)

# Dictionnaires pour les groupes de contenu
groupes_contenu = {
    "C1": [],
    "C2": [],
    "C3": [],
    "C4": [],
    "C5": [],
    "C6": [],
    "C7": [],
    "C8": [],
    "C9": [],
    "00000010": []
}

# Parcourir les fichiers dans le répertoire
for element in chemin.glob("*.fasta"):
    with open(element, 'r') as chromosome:
        contenu = chromosome.read()
        for key in groupes_contenu.keys():
            if key in contenu:
                groupes_contenu[key].append(contenu)

# Créer le répertoire de sortie s'il n'existe pas
dossier = Path("Projet_Pangenome/Concat")
if not dossier.exists():
    dossier.mkdir(parents=True)

# Écrire les fichiers concaténés
for key, sequences in groupes_contenu.items():
    if sequences:  # Vérifier qu'il y a des séquences à écrire
        output_file = dossier / f"Concat_{key}.fasta"
        with open(output_file, "w") as concat:
            concat.write("\n".join(sequences))

print("Concaténation terminée.")