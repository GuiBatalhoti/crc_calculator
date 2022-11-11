

class CRCCalc:
    def __init__(self, data, divisor) -> None:
        #data to be checked
        self.data = data
        #divisor
        self.divisor = divisor
        #the polynomial binary 
        self.generator = '100010111'

        self.crc = None


    def mod2div(self):
        generator_len = len(self.generator)




    def is_valid(self) -> bool:
        pass
