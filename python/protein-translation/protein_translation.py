codon_proteins = {
    'AUG':'Methionine', 
    'UUU': 'Phenylalanine', 
    'UUC': 'Phenylalanine', 
    'UUA': 'Leucine', 
    'UUG': 'Leucine', 
    'UCU': 'Serine', 
    'UCC': 'Serine', 
    'UCA': 'Serine', 
    'UCG': 'Serine', 
    'UAU': 'Tyrosine', 
    'UAC':'Tyrosine', 
    'UGU': 'Cysteine', 
    'UGC': 'Cysteine', 
    'UGG': 'Tryptophan', 
    'UAA': 'STOP', 
    'UAG': 'STOP', 
    'UGA': 'STOP'
}
def proteins(strand):
    if not isinstance(strand, str):
        raise ValueError('value not a string')
    
    result = []
    n = 3 
    codons = [strand[i:i+n] for i in range(0, len(strand), n)]
    for codon in codons:
        proteins = codon_proteins[codon]
        if proteins != 'STOP':
            result.append(proteins) 
        else : 
            break

    return result
