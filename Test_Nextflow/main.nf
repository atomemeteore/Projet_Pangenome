params.genomes_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/genomes'
params.concat_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow'
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

process index_fasta {
    input:
    path fasta_file // Input individual FASTA file

    output:
    tuple path(fasta_file), path("${fasta_file}.fai") // Output FASTA file and its index

    publishDir "${params.index_dir}", mode: 'copy' // Copy index files to the index directory

    maxForks 1
    script:
    """
    samtools faidx ${fasta_file}
    """
}

process PGGB {
    input:
    tuple path(fasta_file), path(index_file) // Input FASTA file and its index

    output:
    path "${fasta_file.baseName}" // Output directory for PGGB results

    publishDir "${params.outputPGGB_dir}/${fasta_file.baseName}", mode: 'copy' // Copy each result to its specific directory

    maxForks 1 // Limiter à un seul processus PGGB en cours à la fois

    script:
    """
    mkdir -p ${fasta_file.baseName}
    pggb -i ${fasta_file} -n 6 -o ${fasta_file.baseName} --multiqc
    """
}

workflow {
    // Étape 1 : Extraction et concaténation
    extract_and_concatenate(params.genomes_dir)

    // Étape 2 : Récupération des fichiers générés dans le répertoire `concat`
    Channel
        .fromPath("${params.concat_dir}/concat/*.fasta")
        .view { "Fichier détecté pour indexation : ${it}" }
        .set {fasta_files}

    fasta_files | index_fasta

    index_fasta.out.view {"indexé : ${it}"}

    // Étape 3 : Exécution de PGGB pour chaque fichier indexé
    index_fasta.out | PGGB
}
