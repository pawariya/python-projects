
#Project by Riya Pawar. DNA Matching. c:
#This program will allow the user to type in two DNA sequences.
#From there, the program will calculate the simliarty between the two sequences.
#Then, it will output the similiarty sequence.

#makes sure that both the lengths of each sequence is the same
def length_check(sequence1, sequence2):
    if len(sequence1) != len(sequence2):
        return bool(True)
    else:
        return bool(False)
    
#makes sure that only the nucleotides A, T, G, or C are inputted 
def letter_check(s):
    for k in range (0, len(s)):
        if (s[k].upper() == 'A' or s[k].upper() == 'T' or s[k].upper() == 'G' or s[k].upper() == 'C'):
            valid = bool(True)
        else:
            valid = bool(False)
    return valid

#checks each nucleotide in the sequences for simliarity
def compare_sequences(s1, s2):
    total_length = len(sequence1)
    match_counter = 0
    for x in range (0, total_length):
        if (s1[x] == s2[x]):
            match_counter += 1
    return match_counter

#calculates the simliarty
def calculate_similarity(match_counter, total_length):
    similarity = (match_counter / total_length)  * 100 
    return similarity

#asks user to input two sequences
sequence1 = input("Please enter first DNA sequence.")
sequence2 = input("Please enter second DNA sequence.")

#checking all previously defined variables
if length_check(sequence1, sequence2) == True:
    print ("Ensure that the sequence length is the same. ")
else:
    if letter_check (sequence1) and letter_check (sequence2) == True:
        match_counter = compare_sequences(sequence1, sequence2)
        simliarity_percent = calculate_similarity(match_counter, len(sequence1))
        print("Your simliarity percentage is " + str(simliarity_percent) + "%")
    else:
        print ("Ensure that each letter in the sequence is one of the four nucleotides: A, T, C, or G")