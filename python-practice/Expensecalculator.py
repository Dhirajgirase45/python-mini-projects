
Food=int(input("Food: "))
Travel=int(input("Travel: "))
Shopping=int(input("Shopping: "))
Education=int(input("Education: "))
Other=int(input("Other: "))

total=Food+Travel+Shopping+Education+Other
average=total/5
highest=max(Food,Travel,Shopping,Education,Other)
lowest=min(Food,Travel,Shopping,Education,Other)

print("Data of your expense")
print("Total expense: ",total)
print("Average expense: ",average)
print("Highest expense: ",highest)
print("Lowest expense: ",lowest)

