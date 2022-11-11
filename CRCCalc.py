

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
        divisor_len = len(self.divisor)

        n_bits = self.data

        while divisor_len < len(self.data):
            pass




    def is_valid(self) -> bool:
        return 0 == self.mod2div()
