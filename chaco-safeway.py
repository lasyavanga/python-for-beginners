print('Welcome To Chaco Safeway')
print('Cashier')

# Take hot chocolate
hot_chocolate_count = input('Enter the number of hot chocolates bought: ')
hot_chocolate_price = input('Enter the price of each hot chocolate: ')

# Take chocolate
chocolate_count = input('Enter the number of chocolates bought: ')
chocolate_price = input('Enter the price of each chocolate: ') 

# Calculate
hot_chocolate_total = int(hot_chocolate_count) * float(hot_chocolate_price)
chocolate_total = int(chocolate_count) * float(chocolate_price)

# Total
total = hot_chocolate_total + chocolate_total

# Print
print("Total price is: $" + str(total))