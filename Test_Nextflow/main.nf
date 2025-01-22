params.genomes_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/genomes'
params.concat_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow'
params.inputPGGB_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/concat'
params.outputPGGB_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/Results_PGGB'
params.index_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/Results_Index'

process extract_and_concatenate {
    input:
    path genomes_dir // Input directory with genome files

    output:
    path "concat" // Temporary output directory within the work directory

    publishDir "${params.concat_dir}", mode: 'copy' // Copy final outputs to the desired directory

    script:
    """
    mkdir -p concat
    python3 /home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/extract_and_concatenate.py --input ${genomes_dir} --output concat
    """
}

process PGGB {
    input:
    path fasta_file // Input individual FASTA file

    output:
    path "Results_PGGB/${fasta_file.baseName}" // Output directory for each FASTA file

    publishDir "${params.outputPGGB_dir}/${fasta_file.baseName}", mode: 'copy' // Copy each result to its specific directory

    script:
    """
    mkdir -p Results_PGGB/${fasta_file.baseName}
    pggb -i ${fasta_file} -n 6 -o Results_PGGB/${fasta_file.baseName} --multiqc
    """
}

process index_output {
    input:
    path fasta_file // Input individual FASTA file from PGGB output

    output:
    path "${fasta_file.baseName}.fai" // Output index file

    publishDir "${params.index_dir}", mode: 'copy' // Copy index files to the index directory

    script:
    """
    samtools faidx ${fasta_file}
    """
}

workflow {
    // Étape 1 : Extraction et concaténation
    extract_and_concatenate(params.genomes_dir)

    // Étape 2 : PGGB pour chaque fichier concaténé
    Channel
        .fromPath("${params.inputPGGB_dir}/*.fasta")
        | PGGB
        | index_output
}
