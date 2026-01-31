from security import *
from security_types import Stock, Bond, Option

def main():
    print("--- Security Management System ---\n")

    #יצירת security
    name = input("Enter Security Name: ")
    symbol = input("Enter Symbol: ")

    #בדיקת הזנת מחיר תקין
    while True:
        try:
            initial_price = float(input("Enter Initial Price: "))
            my_security = Security(name, symbol, initial_price)
            break 
        except ValueError as e:
            print(f"Error: {e}. Try again.")

    print(f"Initial Status: {my_security}")

    qty = int(input(f"How many units of {my_security.symbol} do you own? ")) 
    print(f"Total Portfolio Value: {my_security.calculate_value(qty):}$")  #מימוש המתודה


    #יצירת Stock
    print("\n--- Stock Section ---")
    msft_stock = Stock("Microsoft", "MSFT", 420.0, 4.2)
    print(msft_stock)
    print(f"Calculated dividend yield: {msft_stock.dividend_yield():}%") #מימוש המתודה


    # יצירת Bond
    print("\n--- Bond Section ---")
    us_bond = Bond("US Treasury 10Y", "US10Y", 1000.0, 4.0)
    print(us_bond)
    print(f"Your Annual Gain: {us_bond.annual_interest_gain()}$") #מימוש המתודה


    # יצירת Option
    print("\n--- Option Section ---")
    amzn_option = Option("Amazon Call", "AMZN_OPT", 175.0, 185.0)
    print(f"Current Market Status: {amzn_option}")
    
    status = "Profitable!" if amzn_option.is_profitable() else "Not profitable yet." #מימוש המתודה
    print(f"Option Status: {status}")

if __name__ == "__main__":
    main()
 

 #הורשה היא מנגנון המאפשר לנו ליצור מחלקה חדשה על בסיס מחלקה קיימת.
 #מטרתה היא ליצור סדר והגיון: היא יוצרת היררכיה לוגית של אבסטרקציות (מהכללי אל הספציפי), להשתמש בקוד חוזר ולמנוע כפל קוד.
