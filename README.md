**DNA Matching Project**

**Author:** Riya Pawar
This project provides a program to compare two DNA sequences and calculate the similarity between them. The user will input two DNA sequences, and the program will analyze the sequences, checking for equal length and valid nucleotide characters (A, T, C, G). It then calculates the percentage of similarity between the two sequences and outputs the result.

**Features**

**Length Check:** Ensures both DNA sequences have the same length before comparison.
**Nucleotide Validation:** Validates that each character in the sequences is a valid DNA nucleotide (A, T, C, G).
**Sequence Comparison:** Compares the two DNA sequences and counts the number of matching nucleotides.
**Similarity Calculation:** Calculates the similarity between the sequences as a percentage.

**How to Use**

Run the Program: Execute the program in a Python environment.
Input Sequences: You will be prompted to input two DNA sequences (strings containing only 'A', 'T', 'C', or 'G').
Result: The program will output the similarity percentage, indicating how similar the two DNA sequences are.

**Example**

Please enter **first** DNA sequence: ATCGATCG
Please enter **second** DNA sequence: ATCGATGG
Your similarity percentage **is** _87.5%_

**Functions**

_length_check(sequence1, sequence2)_

Checks whether the lengths of the two DNA sequences are equal.
This returns true if the sequences have different lengths, False otherwise.

_letter_check(s)_

Validates that all characters in the DNA sequence are valid nucleotides (A, T, C, or G).
Returns true if the sequence contains only valid characters, False otherwise.

_compare_sequences(s1, s2)_

Compares each nucleotide in the two sequences for similarity.
Returns the number of matching nucleotides.

_calculate_similarity(match_counter, total_length)_

Calculates the percentage of similarity based on the number of matching nucleotides.
Returns the similarity percentage as a floating-point number.

**Limitations**

The program assumes that the user inputs valid sequences in string format and doesn't handle more complex cases, such as sequences with ambiguous nucleotides (e.g., "N" for unknown base).
The program currently does not handle cases with spaces or other non-nucleotide characters in the input.

**Notes**

The program checks that both DNA sequences are the same length. If they are not, the user will be prompted to ensure the sequences are aligned properly.
The similarity percentage is calculated as the ratio of matching nucleotides to the total number of nucleotides.

-----------------------------------------------------------------------------------------------------------------

**Punnett Square Pairing Project**

**Author: Riya Pawar**

This project provides a program allowing the user to input two alleles (presumably from two parents). The program will then sort and pair each corresponding allele to display all possible genotypes that the two parents' offspring could inherit.

**Features**

Allele Validation: Ensures that each allele contains exactly two characters.
Input Alphabet Range: Validates that the allele consists of only alphabetic characters (A-Z, a-z).
Matching Allele Check: Verifies that both alleles have matching or compatible base characters.
Genotype Generation: Generates all possible genotypes that can result from pairing the two alleles.

**How to Use**

Run the Program: Execute the program in a Python environment.
Input Alleles: You will be prompted to input two alleles (one from each parent). Each allele must contain exactly two characters.
Result: The program will display all possible genotypes for the offspring by pairing the alleles in every combination.

Example
Enter alleles of the parent one (e.g., 'Rr'): Rr
Enter alleles of the parent two (e.g., 'Rr'): Rr
Possible offspring genotypes:
RR
Rr
rR
rr
In this example, the two parents both have the allele Rr, and the possible genotypes for their offspring are RR, Rr, rR, and rr.

Functions
_check_base_count(allele)_

Verifies that each allele contains exactly two characters.
Returns true if the allele has two characters, False otherwise.

_check_input_alphabet_range(allele)_

Ensures that the characters in the allele are alphabetic (A-Z or a-z).
Returns true if the allele contains only valid alphabetic characters, False otherwise.

_check_input_same_alphabet(allele)_

Confirms that the two characters in each allele are the same letter (case-insensitive).
Returns true if the allele contains two identical letters, False otherwise.

_check_allele1_allele2_same_alphabet(allele1, allele2)_

Checks that the first allele matches the second allele in terms of base characters (case-insensitive).
Returns true if the two alleles have matching characters, False otherwise.

_check_first_character(allele)_

Ensures that if the first character of the allele is lowercase, the second character is uppercase.
Returns true if the rule is followed, False otherwise.

_create_square(allele1, allele2)_

Generates and prints the Punnett Square by pairing each allele from the two parents and displaying the possible genotypes.
Returns none (it directly prints the genotypes to the console).


**Limitations**

The program expects exactly two alphabetic characters per allele.
It doesn't support more complex inheritance models (e.g., incomplete dominance or co-dominance).
The program assumes that input alleles are in a format like Rr (capital letter followed by lowercase) and doesn't handle other variations or ambiguous characters.

**Notes**
The program strictly checks for correct input formatting. If the input is invalid (e.g., incorrect number of characters, mixed case for matching letters), an error message will be displayed.
The program generates and displays all possible genotypes that result from the pairing of the input alleles, based on the standard Mendelian inheritance of alleles.
This tool can be used to simulate simple genetic crosses and understand the potential inheritance patterns in offspring.

