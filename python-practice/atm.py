

try:
    balance=100000
    withdraw_amount=int(input("Enter withdraw amount: "))
    if withdraw_amount < 0:
        raise ValueError("Invalid withdrawal amount")
    elif withdraw_amount>balance:
        print("Insufficient balance")
        
    else:
        print("Withdrawal successful")    
        print("Remaining balance", balance-withdraw_amount)

    
except:
    print("Entered only numbers")    
    
finally:
    print("Transaction completed")    
