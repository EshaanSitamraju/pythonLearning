#this is for testing the addition of two numbers
numberofAttemptsAllowed=5
i=0
while i<numberofAttemptsAllowed:
    print("Please type the two numbers you want to add")
    num1 = int((input("Please enter first number - ")))
    num2 = int((input("Please enter second number - ")))
    result=num1+num2
    print("The sum of the two numbers you have given is" , result)
    print("Would you like to add any two numbers again? ;)")
    choice=str(input("Enter yes or no - "))
    print('Oke')
    if choice=="no":
        print("I'll see you next time")
        break
    else:
        if i==numberofAttemptsAllowed:
            print("Enjoy your addition spree")
    i+=1
 print("Sorry to say, but you exeeded the number of attempts")