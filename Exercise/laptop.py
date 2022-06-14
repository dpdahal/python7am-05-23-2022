print("==========Computer Bazar==========")
print("Product items: 1.Dell(Rs:20000) 2.Toshiba(Rs:30000) 3.Mac(Rs:50000)")
option = int(input("Select any option: "))

dell_price = 0
toshiba_price = 0
mac_price = 0
delivery_charge = 0
p_bag_price = 0
p_plastic_bag_price = 0
p_gift_box_price = 0
tax_amount = 0
quantity = 0

if option == 1:
    quantity = int(input("Enter the quantity: "))
    dell_price = 20000 * quantity

elif option == 2:
    quantity = int(input("Enter the quantity: "))
    toshiba_price = 30000 * quantity
elif option == 3:
    quantity = int(input("Enter the quantity: "))
    mac_price = 50000 * quantity

else:
    print(f"Items not found {option}")
    exit()

print("Delivery Option: 1.Home Delivery(Rs:1000) 2.Pickup(Rs:0)")
delivery_option = int(input("Select any option: "))
if delivery_option == 1:
    delivery_charge = 1000

print("Packing: 1.Bax(Rs:1000) 2.Plastic(Rs:500) 3.Gift box(Rs:5000) 4. None")
packing_option = int(input("Select any option: "))
if packing_option == 1:
    p_bag_price = 1000
elif packing_option == 2:
    p_plastic_bag_price = 500
elif packing_option == 3:
    p_gift_box_price = 5000

total = dell_price + mac_price + toshiba_price

print("Location: 1.KTM(13% tax) 2. LTP(Free) 3.BKT(Free)")
location = int(input("Select any option: "))
if location == 1:
    tax_amount = total * 0.13


grand_total = total + delivery_charge + p_bag_price + p_plastic_bag_price + p_gift_box_price + tax_amount
print("=========Bill================")
print(f"Total Price: {total}  total quantity {quantity} tax amount {tax_amount} grand total {grand_total}")
