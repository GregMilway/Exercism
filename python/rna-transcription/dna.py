#transcribe a DNA sequence to an RNA sequence
# 'C' -> 'G'
# 'G' -> 'C'
# 'T' -> 'A'
# 'A' -> 'U'

rna_dict = { 'C':'G','G':'C','T':'A','A':'U'}

def to_rna(seq):
    return ''.join([rna_dict[char] for char in seq])
