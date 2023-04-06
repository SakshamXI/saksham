def KBC():
    def bol(a):
        import pyttsx3
        pyobj =pyttsx3.init()
        pyobj.say(a)
        pyobj.runAndWait()
    d = [1,2,3,4]
    e = 0
    a = ''' Hello, Welcome to Kon baaanega Crorepati
I am Amitabh Bachchan
There are 5 question
For every question,You will get money but don't know who will give
1st question - 1000 rupees
2nd question - 2000 rupees
3rd question - 3000 rupees
4th question - 4000 rupees
5th question - 5000 rupees
Total - 15000 rupees
 Here's your first question
 What is Mahatma Gandi called?
Your options are:-
1. Father of Nation
2. Mother of Nation
3. Son of Nation
4. Daughter of Nation 
For option 1:- Press1
For option 2:- Press 2
For option 3:- Press 3
For option 4:- Press 4'''
    print(a)
    bol(a)
    i = str(input(" Enter your option:"))
    i = int(i)
    if i == 1:
        i= 1
        if i in d:
            e += 1000
            print((f"you are right,you have won {e}rupees"))
            bol((f"you are right,you have won {e}rupees"))
    else:
        print((f"You are wrong,you have won {e}rupees"))
        bol((f"You are wrong,you have won {e}rupees"))
        exit()
    print('''Here's your 2nd question
 In a year,How many months have 28 days?
Your options are:-
1. 1
2. 6
3. 12
4. 9
Option rules are same as that of 1st question''')
    bol('''Here's your 2nd question
 In a year,How many months have 28 days?
Your options are:-
1. 1
2. 6
3. 12
4. 9
Option rules are same as that of 1st question''')
    i = input("Enter you option:")
    i = int(i)
    if i== 3:
        i= 3
        if i in d:
            e += 2000
            print((f"you are right,you have won {e}rupees"))
            bol((f"you are right,you have won {e}rupees"))
    else:
        print((f"You are wrong,you have won {e}rupees"))
        bol((f"You are wrong,you have won {e}rupees"))
        exit()
    print('''Here's your third question
What is the cube root of 1000?
Your options are:-
1. 10
2. 20
3. 30
4. 40 
Option rules are same as that of 1st question''')
    bol('''Here's your third question
What is the cube root of 1000?
Your options are:-
1. 10
2. 20
3. 30
4. 40 
Option rules are same as that of 1st question''')
    i = input("Enter you option: ")
    i = int(i)
    if i== 1:
        i= 1
        if i in d:
            e += 3000
            print((f"you are right,you have won {e}rupees"))
            bol((f"you are right,you have won {e}rupees"))
    else:
        print((f"You are wrong,you have won {e}rupees"))
        bol((f"You are wrong,you have won {e}rupees"))
        exit()
    print('''Here's your fourth question
Before becoming Prime Minister,What Narendra Modi was?
Your options are:-
1. Tea seller
2. Sweeper
3. Owner of a Big firm
4. C.M
Option rules are same as that of 1st question''')
    bol(''' Here's your fourth question
Before becoming Prime Minister,What Narendra Modi was?
Your options are:-
1. Tea seller
2. Sweeper
3. Owner of a Big firm
4. C.M
Option rules are same as that of 1st question''')
    i = input(" Enter you option:")
    i = int(i)
    if i== 4:
        i= 4
        if i in d:
            e += 4000
            print((f"you are right,you have won {e}rupees"))
            bol((f"you are right,you have won {e}rupees"))
    else:
        print((f"You are wrong,you have won {e}rupees"))
        bol((f"You are wrong,you have won {e}rupees"))
        exit()
    print('''Here's your fifth question
Probability of getting a 1 when we toss a coin?
Your options are:-
1. 1/2
2. 1
3. 2/3
4. 0 
Option rules are same as that of 1st question''')
    bol(''' Here's your fifth question
Probability of getting a 1 when we toss a coin?
Your options are:-
1. 1/2
2. 1
3. 2/3
4. 0 
Option rules are same as that of 1st question''')
    i = input("Enter you option: ")
    i = int(i)
    if i== 4:
        i= 4
        if i in d:
            e += 5000
            print((f"you are right,you have won {e}rupees"))
            bol((f"you are right,you have won {e}rupees"))
    else:
        print((f"You are wrong,you have won {e}rupees"))
        bol((f"You are wrong,you have won {e}rupees"))
        exit()
    print('''Thankyou,For Playing KBC''')

    bol('''Thankyou,For Playing KBC''')
if __name__ == "__main__":
    KBC()
    
