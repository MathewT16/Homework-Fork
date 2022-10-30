def main():
    #good working example!
    stringInput = input("enter a string")
    if stringInput.isalpha():
        print("string!")
    else:
        print("not string :(")
        
    #can you google and find what function you should use to check if it's numeric (an int?)?
    intInput = input("enter an int")
    if intInput.isdigit():
        print("int!")
    else:
        print("not int :(")
    
    #what about if it's both letters and numbers?
    alphIntInput = input("Enter letters and numbers")
    if alphIntInput.isalnum():
        print("Letters and numbers!")
    else:
        print("weird characters :(")
       
    #good working example
    asterisk = input("Enter an asterisk please")
    if asterisk == "*":
        print("good!")
    else:
        print("not asterisk :(")

    #now write code to check if the input was either an asterisk OR an ampersand (&)
    askUser = input("Enter an asterisk or an ampersand")
    if askUser == "*":
        print("great!")
    elif askUser == "&":
        print("awesome")
    else:
        print("wrong")
        
    #do the live example we did in class: ask user to input an integer, but before you cast it to an int, check that it's an integer before doing your variable = int(variable) command
    askInt = input("enter an int")
    if askInt.isdigit():
        int(askInt)
    # last challenge: find out how to check if the string input has the substring "marist"
    #google this one ;) substring is the key google term
    substring = input("Show school spirit")
    if "marist" in substring:
        print("Red FOX")
    else:
        print("L")
    
main()
