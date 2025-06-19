#excercise-4
#encoding and decoding

#Coding:

#If the word contains at least 3 characters:

#Remove the first letter.
#Append the removed letter at the end.
#Append three random characters at the beginning and end.
#Else (if the word contains less than 3 characters):
#Simply reverse the string.

#Decoding:

#If the word contains less than 3 characters:
#Reverse the string
#Remove 3 random characters from the start and end.
#Remove the last letter and append it to the beginning.
word = input("enter the script: ")
print("do you want to encode or decode")
choice = int(input("1 for coding and 2 for decoding: "))

def encoding(word):
    length = len(word)
    encoded = ""  # Initialize the encoded variable
    try:
        if length >= 3:
            lang = word[0:1]
            word=word[1:length]
            
            encoded = word + lang
        else:
            encoded = word[::-1]  # Correct method to reverse the string
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print(encoded)

if choice == 1:
    encoding(word)

elif(choice==2):
   def decoding(word):
    length = len(word)
    if length >= 3:
        temp = word[0:length-1]
        last_char = word[length-1]
        decode = temp + last_char
        word = decode
    elif length < 3:
        word = word[::-1]
    print(word)





       
       
    


            

   
            
           
