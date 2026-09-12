item1=input("Enter item 1 name: ")
price1=int(input("Enter item 1 price: "))

item2=input("Enter item 2 name: ")
price2=int(input("Enter item 2 price: "))

item3=input("Enter item 3 name: ")
price3=int(input("Enter item 3 price: "))

item4=input("Enter item 4 name: ")
price4=int(input("Enter item 4 price: "))

item5=input("Enter item 5 name: ")
price5=int(input("Enter item 5 price: "))

total=price1+price2+price3+price4+price5
highest=max(price1,price2,price3,price4,price5)
lowest=min(price1,price2,price3,price4,price5)
average=total/5

print("Total bill: ",total)
print("Highest price: ",highest)
print("Lowest price: ",lowest)
print("Average price: ",average)

if total>10000:
    print("You got a discount")
    
else:
    print("No discount")    
