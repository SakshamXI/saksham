b = [1, 2, 3, 4]
c = 0
print(" Hello, Welcome to Kaun banega Crorepati")
print(" I am Amitabh Bachan")
print(''' Here's your first question
What is Mahatma Gandi called?
Your options are:-
1. Father of Nation
2. Mother of Nation
3. Son of Nation
4. Daughter of Nation ''')
a = int(
  input('''For option 1:- Press1
For option 2:- Press 2
For option 3:- Press 3
For option 4:- Press 4'''))
if a == 1:
  a = 1
  if a in b:
    print("You are right")
    c += 1000
else:
  print("You are wrong,You have won ", c)
  exit()
print()
print(''' Here's your second question
In a year,How many months have 28 days?
Your options are:-
1. 1
2. 6
3. 12
4. 9 ''')
d = int(
  input('''For option 1:- Press1
For option 2:- Press 2
For option 3:- Press 3
For option 4:- Press 4'''))
if d == 3:
  d = 1
  if d in b:
    print("You are right")
    c += 2000
else:
  print("You are wrong,You have won", c)
  exit()
print()
print(''' Here's your third question
What is the cube root of 1000?
Your options are:-
1. 10
2. 20
3. 30
4. 40 ''')
a = int(
  input('''For option 1:- Press1
For option 2:- Press 2
For option 3:- Press 3
For option 4:- Press 4'''))
if a == 1:
  a = 1
  if a in b:
    print("You are right")
    c += 3000
else:
  print("You are wrong,You have won", c)
  exit()
print()
print(''' Here's your fourth question
Before becoming Prime Minister,What Narendra Modi was?
Your options are:-
1. Tea seller
2. Sweeper
3. Owner of a Big firm
4. C.M ''')
a = int(
  input('''For option 1:- Press1
For option 2:- Press 2
For option 3:- Press 3
For option 4:- Press 4'''))
if a == 4:
  a = 4
  if a in b:
    print("You are right")
    c += 4000
else:
  print("You are wrong,You have won", c)
  exit()
print()
print(''' Here's your fifth question
Probability of getting a 1 when we toss a coin?
Your options are:-
1. 1/2
2. 1
3. 2/3
4. 0 ''')
a = int(
  input('''For option 1:- Press1
For option 2:- Press 2
For option 3:- Press 3
For option 4:- Press 4'''))
if a == 4:
  a = 4
  if a in b:
    c += 5000
    print("You are right,You have won,", c)
else:
  print("You are wrong,You have won", c)
