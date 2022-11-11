

class CRCCalc:
    def __init__(self, data) -> None:
        #data to bem checked
        self.data = data
        #the polynomial binary 
        self.generator = '0b1110010101001010111010100100111'

        self.crc = None

    def calculate(self):
        pass
