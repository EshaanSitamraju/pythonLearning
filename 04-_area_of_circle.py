#This is a test to the area of a circle
#Refrence taken from YT- https://www.youtube.com/@parvatcomputertechnology
numberofAttemptsAllowed=5
i=0
while i<numberofAttemptsAllowed:
    r= float((input("Please enter the radius of the circle you want - ")))
    area=3.14156*r*r
    print("The area of the circle you have given is -   ", area)
    print("Now you know the area of your circle")
    print("Would you like to calculate the the area of a circle again? ;)")
    choice=str(input("Enter yes or no - "))
    print('Oke')
    if choice=="no":
        print("I'll see you next time")
        break
    elif choice=="yes":
            if i==numberofAttemptsAllowed:
                
                print("Enjoy your calculation spree ;)")
    i+=1
print("Sorry to say, but you exeeded the number of attempts")