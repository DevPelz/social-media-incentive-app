
from __future__ import print_function

import africastalking

class AIRTIME:
    def __init__(self):
		
        self.username = "Zaddyy"
        self.api_key = "7e62c3354e8c37df9cc21abb2fee96f5286d7d314cc244ad52c6e508068f1afa"

        
        africastalking.initialize(self.username, self.api_key)

        
        self.airtime = africastalking.Airtime

    def send(self):
        
        phone_number = 'MyPhoneNumber'

       
        amount = "150"
        currency_code = "NGN"

        try:
			
            responses = self.airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
            print (responses)
        except Exception as e:
            print ("Encountered an error while sending airtime:%s" %str(e))

if __name__ == '__main__':
    AIRTIME().send()