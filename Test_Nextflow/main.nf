params.genomes_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/genomes'  
params.concat_dir = '/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/concat'


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


workflow {
    genomes_files = Channel.fromPath("${params.genomes_dir}/*.fasta")
    concat_files = extract_and_concatenate(genomes_files)

    // Move files to the final output directory
    concat_files.view()
    concat_files.map { file -> 
        file.moveTo("${params.concat_dir}/${file.name}")
    }
}
