# _**Projet d'analyse bioinformatique d'Alexis NGUYEN (M2 CCB4 - Université de Rouen Normandie)**_

Ce projet a pour but d'analyser les différences génétiques de plusieurs génomes de variétés de Brassica oleracea :

Les différents génomes sous format fasta étant trop lourds pour être uploadés sur le github, les liens d'accès sont donnés ci-dessous : 

## Lien google drive du dossier comprenant tous les génomes d'étude : 

https://drive.google.com/drive/folders/1o61SW1oh9svc7LyzNNhwCiAi5d91BiOa?usp=sharing

## Liens pour chaque génome individuel : 

* wild cabbage (W1701) : https://ngdc.cncb.ac.cn/gwh/Assembly/83522/show

* kohlrabi (PL021) : https://ngdc.cncb.ac.cn/gwh/Assembly/83524/show

* Broccoli (06-9-28) : https://ngdc.cncb.ac.cn/gwh/Assembly/83520/show

* kale (07-DH-33) : https://ngdc.cncb.ac.cn/gwh/Assembly/83523/show

* Brussels sprouts (D101) : https://ngdc.cncb.ac.cn/gwh/Assembly/83525/show

* Chinese kale (M249) : https://ngdc.cncb.ac.cn/gwh/Assembly/83516/show 

## Dossier Github Projet_Pangenome 

Le dossier Github Projet_Pangenome comprend :

* Un répertoire **data** comportant les séquences chromosomiques séparées, sous format fasta pour chaque génome (à titre d'information, à défaut d'avoir les séquences génomiques directement dans le github)

* Un répertoire **Scripts_python** comportant des fichiers python non-utilisés dans le projet.

* Un carnet Jupyter  **workflow.ipynb** expliquant le fonctionnement des scripts pytonh utilisés et du projet.

* Un répertoire **Test_Nextflow** reprenant certaines éléments du dossier parent Projet_Pangenome, mais en incluant des scripts Nextflow pour l'intégration des différentes étapes du projet dans un pipeline. (Les fichiers python sont modifiés pour la bonne intégration dans le pipeline)

Pour la bonne réalisation des scripts dans le dossier Projet_Pangenome et du pipeline dans le dossier Test_Nextflow, vérifier les chemins des inputs et des outputs et les modifier si besoin : Le chemin de l'input devrait pointer vers le dossier complet "genomes" comportant les différentes génomiques sous format fasta.
(Des modifications seront apportées pour permettre une utilisation plus générale des chemins).

## Resultats
Voici un résultat typique obtenu (Chromosome 5):
https://drive.google.com/file/d/1jwcx1gf7WMsbg5im4JxlzF2IoCR2bUi4/view?usp=sharing

## Pistes d'intérêts pour l'annotation de graphes 

GRannot : https://forge.ird.fr/diade/dynadiv/grannot


# _**Alexis NGUYEN bioinformatics analysis project (M2 CCB4 - Université de Rouen Normandie)**_

This project aims to analyse the genetic differences of several genomes of Brassica oleracea varieties:

The different genomes in fasta format are too heavy to be uploaded on github, access links are given below: 

## Google drive link of the folder including all study genomes: 

https://drive.google.com/drive/folders/1o61SW1oh9svc7LyzNNhwCiAi5d91BiOa?usp=sharing

## Links for each individual genome: 

* wild cabbage (W1701): https://ngdc.cncb.ac.cn/gwh/Assembly/83522/show

* kohlrabi (PL021): https://ngdc.cncb.ac.cn/gwh/Assembly/83524/show

* Broccoli (06-9-28): https://ngdc.cncb.ac.cn/gwh/Assembly/83520/show

* kale (07-DH-33): https://ngdc.cncb.ac.cn/gwh/Assembly/83523/show

* Brussels sprouts (D101): https://ngdc.cncb.ac.cn/gwh/Assembly/83525/show

* Chinese kale (M249): https://ngdc.cncb.ac.cn/gwh/Assembly/83516/show 

## Github Projet_Pangenome folder 

The Github Projet_Pangenome folder includes:

* A **data** directory with the separated chromosome sequences, in fasta format for each genome (for information, failing to have the genomic sequences directly in the github)

* A **Scripts_python** directory containing python files not used in the project.

* A Jupyter notebook  **workflow.ipynb** explaining the operation of the pytonh scripts used and the project.

* A **Test_Nextflow** directory containing some elements of the parent Projet_Pangenome folder, but including Nextflow scripts for integrating the different stages of the project into a pipeline. (Python files are modified for proper integration in the pipeline)

For the correct execution of the scripts in the Projet_Pangenome folder and the pipeline in the Test_Nextflow folder, check the input and output paths and modify them if necessary: The input path should point to the complete "genomes" folder containing the different genomes in fasta format.
(Changes will be made to allow more general use of paths).

## Results
The following is a typical result (Chromosome 5):
https://drive.google.com/file/d/1jwcx1gf7WMsbg5im4JxlzF2IoCR2bUi4/view?usp=sharing



