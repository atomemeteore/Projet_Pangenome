#!/usr/bin/env nextflow

nextflow.enable.dsl=2

// Définition des paramètres
params.input_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/genomes' // Chemin vers les fichiers d'entrée
params.output_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow' // Dossier pour les résultats

// Processus pour extraire les chromosomes
process extract_chromosomes {
    tag "${file.name}"

    input:
    path file

    output:
    path "Chromosomes/*"

    publishDir "${params.output_dir}", mode: 'copy'

    script:
    """
    echo "Processing file: ${file}" >> debug.log
    mkdir -p Chromosomes
    python3 /home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/extraction_chromosome.py --input ${file} --output Chromosomes >> debug.log 2>&1
    ls -l Chromosomes >> debug.log
    """
}



// Workflow principal
workflow {
    // Crée un canal à partir des fichiers du répertoire d'entrée
    files_ch = Channel.fromPath("${params.input_dir}/*")

    // Vérifiez si le canal contient des fichiers
    files_ch.view() // Affiche les fichiers du canal dans la sortie

    // Connecter le canal de fichiers au processus
    extracted_chromosomes = extract_chromosomes(files_ch)
}
