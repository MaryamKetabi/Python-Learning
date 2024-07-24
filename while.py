x = input("num1?\n")
y = input("num2?\n")
Numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

while x > y:
    print("first number is bigger than second one")
    print(Numbers)
    break

z = 0
while z < 10:
    z = z + 1 #attention!
    print(z , end=" | ")
    z = z + 1 #attention!
