import time
timestamp = time.strftime('%H:%M:%S')
hour = int(timestamp[:2])  # Extract the hour from the timestamp

from datetime import datetime

def get_current_hour():
    return datetime.now().hour


def greet():
    if 0 <= hour < 5:
         print("A very Good Beignning of the Day")
    elif 5 <= hour < 12:
        print("A very Good Morning")
    elif 12 <= hour < 17:
        print("A very Good Afternoon")
    elif 17 <= hour < 24:
        print("A very Good Evening")
    else:
        print("Certainly a new day")

time.sleep(1)

    
#if greet() ==-1:
   # timestamp = time.strftime('%H:%M:%S')
    #hour = int(timestamp[:2])  # Extract the hour from the timestamp
    #if 0 <= hour < 5:
    # print("A very Good Beignning of the Day")
    #elif 12 <= hour < 17:
        #print("A very Good Afternoon")
    #else:
        #time.sleep(1)
#if greet() == 1:
    #if 5 <= hour < 12:
        #timestamp = time.strftime('%H:%M:%S')
       ## hour = int(timestamp[:2])  # Extract the hour from the timestamp
    #if 5<=hour <12:
        #print("A very Good Morning")
   # elif 17 <= hour < 24:
       # print("A very Good Evening")
    #else:
        #time.sleep(1)
        
    
        
                    

    
