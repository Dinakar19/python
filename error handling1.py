try:
     num=int(input("enter the number:"))
     print(num**2)
except (KeyboardInterrupt):
     print("you should have entered a number..........program terminating....... ")
except (ValueError):
     print("Please checmk before you enter.......program terminating........")
print("bye")
