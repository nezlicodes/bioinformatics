from Bio import Entrez, SeqIO
Entrez.email = 'benmeradi.lilyanezli@gmail.com'
handle = Entrez.esearch(db='nucleotide', term='CRT[Gene Name] AND "Plasmodium falciparum"[Organism]')
rec_list = Entrez.read(handle);
if rec_list['RetMax'] < rec_list['Count']:
    handle = Entrez.esearch(db='nucleotide', term='CRT[Gene Name] AND "Plasmodium falciparum"[Organism]', retmax=rec_list['Count'])
    rec_list = Entrez.read(handle)
id_list = rec_list['IdList']
hdl = Entrez.efetch(db='nucleotide', id=id_list, rettype='gb')
recs = list(SeqIO.parse(hdl, 'gb'))
for rec in recs:
    if rec.name == 'KM288867':
        break
print(rec)
print(rec.description)

for feature in rec.features:
    if feature.type == 'gene':
        print(feature.qualifiers['gene'])
    elif feature.type == 'exon':
        loc = feature.location
        print(loc.start, loc.end, loc.strand)
    else:
        print('not processed:\n%s' % feature)

