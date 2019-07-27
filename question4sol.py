user_input=input("Enter an alphabet: ")

if user_input.isalpha() and len(user_input)==1:
    vowels=['a','e','i','o','u']
    if  user_input.lower() in vowels:
        print("The alphabet is a vowel")
    else:
        print("The alphabet is a consonant")
else:
    print("Enter an alphabet only")