from Bio import Entrez, SeqIO
Entrez.email = 'benmeradi.lilyanezli@gmail.com'
handle = Entrez.esearch(db='nucleotide',term='CRT[Gene Name] AND "Plasmodium falciparum"[Organism]')
rec_list = Entrez.read(handle)
if rec_list['RetMax'] < rec_list['Count']:
    handle = Entrez.esearch(db='nucleotide', term='CRT[Gene Name] AND "Plasmodium falciparum"[Organism]', retmax=rec_list['Count'])
    rec_list = Entrez.read(handle)
