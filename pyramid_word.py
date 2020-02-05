string = input("Enter any string:") #give any string
freq = dict((letter,string.count(letter)) for letter in set(string)) # letter frequencies
l = list(freq.values()) #list of values
l.sort() #sorted list of values
l1=[] #empty list for sequence of numbers with length of the given string
for i in range(len(string)):
    l1.append(i+1)
def sequence_match(list1,list2):#matching the sequences of two lists
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True
sequence_match(l,l1)


