#!/usr/bin/env nextflow

nextflow.enable.dsl=2

params.input_dir = '/chemin/vers/les/genomes'  // Chemin vers les fichiers d'entrée
params.output_dir = '/home/nguyeho3/Documents/Test_Nextflow/Chromosomes'  // Répertoire de sortie

process say_hello {
    output:
    path "hello.txt"

    publishDir "${params.output_dir}", mode: 'copy'

    script:
    """
    echo "Hello, Nextflow!" > hello.txt
    """
}

workflow {
    say_hello()
}
