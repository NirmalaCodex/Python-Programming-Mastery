Balance = 1000
print("======================================")        

print("----------ATM System----------")
print("1. Check Balance")
print("2. Withdrawl Money")
print("3. Deposit Money")

choice = int(input("Enter your choice: "))

if choice ==1: 
    print(f"Remaining Balance= {Balance}")
elif choice==2:
    withdrawl_amount= float(input("Enter the withdrawal amount: "))
    if withdrawl_amount<= Balance:
        Balance = Balance - withdrawl_amount
        print("Withdrawal successful")
        print(f"Remaining balance: {Balance}")
    
    else: 
        print("Insufficient Balance")

elif choice==3:
    deposit_amount = float(input("Enter the deposit amount: "))
    Balance = Balance + deposit_amount 
    print("Deposit Successful")
    print(f"Remaining Balance {Balance}")
else: 
    primmt("Enter a valid choice from 1,2,3")

print("======================================")