'''
## NAME:
  rna2prot.py
  
## LANGUAGE & VERSION:
  python 3.8.5
  
## AUTHOR:
  Phabel Antonio Lopez Delgado <phabel2001@gmail.com>
  
## DATE:
  June 16th, 2021.
  
## DESCRIPTION & LOGIC:
  This script takes an RNA string, converts it to DNA and
  provides its aminoacid sequence.
  
## USAGE:
  rna2prot.py python 3.8.5
  
## ARGUMENTS:
  No arguments needed

## INPUT - OUTPUT:
     Input: RNA sequence
     Output: Aminoacid sequence
    
## EXAMPLES
    Input:
    RNA sequence: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

    Output:
    MAMAPRTEINSTRING

## SOFTWARE REQUIREMENTS:
    python3
    
## FUNCTIONS:
  No functions were created.
  Methods: input(), range(), split(), print()

## EXTRA COMMENTS:
    This is a solution to Rosalind: Translating RNA into Protein.
    
## LAST MODIFICATION:
  Phabel Antonio Lopez Delgado : June 16th, 2021. [Creation]

## GITHUB
  [Insert GitHub link]
  
'''

############
# Main Code
############

## Genetic code
gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 
    'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N', 
    'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 
    'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H', 
    'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 
    'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V', 
    'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 
    'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S', 
    'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 
    'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

## Get DNA string and start codon list
rna_seq = input('RNA sequence: ')
dna_seq = rna_seq.replace('U', 'T')
codons = []

## Add every codon to a list
for codon in range(0, len(dna_seq), 3):
    codons.append(dna_seq[codon : codon+3])
    
## Created protein list of aminoacids
protein = []
for codon in codons:
    protein.append(gencode[codon])
    
## Remove STOP codon and print aminoacid sequence
del protein[-1]
print(*protein, sep = '')
