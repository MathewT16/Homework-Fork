#if you don't know how to play blackjack, tbh not super important but look it up anyway LOL
#this script is going to require some googling: I want you to practice using your resources with this one. But of course if you get stuck, reach out :)
'''instructions: randomly generate three values between 1 and 11. in the function bust: add these three numbers together. if they add up to or less than 21, return the sum. If it's over 21, return 0. If it's over 21 BUT there's an 11 as one of the values, return the sum - 10. '''
import random

#adds the parameters than if check the value of total and depending on what it is return a certain number
def bust(num1,num2,num3):
    totNum = num1 + num2 + num3
    if totNum <= 21:
        return totNum
    elif totNum > 21:
       if num1 == 11 or num2 == 11 or num3 == 11:
            return totNum - 10
    return 0

    


#creates 3 random variables then calls and prints bust
def main():
    num1 = int(random.random() * 11) + 1
    # or random.randint(1,11)
    num2 = int(random.random() * 11) + 1
    num3 = int(random.random() * 11) + 1

    print(bust(num1,num2,num3))
    

main()
