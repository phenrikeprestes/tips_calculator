print("Welcome to the tip calculator!")

total_bill = input("What was the total bill? $  ")

tip = input("How much tip would you like to give? 10, 12, or 15? ")

number_people = input("How many people to split the bill? ")

final_bill = round(float(total_bill)*float(1+float(tip)/100), 2)

per_person = round(final_bill/float(number_people), 2)

print(f"Each person should pay : ${per_person:.2f}")
