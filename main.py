print("Welcome to the tip calculator")
bill = input("What was the total bill?")
percentage = input("What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")

bill_per_person = float(bill) / float(people)
percentage_per_person = float(percentage)/100 *bill_per_person
final_bill = bill_per_person + percentage_per_person
final_bill2 = round(final_bill, 2)
print(f"Each person should pay: {final_bill2}")

