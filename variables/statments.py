
#Project by Riya Pawar. Punnet square pairing. c:

#ensuring that there are 2 bases per allele
def check_base_count (allele):
    if len(allele) != 2:
        return bool(False)
    else:
        return bool(True)

#ensuring bases are A-Z & a-z
def check_input_alphabet_range (allele):
    if ((allele[0] >= "A" and allele[0] <= "Z") or (allele[0] >= "a" and allele[0] <= "z")) and ((allele[1] >= "A" and allele[1] <= "Z") or (allele[1] >= "a" and allele[1] <= "z")) :
        return bool(True)
    else:
        return bool(False)
    
#ensuring bases in each allele match (character)  
def check_input_same_alphabet (allele):
     if allele[0].upper() == allele[1].upper() :
          return bool(True)
     else:
        return bool(False)

#ensuring allele1 and allele2 bases match (character)
def check_allele1_allele2_same_alphabet(allele1, allele2):
    if allele1.upper() == allele2.upper() :
        return bool(True)
    else:
        return bool(False)
    
#ensuring that if the first base is a lowercase base that the second base if NOT lowercase
def check_first_character(allele):
    if (allele[0] >= "a" and allele[0] <= "z") and (allele[1] >= "A" and allele[1] <= "Z"):
        return bool(False)
    else:
        return bool(True)
    
#actual process of matching
def create_square (allele1, allele2) :
    for b1 in allele1:
        for b2 in allele2:
            if (b1 >= "a" and b1 <= "z") and (b2 >= "A" and b2 <= "Z:"):
                genotype = b2 + b1
            else:
                genotype = b1 + b2
            print (genotype)

#asks user for alleles
allele1 = input("Enter alleles of the parent one (e.g., 'Rr'): ")
allele2 = input("Enter alleles of the parent two (e.g., 'Rr'): ")

#checking for valid character input
if check_base_count (allele1) and check_base_count (allele2):
    if check_input_alphabet_range (allele1) and check_input_alphabet_range (allele2):
        if check_input_same_alphabet (allele1) and check_input_same_alphabet (allele2):
            if check_allele1_allele2_same_alphabet (allele1, allele2):
                if check_first_character (allele1) and check_first_character (allele2):
                    create_square(allele1, allele2)
                else:
                    print("Bad input. If first base is lowercase, second base MUST be lowercase.")
            else:
                print("Bad input. Make sure both bases for the alleles are the same letters.")
        else:
            print ("Bad input. Make sure the alleles are the same letters.") 
    else:
        print ("Bad input. Make sure the alleles are A-Z.")
else:
    print("Bad Input. Ensure that there is only two bases per allele.")