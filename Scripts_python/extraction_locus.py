from Bio import SeqIO

# Dossier contenant les fichiers FASTA pour chaque chromosome
fasta_folder = "/home/nguyeho3/Documents/Projet_pangenome/chromosomes/chromosomes_2/"

# Liste des loci à extraire
# Format : {chromosome_filename: [(start1, end1), (start2, end2), ...]}
loci_to_extract = {
    "GWHEQVE00000002.fasta": [(500001, 700000)],
    "GWHEQVJ00000002.fasta": [(500001, 700000)],
    "GWHEQVM00000002.fasta": [(500001,700000)],
    "GWHEQVN00000002.fasta": [(500001,700000)],
    # Ajouter d'autres fichiers et coordonnées si nécessaire
}

# Fichier de sortie
output_file = "extracted_loci_3.fasta"

# Extraire les loci depuis les fichiers FASTA individuels
with open(output_file, "w") as out_file:
    for fasta_file, loci in loci_to_extract.items():
        fasta_path = fasta_folder + fasta_file
        
        try:
            # Charger la séquence du fichier FASTA
            record = next(SeqIO.parse(fasta_path, "fasta"))
            sequence = record.seq
        except FileNotFoundError:
            print(f"Avertissement : Fichier '{fasta_file}' introuvable.")
            continue
        except StopIteration:
            print(f"Avertissement : Fichier '{fasta_file}' est vide.")
            continue
        
        # Extraire les loci pour ce fichier
        for i, (start, end) in enumerate(loci, start=1):
            # Extraire le locus (attention à l'index 0 en Python)
            locus_seq = sequence[start-1:end]
            
            # Créer un header unique pour chaque locus
            header = f">{fasta_file}_locus_{start}_{end}_segment_{i}"
            
            # Sauvegarder dans le fichier FASTA
            out_file.write(f"{header}\n")
            out_file.write(str(locus_seq) + "\n")
            print(f"Locus extrait : {header}")

print(f"Extraction terminée. Résultats sauvegardés dans '{output_file}'.")
