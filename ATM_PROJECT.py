
PIN = 2026
BALANCE = 5000
WITHDRAW_MONEY = []
DEPOSIE_MONEY = []
def view_balance():
    if BALANCE  :
        print("=======================================================")
        print("YOUR BALANCE :" "$",BALANCE)
        print("=======================================================")
    elif BALANCE < 0 :
        print("========================================================")
        print("YOUR BALANCE :" "0$",0)
        print("=========================================================")
     
def withdraw_money(withdraw):
    global BALANCE
    if withdraw > BALANCE :
        print("=========================================================")
        print("INSUFFICIANT AMOUNT")
        print("=========================================================")
    else:
        BALANCE -= withdraw
        WITHDRAW_MONEY.append(withdraw)
        print("=========================================================")
        print("WITHDRAW SUCCESFULLLY :",withdraw)
        print("=========================================================")
      
def deposit_money(deposit):
    global BALANCE
    
    BALANCE += deposit 
    print("=======================================================")
    DEPOSIE_MONEY.append(deposit)

    
    
    
    print("DEPOSITE SUCCESSFULLY :",deposit )
    print("=======================================================")


attempt = 0

while attempt < 3:
    print("\n====== WELCOME TO SECURE BANK ATM ======\n")

    pin = int(input("ENTER YOUR PIN : "))
    if pin != PIN:
        print("INVALID PIN! PLS TRY AGIAN")
        attempt +=1
        if  attempt == 3 :
            print("YOUR ACCOUNT LOCKED")
            
    else :
        
        print("PIN VERIFINATION SUCCESSFULLY\n")
        while True:
            print("\n====================== ATM SIMULATION =========================")
            
            print("CHOOSE ANY OPTION\n 1. BALANCE ENQUAERY\n 2. WITHDRAW AMOUNT\n 3. DEPOSITE AMOUNT\n 4. Transaction History\n 5. EXIT! THANKYOU ")
            
            select = int(input("SELCT ANY OPTION : "))
            if select == 1:
                view_balance()
            elif select == 2:
                withdraw = int(input("ENTER YOUR WITHDRAW AMOUNT : "))
                withdraw_money(withdraw)
            elif select == 3:
                deposit = int(input("ENTER YOUR DEPOSITE AMOUNT : "))
                deposit_money(deposit)
            elif select == 4:
                print("\n============ TRANSACTION HISTORY=============")
                print("1. WITHDRAW HISTORY\n 2. DEPOSITE HISTORY")
                history = int(input("ENTER ANY NUMBER TO VIEW TRANSACTION HISTORY : "))
                if history == 1:
                    if not WITHDRAW_MONEY:
                        print("NOT WITHDRAW HISTORY")
                    else:
                        print("=======================================================")
                        print(F"WITHDRAW AMT HISTORY : ",WITHDRAW_MONEY)
                        print("=======================================================")
                elif history == 2:
                    if not DEPOSIE_MONEY:
                        print("NOT DEPOSIT HISTORY")
                    else:
                        print("=======================================================")
                        print(F"DEPOSIE AMT HISTORY :",DEPOSIE_MONEY)
                        print("=======================================================")
                else:
                    print("INVALID VALUE! PLS TRY AGAIN")
                
            elif select == 5:
                print("EXIT! THANKYOU ")
                break
            else:
                print("INVALID VALUE! PLS ENTER VALUID VALUE")
        break

                    
