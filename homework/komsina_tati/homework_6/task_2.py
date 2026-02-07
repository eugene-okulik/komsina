for number in range(1, 16):
    if number % 3 == 0 | number % 5 == 0:
        print("FuzzBuzz")
    if number % 3 == 0:
        print("Fuzz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
