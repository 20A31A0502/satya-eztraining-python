q1="""who is current captain of indian cricket team?
a.Rohit Sharma
b.Virat Kohli
c.Shikhar Dhawan
d.Rishabh Pant"""

q2="""who is the president of usa?
a.Barack Obama
b.Donald Trump
c.Joe Biden
d.Jill Biden"""

q3="""How many teams have qualified for fifa World Cup 2022?
a.24
b.28
c.32
d.36"""

q4="""In which year mangalyaan was launched?
a.2012
b.2013
c.2014
d.2015"""

q5="""how many categories are there in oscar nominations?
a.21
b.22
c.23
d.24"""

questions={q1:"a",q2:"c",q3:"c",q4:"b",q5:"d"}
name=input("Hi what's ur name:")
print("Hello",name,"Welcome to the Quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this question (yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter your answer:")
    if ans==questions[i]:
        print("Wow! you got one point")
        score=score+1
        print("your current score is:",score)
    else:
        print("wrong answer,u lost 1 mark")
        score=score-1
        print("ur current score is:",score)
    flag2=input("Do you want to Quit?(yes/no)")
    if flag2=="yes":
        break
print("Your total score is:",score)
       
