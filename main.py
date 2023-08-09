print("Welcome to the tip calculator!!")

#Getting total bill amount from user
bill_amount = float(input("What was the total bill amount in rs "))

#Asking how much percentage tip that they are going to provide
tip = float(input("What percentage tip would you like to give? 5 , 10 , 15 , 20 "))

#Getting information how many members to split
members = int(input("How many people to spilt the bill "))

#calculating tip percentage into total amount
tip_percentage_amount = (bill_amount /100 ) * tip



#splitting the amount for each head
spilt_amount = ((bill_amount+tip_percentage_amount) / members)

final_amount="{:.2f}".format(spilt_amount)

print(f"Each person should pay {final_amount} rs")
