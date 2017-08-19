status_message = "Hey {}, you're so cool. But today is {}, and it's cool"
import time
print(status_message.format(input("Put in your name here please: "), time.strftime("%m/%d/%Y")))
