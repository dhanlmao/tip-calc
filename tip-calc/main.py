def tip_calc(total, tip, people):
	total = int(total)
	tip = int(tip)
	people = int(people)
	return((((total/100)*tip)+total)/people)


print("Welcome to the Tip Calculator!")
total_bill = input("What was the total bill?")
tip_perc = input("What percentage of tip would you like to give?")
num_people = input("How many people to split the bill?")

print("Each person should pay: ", tip_calc(total_bill, tip_perc, num_people))

