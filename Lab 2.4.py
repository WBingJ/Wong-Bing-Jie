# Student ID: 1201200237
# Student Name: Wong Bing Jie

print("Invoice for Fruits Purchase")
print("---------------------------------")

combs=int(input("Enter the quatity (comb) of banana bought: "))
kg=int(input("Enter the amount (kg) of grapes bought: "))

banana_p=1.5
grapes_p=5.6

banana=combs * banana_p
grapes=kg * grapes_p

print("Item\t\t Qty\t Price\t Total")
print("banana (combs)\t\t RM{:.2f}\t RM{:.2f}\t RM{:.2f}".format(combs,banana_p,banana))
print("Grapes (kg)\t\t RM{:.2f}\t RM{:.2f}\t RM{:.2f}".format(kg,grapes_p,grapes))
