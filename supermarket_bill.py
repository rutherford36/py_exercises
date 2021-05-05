name = input("Enter the Name of Customer: ")
qty = int(input("Enter the Quantity of item: "))
price = qty * 100
print("Receipt for", name, ": ")
print("-" * 50)
if price <= 500:
    amount = price * 0.95
    disc = (price - amount)
    print("Total Bill after Discount (5%): ", amount, "pesos")
elif 500 < price <= 1000:
    amount = price * 0.90
    disc = (price - amount)
    print("Total Bill after Discount (10%): ", amount, "pesos")
elif 1000 < price <= 2000:
    amount = price * 0.85
    disc = (price - amount)
    print("Total Bill after Discount (15%): ", amount, "pesos")
elif price > 2000:
    amount = price * 0.8
    disc = (price - amount)
    print("Total Bill after Discount (20%): ", amount, "pesos")
print("Detailed Bill ")
print("Item Quantity:                   ", qty)
print("Purchase Amount:                 ", price, "pesos")
print("Discount:                        ", disc, "pesos")
print("=" * 50)
print("Total Bill:                      ", amount, "pesos")
print("=" * 50)
print("Congrats, your savings in this bill: ", disc, "pesos")


OUTPUT :
  
Enter the Name of Customer: Customer
Enter the Quantity of item: 7
Receipt for Customer : 
--------------------------------------------------
Total Bill after Discount (10%):  630.0 pesos
Detailed Bill 
Item Quantity:                    7
Purchase Amount:                  700 pesos
Discount:                         70.0 pesos
==================================================
Total Bill:                       630.0 pesos
==================================================
Congrats, your savings in this bill:  70.0 pesos
