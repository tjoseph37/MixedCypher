# MixedCypher

The following python file takes in a file name at the command line and prompts the user to enter a keyword. This keyword 
is then used to create a mixed alphabet by removing any duplicates in the keyword and placing the keyword at the beginning of the alphabet
then removing any duplicates in the mixed alphabet. For instance, let the user enter the keyword COMPUTER. This would produce:
        Plaintext: ABCDEFGHIJKLMNOPQRSTUVWXYZ
        Ciphertext: COMPUTERABDFGHIJKLNQSVWXYZ 
        
This mixed alphabet is then used to encode the file contents. The command to run the file is as follows:
        python mixed_cypher.py filename
