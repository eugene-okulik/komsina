import random

salary = int(input('Input your salary '))
bonus = random.choice([True, False])

bonus_to_pay = random.randrange(1000, 5000)

if bonus:
    total_payment = salary + bonus_to_pay
    print(f"{salary}, {bonus} - '${total_payment}'")
else:
    total_payment = salary
    print(f"{salary}, {bonus} - '${total_payment}'")
