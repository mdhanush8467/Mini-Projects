print("Wellcome to learn with esprit")

player=input("do you want to play?")

if player.lower() !="yes":
    quit()
print("ok lets play")
score=0

question=input("How many days do we have in a week?")
if question.lower() =="7":
    print("correct")
    score+=1
else:
    print("incorrect")
question=input("How many hands in human?")
if question.lower() =="2":
    print("correct")
    score+=1
else:
    print("incorrect")
    
print("your score :"+str(score))