#create a matrix class

class Matrix:
    def __init__(self,numstring):
        self.rows = self.get_rows(numstring)
        self.columns = self.get_cols(numstring)

    def get_rows(self,numstring):
        return [map(int,row.split()) for row in numstring.split('\n')]

    def get_cols(self,numstring):
        return map(list, zip(*self.get_rows(numstring)))
