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
