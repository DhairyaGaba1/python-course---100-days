# Exercise 3 - Create a program capable of displaying questions to the user like KBC
# Use list data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing.
def lifeline(l_lines):
    print(l_lines)
    a=input("Which lifeline do you want to use(please enter the proper name): ")
    if a.capitalize()=="Expert advice":
        num=q_bank.index(i)
        ans=a_key[num]
        print("According to the expert the answer to your question should be: ",ans)
        l_lines.remove(a.capitalize())
    elif a.capitalize()=="Switch question":
        print("From which category would you like to replace your question with?(Gaming/Religion/History/Sports)?")
        b=input("Enter a choice(please enter the proper name of the category): ")
        if b.lower()=="gaming":
            ques=input("Who has created the game God Of War:Ragnarok?")
            ans=input("Enter your answer:")
            if ans.lower() in "santa monica studios":
                print("You got the right answer")
            else:
                print("Sorry but your answer wasn't correct.")
        elif b.lower()=="religion":
            ques=input("Which religious figure’s statue was the tallest in the world until it was over taken by the Statue of Unity?")
            ans=input("Enter your answer:")
            if ans.lower() in "lord buddha":
                print("You got the right answer")
            else:
                print("Sorry but your answer wasn't correct.")
        elif b.lower()=="history":
            ques=input("Who killed Mohandas Karamchand Gandhi?")
            ans=input("Enter your answer:")
            if ans.lower() in "nathuram godse":
                print("You got the right answer")
            else:
                print("Sorry but your answer wasn't correct.")
        elif b.lower()=="sports":
            ques=input("Who has scored most runs in finals for india in ICC events?")
            ans=input("Enter your answer:")
            if ans.lower() in "virat kohli":
                print("You got the right answer")
            else:
                print("Sorry but your answer wasn't correct.")
    else:
        print("Please enter a valid lifeline name.")
        # ask_type=input("Which type of question do you want")
print("Hello, we are gonna play KBC")
print("You are going to have 2 lifelines which are: \n")
print('''
        1. Expert advice - You will be told the answer of the questions and it will directly move to the next question.
        2. Switch question - Your current question will be replaced with another question of your preference but no options will be given.
      ''')
l_lines=["Expert advice","Switch question"]
q_bank=["Current Railway Minister of India is","Which god is also known as ‘Gauri Nandan’?","What does not grow on tree according to a popular Hindi saying?","Which city is known as Pink City in India?","Who wrote India's National Anthem?","How many major religions are there in India?","When is the National Hindi Diwas celebrated?","How many states are there in India?","Where in India Gate located?","Who wrote Vande Mataram?"]
a_key=["C","D","A","C","A","A","B","A","D","C"]
print(len(a_key))
while True:
        for i in q_bank:
            print(i)
            if i==q_bank[0]:
                print('''Your options for the question are:
A) Mamta banarjee
B) Ram Vilash
C) Ashwini Vaishnaw
D) Piyush Goyal  
                      
                      ''')
                ask = input("Do you want to use a lifeline?(yes/no): ")
                if ask=="yes":
                    lifeline(l_lines)
                    
                else:
                    ask=input("Enter your answer(A/B/C/D): ")
                    z=q_bank.index(i)
                    if ask==a_key[z]:
                        print("Congratulations!! You got the right answer.")
                        print("You won Rs.1000")
                    else:
                        print("Sorry your answer wasn't correct, you won Rs.0")
                        break
            if i==q_bank[1]:
                print('''Your options for the question are:
A) Agni
B) Indra
C) Hanuman
D) Ganesha  
                      
                      ''')
                ask = input("Do you want to use a lifeline?(yes/no): ")
                if ask=="yes":
                    lifeline(l_lines)
                    
                else:
                    ask=input("Enter your answer(A/B/C/D): ")
                    z=q_bank.index(i)
                    if ask==a_key[z]:
                        print("Congratulations!! You got the right answer.")
                        print("You won Rs.2000")
                    else:
                        print("Sorry your answer wasn't correct, you won Rs.0")
                        break
            if i==q_bank[2]:
                print('''Your options for the question are:
A) Money 
B) Flowers
C) Leaves
D) Fruits  
                      
                      ''')
                ask = input("Do you want to use a lifeline?(yes/no): ")
                if ask=="yes":
                    lifeline(l_lines)
                    
                else:
                    ask=input("Enter your answer(A/B/C/D): ")
                    z=q_bank.index(i)
                    if ask==a_key[z]:
                        print("Congratulations!! You got the right answer.")
                        print("You won Rs.5000")
                    else:
                        print("Sorry your answer wasn't correct, you won Rs.0")
                        break
            if i==q_bank[3]:
                print('''Your options for the question are:
A) Bangalore
B) Maysore
C) Jaipur
D) Kochi  
                      
                      ''')
                ask = input("Do you want to use a lifeline?(yes/no): ")
                if ask=="yes":
                    lifeline(l_lines)
                    
                else:
                    ask=input("Enter your answer(A/B/C/D): ")
                    z=q_bank.index(i)
                    if ask==a_key[z]:
                        print("Congratulations!! You got the right answer.")
                        print("You won Rs.10000")
                    else:
                        print("Sorry your answer wasn't correct, you won Rs.0")
                        break
            if i==q_bank[4]:
                print('''Your options for the question are:
A) Rabindranath Tagore
B) Lal Bahadur Shastri
C) Chetan Bhagat
D) RK Narayan
                      
                      ''')
                ask = input("Do you want to use a lifeline?(yes/no): ")
                if ask=="yes":
                    lifeline(l_lines)
                    
                else:
                    ask=input("Enter your answer(A/B/C/D): ")
                    z=q_bank.index(i)
                    if ask==a_key[z]:
                        print("Congratulations!! You got the right answer.")
                        print("You won Rs.20000")
                    else:
                        print("Sorry your answer wasn't correct, you won Rs.10000")
                        break
            if i==q_bank[5]:
                print('''Your options for the question are:
A) 6
B) 7
C) 8
D) 9 
                      
                      ''')
                ask = input("Do you want to use a lifeline?(yes/no): ")
                if ask=="yes":
                    lifeline(l_lines)
                    
                else:
                    ask=input("Enter your answer(A/B/C/D): ")
                    z=q_bank.index(i)
                    if ask==a_key[z]:
                        print("Congratulations!! You got the right answer.")
                        print("You won Rs.40000")
                    else:
                        print("Sorry your answer wasn't correct, you won Rs.10000")
                        break
            if i==q_bank[6]:
                print('''Your options for the question are:
A) 13 September
B) 14 September
C) 14 July
D) 15 August
                      
                      ''')
                ask = input("Do you want to use a lifeline?(yes/no): ")
                if ask=="yes":
                    lifeline(l_lines)
                    
                else:
                    ask=input("Enter your answer(A/B/C/D): ")
                    z=q_bank.index(i)
                    if ask==a_key[z]:
                        print("Congratulations!! You got the right answer.")
                        print("You won Rs.80000")
                    else:
                        print("Sorry your answer wasn't correct, you won Rs.10000")
                        break
            if i==q_bank[7]:
                print('''Your options for the question are:
A) 28
B) 29
C) 31
D) 30
                      
                      ''')
                ask = input("Do you want to use a lifeline?(yes/no): ")
                if ask=="yes":
                    lifeline(l_lines)
                    
                else:
                    ask=input("Enter your answer(A/B/C/D): ")
                    z=q_bank.index(i)
                    if ask==a_key[z]:
                        print("Congratulations!! You got the right answer.")
                        print("You won Rs.160000")
                    else:
                        print("Sorry your answer wasn't correct, you won Rs.10000")
                        break
            if i==q_bank[8]:
                print('''Your options for the question are:
A) Agra
B) Punjab
C) Mumbai
D) New Delhi
                      
                      ''')
                ask = input("Do you want to use a lifeline?(yes/no): ")
                if ask=="yes":
                    lifeline(l_lines)
                    
                else:
                    ask=input("Enter your answer(A/B/C/D): ")
                    z=q_bank.index(i)
                    if ask==a_key[z]:
                        print("Congratulations!! You got the right answer.")
                        print("You won Rs.320000")
                    else:
                        print("Sorry your answer wasn't correct, you won Rs.10000")
                        break
            if i==q_bank[9]:
                print('''Your options for the question are:
A) Sarat Chandra Chattopadhyay
B) Rabindranath Tagore
C) Bankim Chandra Chatterjee
D) Ishwar Chandra Vidyasagar
                      
                      ''')
                ask = input("Do you want to use a lifeline?(yes/no): ")
                if ask=="yes":
                    lifeline(l_lines)
                    
                else:
                    ask=input("Enter your answer(A/B/C/D): ")
                    z=q_bank.index(i)
                    if ask==a_key[z]:
                        print("Congratulations!! You got the right answer.")
                        print("You won Rs.640000")
                    else:
                        print("Sorry your answer wasn't correct, you won Rs.320000")
                        break
print("Thanks for playing!")

#To be continued.