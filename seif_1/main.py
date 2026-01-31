from invoice import *

def main():
    invoice_number = input("הכנס מספר חשבונית: ")
    customer_name = input("הכנס שם לקוח: ")

    while True:
        try:
            amount = float(input("סכום: "))
            invoice = Invoice(invoice_number, customer_name, amount)
            break
        except ValueError as e:
            print(e)

    # מימוש מתודות
    invoice.mark_as_paid() #הפעלת חשבונית שולמה
    invoice.total_with_tax() #חישוב הסכום כולל מס

    print(invoice) #הצגת המופע באמצעות מתודת __str__


if __name__ == "__main__":
    main()

#מטרת הכימוס היא להסתיר את המימוש הפנימי של האובייקט ולאפשר גישה מבוקרת לנתוניו באמצעות מתודות בלבד.
#באמצעות הכימוס ניתן לשלוט על אופן שינוי הנתונים, לבצע בדיקות תקינות (כגון מניעת ערכים שליליים), ולשמור על עקביות ותקינות האובייקט.
#תוצאת הכימוס היא קוד בטוח, קריא וקל יותר לתחזוקה, שבו לא ניתן לשנות נתונים פנימיים באופן לא מבוקר, והאובייקט שומר על מצב תקין לאורך זמן.