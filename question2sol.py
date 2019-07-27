user_input=input("Enter a string : ")
letter=0
digit=0
for str in user_input:
    if str.isalpha():
        letter=letter+1
    elif str.isdigit():
        digit=digit+1
print("Letter :",letter)
print("Digit :",digit)