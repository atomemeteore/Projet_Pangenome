params.genomes_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/genomes'
params.concat_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow'
params.inputPGGB_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/concat'
params.outputPGGB_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow'

process extract_and_concatenate {

    input:
    path genome_file

    output:
    path "${genome_file.baseName}_concatenated.fasta"

    script:
    """
    python3 $projectDir/extract_and_concatenate.py --input ${genome_file.parent} --output ${genome_file.baseName}_concatenated.fasta
    """
}

process PGGB {
    input:
    path fasta_file // Input directory concatenated chromosomes in fasta format

    output:
    path "Results_PGGB/${fasta_file.baseName}" // Outputdirectory for each fasta file

    publishDir "${params.outputPGGB_dir}/${fasta_file.baseName}", mode: 'copy' // Copy each output to its specific directory

    script:
    """
    mkdir -p Results_PGGB/${fasta_file.baseName}
    samtools faidx ${fasta_file}
    nohup pggb -i ${fasta_file} -n 6 -o Results_PGGB/${fasta_file.baseName} --multiqc
    """
}




workflow {
    extract_and_concatenate(params.genomes_dir)

        // Étape 2 : PGGB pour chaque fichier concaténé
    Channel
        .fromPath("${params.inputPGGB_dir}/*.fasta")
        | PGGB
}
