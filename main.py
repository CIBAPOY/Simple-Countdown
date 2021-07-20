import time as wait
number = input("Number: ")
def countdown(num):
    num = int(num)
    while num > 0:
        print(f"{num}...")
        num -= 1
        wait.sleep(1)
    print("Finished!")
countdown(number)
