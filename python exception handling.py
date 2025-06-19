9
a=int(input("enter the number"))
print("multiplication of {a} is:")
try:
    for i in range (1,11):
        print(f"{int(a)}*{i}={int(a)*(i)}")
except exception as e:
    print("sorry")
    print("some lines of code")
    print("end of programme")
