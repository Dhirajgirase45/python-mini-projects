number1=int(input("Enter number 1: "))
number2=int(input("Enter number 2: "))
number3=int(input("Enter number 3: "))
number4=int(input("Enter number 4: "))
number5=int(input("Enter number 5: "))

total=number1+number2+number3+number4+number5
average=total/5
highest=max(number1,number2,number3,number4,number5)
lowest=min(number1,number2,number3,number4,number5)

even_count = 0
odd_count = 0

if number1 % 2 == 0:
    even_count += 1
else:
    odd_count += 1

if number2 % 2 == 0:
    even_count += 1
else:
    odd_count += 1

if number3 % 2 == 0:
    even_count += 1
else:
    odd_count += 1

if number4 % 2 == 0:
    even_count += 1
else:
    odd_count += 1

if number5 % 2 == 0:
    even_count += 1
else:
    odd_count += 1



print("Total: ",total)
print("Average: ",average)
print("Highest: ",highest)
print("Lowest: ",lowest)
print("Even number: ",even_count)
print("Odd even: ",odd_count)


    