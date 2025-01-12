
from Bio import SeqIO
import os

# Nom du fichier FASTA source
input_file = "/home/nguyeho3/Documents/(06-9-28)-GWHEQVJ00000000.genome.fasta"

# Liste des identifiants des chromosomes à extraire
chromosome_ids = [
    "GWHEQVJ00000001",
    "GWHEQVJ00000002",
    "GWHEQVJ00000003",
    "GWHEQVJ00000004",
    "GWHEQVJ00000005",
    "GWHEQVJ00000006",
    "GWHEQVJ00000007",
    "GWHEQVJ00000008",
    "GWHEQVJ00000009",
    "GWHEQVJ00000010",
    
    # Ajoutez les autres identifiants ici
]

# Dossier de sortie
output_folder = "/home/nguyeho3/Documents/chromosomes_(06-9-28)"
os.makedirs(output_folder, exist_ok=True)

# Lecture et extraction des séquences correspondant aux identifiants
for record in SeqIO.parse(input_file, "fasta"):
    if record.id in chromosome_ids:
        # Construire un fichier de sortie basé sur l'identifiant
        output_file = os.path.join(output_folder, f"{record.id}.fasta")
        with open(output_file, "w") as f:
            SeqIO.write(record, f, "fasta")
        print(f"Séquence {record.id} sauvegardée dans {output_file}")
    else:
        print(f"Séquence {record.id} ignorée (non dans la liste des identifiants).")

print("Extraction terminée.")

