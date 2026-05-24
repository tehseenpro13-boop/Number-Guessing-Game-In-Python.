import random

count = 0
score = 0

while True:
 computer = random.randrange(1,11)
 your_choice = int(input("Enter A number between 1-10 :"))
 count = count + 1
 with open("Project_2/Attempts.txt", "w") as f:
    f.write(str(count))
 if(your_choice==computer):
        score = score + 10
        with open("Project_2/Score.txt", "w") as f:
         f.write(str(score))
        print()
        print("Perfect Guess!")
        print()
        print(f"You took {count} Attempts")
        print()
        print(f"Your Score is {score}")
        print()
        again = input("Enter Yes or No if you want to play again :")
        print()
        if(again == "no" or again == "No"):
           print(f"Your Final Score is {score}")
           break
        else:
              count = 0
        
      
    


    
 elif(your_choice < computer):
        print("Too Low!")
       
        
 elif(your_choice > computer):
        print("Too High!")





