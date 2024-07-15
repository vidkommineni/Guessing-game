#import random

def checkVal(randomNumber,guess):  #Funsction that takes in randomnum and guess, to calculate the diff
   #returns the difference btwn the user guess and the randomnum
    return guess-randomNumber
def main():  
    
    #randomNum = random.randint(0,100)
    randomNum = 26
    count=0
    print("Guess the secret number! Hint: it's an integer between 1 and 100...")  #giving the user context for the guess. 
    
    while(True):
        try:
            guess = int(input("What is your guess?")) #takes in a value from user
            count+=1 # aadds one to the count
            difference=checkVal(randomNum,guess) 
            if difference==0: #if difference is 0 then the randomnum is guessed, and program will end
                print("You guessed it! It took you",count,"guesses.")
                break
            elif difference>0: #if diff is greater, then the guess is greater
                print("Too high!")
            else:  #When guess is lower
                print("Too low!")
        except: #when user inputs invalid input (i.e. not an int)
            try:
                guess=int(input("Bad input! Try again:"))
                count+=1 # aadds one to the count
                difference=checkVal(randomNum,guess) #calls the checkVal function to see the difference
                if difference ==0: #if difference is 0 then the randomnum is guessed, and program will end
                    print("You guessed it! It took you",count,"guesses.")
                    break
                elif difference>0: #if diff is greater, then the guess is greater
                    print("Too high!")
                else:
                        print("Too low!")  #When guess is lower
            except:  #when user inputs invalid input (i.e. not an int)
                try:
                    guess=int(input("Bad input! Try again:"))
                    count+=1 # aadds one to the count
                    difference=checkVal(randomNum,guess) #calls the checkVal function to see the difference
                    if difference ==0: #if difference is 0 then the randomnum is guessed, and program will end
                        print("You guessed it! It took you",count,"guesses.")
                        break
                    elif difference>0: #if diff is greater, then the guess is greater
                        print("Too high!")
                    else:
                        print("Too low!") #When guess is lower
                except: #when user inputs invalid input (i.e. not an int)
                    try:
                        guess=int(input("Bad input! Try again:"))
                        count+=1 # aadds one to the count
                        difference=checkVal(randomNum,guess) #calls the checkVal function to see the difference
                        if difference ==0: #if difference is 0 then the randomnum is guessed, and program will end
                            print("You guessed it! It took you",count,"guesses.")
                            break
                        elif difference>0: #if diff is greater, then the guess is greater
                            print("Too high!")
                        else:
                            print("Too low!") #When guess is lower
                    except: #when user inputs invalid input (i.e. not an int)
                        guess=int(input("Bad input! Try again:"))
                        count+=1 # aadds one to the count
                        difference=checkVal(randomNum,guess) #calls the checkVal function to see the difference
                        if difference ==0: #if difference is 0 then the randomnum is guessed, and program will end
                            print("You guessed it! It took you",count,"guesses.")
                            break
                        elif difference>0: #if diff is greater, then the guess is greater
                            print("Too high!")
                        else:
                            print("Too low!") #When guess is lower
                
        
            
           
         
main()
