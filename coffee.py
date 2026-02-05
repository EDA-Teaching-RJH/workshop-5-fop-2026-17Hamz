coins = (50, 20, 10,5)
def main ():
    amount_due = 75 
    while amount_due > 0:
     coin = int(input("Please insert a coin:"))

     if coin in coins:
        amount_due -=coin 
        print(amount_due)

    after_payment(abs(amount_due))

def after_payment(moneyleftover):
   if moneyleftover > 0:
      
      
   

main()