#Mixed cypher project 

import sys
import string

if __name__=="__main__":
    f=file(sys.argv[1])
    content=f.read()#File content
    alphabet="abcdefghijklmnopqrstuvwxyz"
    keyword=raw_input("Please enter the keyword for the mixed cypher: ")
    print 'Plaintext: '
    print alphabet
    alphabet=keyword.lower()+alphabet #append lowercase keyword at beginning of alphabet

    i=0
    mixed_cypher=""
    #Check each letter at a tiem for duplicates, starting with keyword in alphabet
    while i<len(alphabet):
        if mixed_cypher.find(alphabet[i]==-1): #if letter not found
            mixed_cypher=mixed_cypher+alphabet[i]
        i=i+1

    print "Ciphertext: ", mixed_cypher, "\n"

    i=0
    encryption=""
    alphabet="abcdefghijklmnopqrstuvwxyz"
    while i<len(content):
        if(content[i].isalpha() and content[i].isupper()):
            pos=alphabet.index(content[i].lower())
            encryption=encryption+mixed_cypher[pos].upper()
        elif(content[i].isalpha() and content[i].lower()):
            pos=alphabet.index(content[i])
            encryption=encryption+mixed_cypher[pos]

        else:
            encryption=encryption+content[i]
        i=i+1
    print encryption
