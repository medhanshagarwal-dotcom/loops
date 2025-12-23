n=int(input("Enter a number "))
p=int(input("Enter a power for the number: "))
power=1
for i in range(p):
    power= power*n

print(f"The power of {n} & {p} is: ", power)