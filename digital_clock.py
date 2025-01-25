import time
import sys
def user_choice(choice):
    if (choice ==1):
        digital_clock()
    else:
        print("Invalied choice")
def digital_clock():
    print("DIsplay the Digital clock")
    while True:
        current_time=time.strftime("%I:%M:%S",time.localtime())
        print(current_time,end='\r')
        time.sleep(1)
print("Enter your choice on digital clock:")
print("1.Digital clock")
user_venkat=int(input())
user_choice(user_venkat)
