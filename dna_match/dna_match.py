
#Project by Riya Pawar. DNA Matching. c:
#Type in info here!

def length_check(sequence1, sequence2):
    if len(sequence1) != len(sequence2):
        return bool(True)
    else:
        return bool(False)
    
def letter_check(s):
    for k in range (0, len(s)):
        if (s[k].upper() == 'A' or s[k].upper() == 'T' or s[k].upper() == 'G' or s[k].upper() == 'C'):
            valid = bool(True)
        else:
            valid = bool(False)
    return valid

def compare_sequences(s1, s2):
    total_length = len(sequence1)
    match_counter = 0
    for x in range (0, total_length):
        if (s1[x] == s2[x]):
            match_counter += 1
    return match_counter

def calculate_similarity(match_counter, total_length):
    similarity = (match_counter / total_length)  * 100 
    return similarity

sequence1 = input("Please enter first DNA sequence.")
sequence2 = input("Please enter second DNA sequence.")

if length_check(sequence1, sequence2) == True:
    print ("Ensure that the sequence length is the same. ")
else:
    if letter_check (sequence1) and letter_check (sequence2) == True:
        match_counter = compare_sequences(sequence1, sequence2)
        simliarity_percent = calculate_similarity(match_counter, len(sequence1))
        print("Your simliarity percentage is " + str(simliarity_percent) + "%")
    else:
        print ("Ensure that each letter in the sequence is one of the four nucleotides: A, T, C, or G")