balance=100000
correct_pin=1234


try:
    pin=int(input("Enter a pin: "))
    
    if pin==correct_pin:
        print("\nPin Verified Successfully")
       
        while True:
            print("\n----ATM MENU----")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdrawal")
            print("4. Exit")
            
            choice=int(input("Enter your choice: "))
            
            #check balance
            if choice==1:
                print("Your balance is: ",balance)
            
            #deposit amount   
            elif choice==2:
                deposit_amount=int(input("Enter deposit amount: "))
                
                
                if deposit_amount< 0:
                    print("Invalid deposit amount")
                
                else:
                    balance=balance+deposit_amount     
                    print("deposit Successfully")
                
                print("New balance",balance)
                
            #withdraw
            elif choice==3:
                withdraw_amount=int(input("Enter withdrawal amount: "))
        
                if withdraw_amount <= 0:
                    print("Invalid withdrawal amount")
               
                elif withdraw_amount>balance:
                    print("Insufficient balance")
                
            else:
                balance=balance-withdraw_amount
                print("Withdrawal Successful")
                print("Remaining balance",balance)
                
            if choice==4:
                print("Thank you for using ATM!")
                break
            
    else:
        print("Invalid pin")
        print("Please Entered correct pin")
                
            
            
except ValueError:
    print("Please entered number only")    
    
    
  
