# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”


def speed(mph):
    if mph > 70:
        overLimit = mph - 70
        points = overLimit / 5
        if points > 12:
            print(f"{points} earnd, license suspended")
        else:
            print(f"over Limit {points} to license")

    if mph < 70:
        print("ok")


speed(160)
