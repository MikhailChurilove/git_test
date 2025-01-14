import time
import os

while True:
    with open("test.txt", 'a') as file:
        file.write("Hello world")
        
        time.sleep(30)
