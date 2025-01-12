import csv

def map_gff_to_graph(gff_file, paf_file, output_file):
    # Charger les alignements PAF
    node_map = {}
    with open(paf_file, 'r') as paf:
        for line in paf:
            cols = line.strip().split('\t')
            node, ref_start, ref_end, node_start, node_end = cols[0], int(cols[7]), int(cols[8]), int(cols[2]), int(cols[3])
            node_map[(ref_start, ref_end)] = node

    # Mapper les annotations GFF sur les nœuds
    with open(gff_file, 'r') as gff, open(output_file, 'w') as out:
        writer = csv.writer(out, delimiter='\t')
        writer.writerow(['NodeID', 'Feature', 'Start', 'End', 'Attributes'])
        for line in gff:
            if line.startswith("#"):
                continue
            cols = line.strip().split('\t')
            ref_start, ref_end, feature, attributes = int(cols[3]), int(cols[4]), cols[2], cols[8]
            for (start, end), node in node_map.items():
                if start <= ref_start and end >= ref_end:
                    writer.writerow([node, feature, ref_start, ref_end, attributes])

# Exécuter le mapping
gff_file = "/home/nguyeho3/Documents/Projet_pangenome/Test_Annotation/GWHEQVJ00000002.gff"
paf_file = "/home/nguyeho3/Documents/Projet_pangenome/Test_Annotation/concatChrom1.fa.21d1a48.alignments.wfmash.paf"
map_gff_to_graph(gff_file, paf_file, 'graph_annotations.tsv')
