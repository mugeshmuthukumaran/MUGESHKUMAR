a=['a','e','i','o','u']
b=raw_input()
if b in a:
    print ("Vowel")
elif(b.isalpha()):
    print("Consonant")
else:
        print("Invalid")
