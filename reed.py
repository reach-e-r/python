right_number = 8
k = int(input("guess a number: "))
n = 0
while k != right_number:
    print("try again")
    n += 1
    if n >= 3:
        print("out of guesses!")
        break
    k = int(input("guess a number: "))
else:
    print("you winnn")




