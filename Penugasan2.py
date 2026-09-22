merchandise_1 = 45000
merchandise_2 = 50000
merchandise_3 = 60000
merchandise_4 = 75000
merchandise_5 = 90000
merchandise_6 = 120000
gift_price = 7500

total_price = merchandise_1 + merchandise_2 + merchandise_3 + merchandise_4 + merchandise_5 + merchandise_6 + gift_price
print("Total price: ", total_price)

len_merchandise = len([merchandise_1, merchandise_2, merchandise_3, merchandise_4, merchandise_5, merchandise_6])
print("Number of merchandise items: ", len_merchandise)

NIM = input("Masukkan NIM anda: ")
if len(NIM) != 3:
    print("NIM is invalid. It should be 3 characters long.")
else:
    print("NIM is valid.")

NIM = 103
bolean = NIM > total_price
if bolean:
    print("NIM is greater than total price.")
else:
    print("NIM is not greater than total price.")