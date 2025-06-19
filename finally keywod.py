def func1():
    try:
        l=[1,5,3,4]
        i=int(input("enter index"))
        print(l[i])
        return 1;
    except:
        print("some error occured")
        return 0;
    finally:
        print("i am always executed")

x=func1()
print(x)
