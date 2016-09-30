#class to check validity of a number based on Luhn's algorithm, and append correct checksum if not.

class Luhn:
    def __init__(self,number = None):
        self.number = number

    def addends(self):
        adds = map(int,str(self.number))[::-1]
        out = []
        for idx, elem in enumerate(adds):
            if idx%2:
                elem *= 2
                if elem > 9:
                    elem -= 9
            out.append(elem)
        return out

    def checksum(self):
        return sum(self.addends())

    def is_valid(self):
        return not self.checksum()%10

    @staticmethod
    def create(number):
        if Luhn(number).is_valid():
            return number
        else:
            chksum = Luhn(number*10).checksum()
            return number*10 + (10 - chksum%10)%10
