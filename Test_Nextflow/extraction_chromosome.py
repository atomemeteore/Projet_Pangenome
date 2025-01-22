import argparse
import os
from Bio import SeqIO

def extraction_chromosome(input_path, output_dir):
    # Vérifiez si l'entrée est un répertoire ou un fichier
    if os.path.isdir(input_path):
        input_list = [os.path.join(input_path, f) for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))]
    elif os.path.isfile(input_path):
        input_list = [input_path]
    else:
        raise ValueError(f"L'entrée spécifiée ({input_path}) n'est ni un fichier valide ni un répertoire.")

    # Créez le répertoire de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)

    # Parcourir et traiter les fichiers
    for file in input_list:
        print(f"Processing file: {file}")
        
        # Parcourir les séquences dans le fichier FASTA
        for record in SeqIO.parse(file, "fasta"):
            output_file = os.path.join(output_dir, f"{record.id}.fasta")
            with open(output_file, "w") as f:
                SeqIO.write(record, f, "fasta")
            print(f"Saved: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extraction des chromosomes.")
    parser.add_argument('--input', required=True, help="Fichier ou répertoire d'entrée")
    parser.add_argument('--output', required=True, help="Répertoire de sortie")
    
    args = parser.parse_args()
    extraction_chromosome(args.input, args.output)
