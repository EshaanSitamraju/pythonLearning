#This is a test to  find the square of any number
numberofAttemptsAllowed=5
i=0
while i<numberofAttemptsAllowed:
    num1 = float((input("Please enter the number of which's square you want to find  - ")))
    square=num1*num1
    print("The number you have chosen is - ", num1)
    print("The square of the number you have chosen is - ", square)
    print("Now you know the square of the number you have chosen")
    print("Would you like to calculate the the square of any number again? ;)")
    choice=str(input("Enter yes or no - "))
    print('Oke')
    if choice=="no":
        print("I'll see you next time")
        break
    elif choice=="yes":
            if i==numberofAttemptsAllowed:
                print("Enjoy your calculation spree")
    i+=1
print("Sorry to say, but you exeeded the number of attempts")
