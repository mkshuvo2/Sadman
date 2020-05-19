#Continue

i = 0;
while i<10:
    i = i + 1
    if(i == 5):
        continue
    print("Number is {:>06b}".format(i))

price = 49.3245
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars.".format(quantity, itemno, price)
print(myorder)


quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {0} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#Unicodes
i = 0
while i<256:
    if(i == 10):
        print('\n')
    print(' {:c}'.format(i), end =" ")
    i = i + 1

# Char to Int
print(ord('5'))    # 53
print(ord('A'))    # 65
print(ord('$'))    # 36