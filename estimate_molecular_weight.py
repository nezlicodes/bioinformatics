def mol_mass(seq, type):
    weights = {
        "DNA": {"A":313.2, "T": 304.2, "C": 289.2, "G":345.2},
        "RNA":  {"A": 329.2, "U":306.2, "C": 305.2, "G":345.2},
        "protein":{"Ala":89, "Arg":174, "Asn": 132,"Asp":133,
                   "Cys":123, "Glu":147, "Gln":146,"Gly":75,
                   "His":155,"Ile": 131, "Leu":131, "Lys":146,
                   "Met":149, "Phe":165, "Pro":115, "Ser": 105,
                   "Thr":119, "Trp":204, "Tyr":181, "Val": 117}
    };
    if type == 'DNA':
        count = 79;
        for i in seq:
            count += weights['DNA'][i];
    elif type == "RNA":
        count = 159;
        for i in seq:
            count += weights['RNA'][i];
    else:
        count = 18.02;
        for i in seq:
            count += weights['protein'][i]

    return '{}Da'.format(count);

print( mol_mass("ATCG", type='DNA'));
