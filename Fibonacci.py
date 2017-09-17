a, b = 0, 1
count = int(input("Please Enter an integer: "))
if(count < 0):
    count = 0
    print("Negative Input Changed to Zero")
elif (count == 0):
    print("Zero")

while b < count:
    print(b, end=", ")
    a, b = b, a + b

