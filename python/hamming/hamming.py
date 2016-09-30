# calculate the hamming distance of two strands of DNA
# the hamming distance is the number of differences in the two strands

def distance(seq1,seq2):
    #hamming distance is not defined for sequences of unequal length
    if len(seq1) != len(seq2):
        return None
    dist = 0
    for i in xrange(len(seq1)):
        if seq1[i] != seq2[i]:
            dist += 1
    return dist
