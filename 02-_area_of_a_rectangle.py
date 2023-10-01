#This is a test to find out the area of a rectangle
numberofAttemptsAllowed=5
i=0
while i<numberofAttemptsAllowed:
    length = float((input("Please enter the leangth you want for the rectangle - ")))
    breadth = float((input("Please enter the breadth you want for the rectangle - ")))
    area=length*breadth
    print("The length is - ", length)
    print("The breadth is - ", breadth)
    print("Area of the rectangle is - ", area)
    print("Now you know the area of the rectangle you have")
    print("Would you like to calculate the area of a rectangle again? ;)")
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
