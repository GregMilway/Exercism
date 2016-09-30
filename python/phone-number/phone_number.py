import re

class Phone:
    """Stores a(n american) phone number
    cleans if necessary, and validates.
    has methods to return pretty-fied version
    and area code."""

    def __init__(self,input_num):
        self.number = self.validate_num(input_num)

    def validate_num(self,num):
        num = re.sub(r'\D','',num)
        if len(num) < 10 or len(num) > 11:
            num = "0000000000"
        elif len(num) == 11:
            if num[0] == '1':
                num = num[1:]
            else:
                num = "0000000000"
        return num

    def area_code(self):
        return self.number[0:3]

    def pretty(self):
        return '({}) {}-{}'.format(self.number[:3],self.number[3:6],self.number[6:])
