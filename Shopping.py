# Compulsory Task 2
# The following allows the user to enter the names and prices of the products they purchased
Product1 = input("Please enter the first product you purchased:")
Price1 = input("Please enter the price you paid for the product including cents: R")
Product2 = input("Please enter the second product you purchased:")
Price2 = input("Please enter the price you paid for the product including cents: R")
Product3 = input("Please enter the third product you purchased:")
Price3 = input("Please enter the price you paid for the product including cents: R")
# The following converts all the prices to floats
Price1 = float(Price1)
Price2 = float(Price2)
Price3 = float(Price3)
Total = Price1 + Price2 + Price3 # Calculates the total price paid
strTotal = str(Total) # Converst the total amount into a string data type
Average = Total/3.00 # Calculates the average price paid for an item
strAverage = str(Average) # Converts the average price to a string data type
print("The Total amount paid for " + Product1 + ", " + Product2 + " and " + Product3 + " is R" + strTotal + " and the average price for the items is R" + strAverage + ".")
