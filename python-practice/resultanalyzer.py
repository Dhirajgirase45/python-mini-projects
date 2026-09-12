marks1=int(input("Enter Physics marks: "))
marks2=int(input("Enter Chemistry marks: "))
marks3=int(input("Enter Mathematics marks: "))
marks4=int(input("Enter Python marks: "))
marks5=int(input("Enter Data Structures marks: "))

total=marks1+marks2+marks3+marks4+marks5
percentage=total/5
highest=max(marks1,marks2,marks3,marks4,marks5)
lowest=min(marks1,marks2,marks3,marks4,marks5)

print("Total marks- ",total)
print("Percentage- ",percentage)
print("Highest marks- ",highest)
print("Lowest marks- ",lowest)
if marks1>=40 and marks2>=40 and marks3>=40 and marks4>=40 and marks5>=40:
    print("Pass")
    
else:
    print("Fail")    

