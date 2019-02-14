# Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.


def showNumbers(limit):
    for number in range(0, limit):
        if number % 2 == 0:
            print(f"{number} even")
        else:
            print(f"{number} odd")


showNumbers(20)
