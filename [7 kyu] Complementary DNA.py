def DNA_strand(dna):
    return "".join({"C" : "G", "G" : "C",
                    "T" : "A", "A" : "T"}[nucleotide] for nucleotide in dna)
