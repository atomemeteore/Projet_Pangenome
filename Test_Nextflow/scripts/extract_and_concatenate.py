from Bio import SeqIO
import argparse
import re
from pathlib import Path
from collections import defaultdict

def extraction_chromosome(input_dir, output_dir):
    pattern = re.compile(r"(.+)\.genome\.fasta")
    chromosomes = defaultdict(list)

    # Parcourir tous les fichiers d'entrée
    for file in Path(input_dir).glob("*.genome.fasta"):
        for record in SeqIO.parse(file, "fasta"):
            search = re.search(r"Chromosome (C\d+)", record.description)
            if search:
                chromosomes[search.group(1)].append(record)

    # Créer le répertoire de sortie s'il n'existe pas
    output_dir.mkdir(parents=True, exist_ok=True)

    # Générer les fichiers concaténés
    for group, chr_list in chromosomes.items():
        output_file = output_dir / f"Concat_{group}.fasta"
        with open(output_file, "w") as concat:
            for chr in chr_list:
                print(chr)
                concat.write(f">{chr.id}\n{chr.seq}\n")

    print("Fichiers FASTA générés.")

def main():
    # Configuration des arguments du script
    parser = argparse.ArgumentParser(description="Extraction et concaténation de chromosomes.")
    parser.add_argument("--input", required=True, help="/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/genomes")
    parser.add_argument("--output", required=True, help="/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/Concat2")
    args = parser.parse_args()

    # Appeler la fonction principale avec les arguments
    extraction_chromosome(Path(args.input), Path(args.output))

if __name__ == '__main__':
    main()
