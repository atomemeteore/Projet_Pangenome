import re
gff_file = "/home/nguyeho3/Documents/Github_Pangenome/Projet_Pangenome/Test_Nextflow/gff_whole/GWHEQVE00000000.gff"

pattern = re.compile(r'ID=(C[0-9])')

with open(gff_file, 'r') as file:
    newfile = open("None.gff",'w')
    for line in file:
        if "OriSeqID=C" in line:
            file_name= re.search(r'ID=(C[0-9])', line).group(1)
            print(file_name)
            newfile = open(file_name + ".gff", 'a')
        newfile.write(line)
