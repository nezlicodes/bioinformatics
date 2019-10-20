#Exemple of reading a fasta file:
import os;
def readFastaFile(fileName):
    fileObj = open(fileName,'rU')
    sequences = [];
    seq = '';
    if not os.path.exists(fileName):
        return -1;
    else:
        for line in fileObj:
            if line.startswith('>'):
                if seq:
                    sequences.append(seq)
                seq='';

            else:
                seq += line.rstrip();
        if seq:
            sequences.append(seq)
        fileObj.close()
        return sequences

print(readFastaFile('data/B4RAG3.fasta.txt'))