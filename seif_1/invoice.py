class Invoice:
    
    def __init__(self, invoice_number:str, customer_name:str, amount:float, tax_rate=0.17):
        self.invoice_number = invoice_number  
        self.customer_name = customer_name    
        self._amount = amount      
        self._tax_rate = tax_rate             
        self.is_paid = False   
        
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError('הסכום לא יכול להיות שלילי!')
        self._amount = value
    
    @property
    def tax_rate(self):
        return self._tax_rate
    
    #מתודות
    def total_with_tax(self): 
        return self._amount* (1+self._tax_rate)
    
    def mark_as_paid(self):
        self.is_paid = True
    
    def __str__(self):
        return f"""
        --- חשבונית ---
        מספר חשבונית: {self.invoice_number}
        שם לקוח: {self.customer_name}
        סכום לפני מס: {self._amount} ₪
        שיעור מס: {self._tax_rate * 100}%
        סכום כולל מס: {self.total_with_tax()} ₪
        סטטוס תשלום: {'שולמה' if self.is_paid else 'לא שולמה'}
        """