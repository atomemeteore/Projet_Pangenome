params.genomes_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/genomes'
params.concat_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow'

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

workflow {
    extract_and_concatenate(params.genomes_dir)
}
