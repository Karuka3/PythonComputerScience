from enum import IntEnum
from typing import Tuple, List


Nucleotide = IntEnum("Nucleotide", ("A", "C", "G", "T"))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]


def string_to_gene(s: str) -> Gene:
    gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene


def linear_contains(gene: Gene, key_codon: Codon) -> bool:  # 線形探索 計算量O(n)
    for codon in gene:
        if codon == key_codon:
            return True
    return False


def binary_contains(gene: Gene, key_codon: Codon) -> bool:  # 二分探索 計算量O(log(n))
    low = 0
    high = len(gene) - 1
    while low <= high:
        mid = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False


if __name__ == "__main__":
    gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
    my_gene = string_to_gene(gene_str)
    my_sorted_gene = sorted(my_gene)

    acg = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
    gat = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

    print(linear_contains(my_gene, acg))
    print(linear_contains(my_gene, gat))

    print(binary_contains(my_sorted_gene, acg))
    print(binary_contains(my_sorted_gene, gat))
