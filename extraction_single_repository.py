
from Bio import SeqIO
import os
import re

repertoire = "Projet_Pangenome/genomes"
input_list = []

for nom_fichier in os.listdir(repertoire):
    chemin_complet = os.path.join(repertoire, nom_fichier)
    input_list.append(chemin_complet)

pattern = re.compile(r"(.+)\/genomes\/(.+)\.genome\.fasta")

def extraction_chromosome():
    output_folder = f"Projet_Pangenome/Chromosomes"
    os.makedirs(output_folder, exist_ok=True)
    for file in input_list:
        print(file)
        # Dossier de sortie
        match = pattern.match(file)
        if match:
            print(match.group(2))                 
            # Lecture et extraction des séquences
            for record in SeqIO.parse(file, "fasta"):
                    # Construire un fichier de sortie basé sur l'identifiant
                    output_file = os.path.join(output_folder,f"{record.id}.fasta")
                    with open(output_file, "w") as f:
                        SeqIO.write(record, f, "fasta")
                    print(f"Séquence {record.id} sauvegardée dans {output_file}")
    print("Extraction terminée.")

def main():
    extraction_chromosome()

if __name__ == '__main__':
    main()