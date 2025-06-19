

def find_name(phonebook):
    for name in phonebook:
        if name in phonebook:
            return name
        else:
            print(f"{name} not found,should we append it?")
            answer=input("yes or no")
            if answer=="yes":
                phonebook.append(name)
                return name
            else:
                print("ok") 
                break
print(f"{find_name(phonebook=["Alice", "Bob", "Charlie"])}")
        