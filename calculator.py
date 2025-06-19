# calculator
#excercise 
choice="yes"
while(choice=="yes"):
    input1=float(input("enter value for opertion"))
    input2=float(input("enter value for operation"))
    print("enter number from 1 to 4\n")
    print("-----------------------------------------------------------MENU------------------------------------\n")
    print("1 is for addition\n")
    print("2 is for subtraction\n")
    print("3 is for multiplication\n")
    print("4 is for division\n")
    n=int(input("enter your choice\n"))
    while(n>0 and n<5):
        if(n==1):
            sum=input1+input2
            print(sum)
            break
        elif(n==2):
            difference=input1-input2
            print(difference)
            break
        elif(n==3):
            multiplication=input1*input2
            print(multiplication)
            break
        elif(n==4):
            quitent=input1/input2
            print(quitent)
            break
        else:
            print("thank you but pls select from menu")
    choice=input("do you wish tocontinue the calculator say yes or no")
    if(choice=="no"):
        break
    
    


