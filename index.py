#Find similarities between two sequences of same length
def score_match(query, subject, match, mismatch):
    score = 0;
    for i in range(0, len(subject)):
        if subject[i] == query[i]:
            score += match;
        else:
            score += mismatch;

    return score;

subject = 'actgatcGATTGATCgatc'
query   =    'tttaGATCGATCtttgatc'

print(score_match(query, subject, 1, -1));