import os

def split_gff_by_chromosome(input_gff, output_dir):
    """
    Sépare les annotations d'un fichier GFF en fichiers distincts par chromosome.
    
    Args:
        input_gff (str): Chemin vers le fichier GFF d'entrée.
        output_dir (str): Répertoire où les fichiers GFF séparés seront stockés.
    """
    # Vérifier si le répertoire de sortie existe, sinon le créer
    os.makedirs(output_dir, exist_ok=True)
    
    # Dictionnaire pour stocker les lignes par chromosome
    chromosomes = {}
    
    # Lire le fichier GFF
    with open(input_gff, 'r') as gff:
        for line in gff:
            # Conserver les lignes de commentaires et d'en-têtes pour chaque fichier
            if line.startswith("#"):
                header = line
                continue
            
            # Extraire le chromosome depuis la première colonne
            parts = line.strip().split("\t")
            if len(parts) < 9:
                continue  # Ignorer les lignes mal formées
            chromosome = parts[0]
            
            # Ajouter la ligne au dictionnaire correspondant
            if chromosome not in chromosomes:
                chromosomes[chromosome] = [header]
            chromosomes[chromosome].append(line)
    
    # Écrire chaque chromosome dans un fichier séparé
    for chromosome, lines in chromosomes.items():
        output_file = os.path.join(output_dir, f"{chromosome}.gff")
        with open(output_file, 'w') as out_gff:
            out_gff.writelines(lines)
    
    print(f"Les fichiers GFF ont été générés dans le répertoire : {output_dir}")

# Exemple d'utilisation
input_gff = "/home/nguyeho3/Documents/Projet_pangenome/GFF/GWHEQVJ00000000.gff"  # Remplacez par le chemin de votre fichier GFF
output_dir = "/home/nguyeho3/Documents/Projet_pangenome/GFF/GFF_chromosomes"  # Répertoire où les fichiers GFF seront stockés
split_gff_by_chromosome(input_gff, output_dir)
