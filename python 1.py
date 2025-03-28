accounts = {
    1001 : ["ram ","24-08-2025","6790",25000],
    1002 : ["shyam ","15-06-2025","1876",15000],
    1003 : ["rajesh ","19-06-2025","2001",14000],
    1004 : ["rahul ","11-0902025",None,10000]
    }
print("welcome !")
while True:
    print("*****************************")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Pin Generate")
    print("4. Mini Statement")
    print("5. Exit")
    x=int(input("Enter your option: "))
    if x > 5:
          print("choose the correct option")
    else:
        if x == 1:
             accno=int(input("Enter Account Number:"))
             if accno not in accounts:
                 print("No user exists with Account Number")
                
             else:
                 if accounts [accno][-2] is None:
                      print("Generate Pin before withdraw operation")
                 else:
                      Pin = input("Enter pin: ")
                      if accounts[accno][-2] !=Pin:
                          print("Invalid Pin,Try Again")
                      else:
                          amt=int(input("Enter Amount to withdraw"))
                          if amt<=accounts[accno][-1]:
                              accounts[accno][-1] -= amt
                              print("withdraw success")
                          else:
                              print("Insufficient Balance/Fund/Amount")

        elif x == 2:
            accno = int(input("Enter Account Number :"))
            if accno not in accounts:
                print("No user exists with Account Number")
            else:
                amt = int(input("Enter Amount to be Deposited: "))
                accounts[accno][-1] += amt
                print("Deposit Success")          
            
        elif x == 3:
            accno = int(input("Enter Account Number: "))
            if accno not in accounts:
                print("No user exists with Accont Number")
            else:
                if accounts[accno][-2] is not None:
                    print("Pin Already Generated")
                else:
                    Pin = input (" Enter Pin: ")
                    cpin = input(" Reenter pin: ")
                    if Pin!= cpin:
                        print("Pin Does not match")
                    else:
                        accounts[accno][-2]=Pin
                        print("Pin Generated Successfully")
                        
        elif x == 4:
            accno = int(input("Enter Account Number"))
            if accno not in accounts:
                print("No user exists with Account Numnber")
            else:
                if accounts[accno][-2] is None:
                    print("Generate Pin before Mini Statement Operation")
                else:
                    pin = input ("Enter Pin")
                    if accounts[accno][-2]!=pin:
                        print("Invalid Pin, Try Again ")
                    else:
                        print(f"Account number :{accno}")
                        print(f"Name : {accounts[accno][0]}")
                        print(f"Date of birth : {accounts[accno][1]}")
                        print(f"Balance : {accounts[accno][-1]}")
        else:
            print("Thank you!,Visit Again")
            break
print("*****************************")
       

       
       
          
          
        
                
                
                
