data = open("data.txt", "r")
dna_seq = data.readlines()[1]
def composition_n(str, n):
    limit = n-1
    composition_n = []
    if(n > len(str)):
        return 'k_mer have to be smaller than length of string'
    for i in range(len(str)-limit):
        composition_n.append(str[i:i+n])
    return composition_n;
print(composition_n(dna_seq, 100))
