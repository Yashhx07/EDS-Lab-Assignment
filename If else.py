import math
number = int(input())
if 1<= number <=9:
    print(number**2)
elif 10<= number <=99:
    print(f"{math.sqrt(number):.2f}")
elif 100<= number <=999:
    print(f"{math.cbrt(number):.2f}")
else:
    print("Invalid")
