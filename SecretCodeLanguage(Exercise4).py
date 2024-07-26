# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

def code(word):
    a=len(word)
    b=word
    if a>=3:
        z=b[1:]
        y="asj"+z+word[0]+"kjl"
        print("Coded word: ",y)
    else:
        q=word[::-1]
        print("Coded word: ",q)

def decode(word):
    a=len(word)
    if a<3:
        print("Decoded word: ",word[::-1])
    else:
        b=word[3:-3]
        c=b[-1]
        z=c+b[:-1]
        print("Decoded word: ",z)
        
print('''
      Enter 1 to Code a word.
      Enter 2 to Decode a word.
      Enter 3 to quit the program.
      ''')
while True:
    ask=int(input("Enter a number: "))
    if ask==1:
        st=input("Enter a string to code: ")
        z=st.split(" ")
        for i in z:
            code(i)
    elif ask==2:
        st=input("Enter the coded the string to decode it: ")
        z=st.split()
        for i in z:
            decode(i)
    elif ask==3:
        break
    else:
        print("Please give a valid input.")
        continue
    