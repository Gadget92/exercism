import string

class PhoneNumber:

    def __init__(self, phone_number):
        self.area_code = ""
        self.number = ""
        self.clean(phone_number)

    def clean(self, number):
        digit_clean = "".join(char for char in number if char.isdigit()) 

        if len(digit_clean) == 11 and digit_clean[0] != "1": 
            raise ValueError('Invalid Country Code')

        elif len(digit_clean) == 11 and digit_clean[0] == "1":  
            self.clean(digit_clean[1:])  

        elif len(digit_clean) == 10 and digit_clean[0] not in ["0", "1"] and digit_clean[3] not in ["0", "1"]: 
            self.area_code = digit_clean[0:3] 
            self.number = digit_clean[0:10]  

        else:
            raise ValueError('Invalid Phone Number') 


    def pretty(self):
        return "({}) {}-{}".format(self.area_code[0:3], self.number[3:6], self.number[6:10])  

