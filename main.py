print("welcome to the tip calculator")

total_bill = float(input("what was the total bill? $"))
tip_perc = int(input("what percentage tipe would you like to five? 10, 12, or 15%?"))
numOfAttendees = int(input("how many people are splitting the bill? "))

tip = (tip_perc/100) * total_bill
total = tip + total_bill
split = total /numOfAttendees
final_split = round(split, 2)

print(f"Each person splitting will pay {final_split}")
