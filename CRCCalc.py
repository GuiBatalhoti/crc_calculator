generator = '100000111'


def encodeMessage(message, generator) -> str:
    #funtion to encode the data to be sent
    messade_with_zeros = message + '0'*(len(generator)-1)

    division_result = mod2div(messade_with_zeros, generator)
    return message + division_result


def decodeMessage(message: bytes, generator) -> str:
    #funtion to eecode the data received
    messade_with_zeros = message.decode() + '0'*(len(generator)-1)

    division_result = mod2div(messade_with_zeros, generator)
    return division_result


def mod2div(dividend, divisor) -> int:
    #length of the binarys
    len_dividend = len(dividend)
    len_divisor = len(divisor)

    #the first dividend slice
    dividend_slice = dividend[0:len_divisor]

    while len_divisor < len_dividend:
        #verifing if is nedded to do the 'XOR'
        if dividend_slice[0] == '1': #leftmost bir is 1
            #XOR the slice and dividend
            #and take the next bit
            dividend_slice = xor(divisor, dividend_slice) + dividend[len_divisor]            
        else: #leftmost bir is 0
            #make the 'XOR' wiht zeros and take the next bits
            dividend_slice = xor('0'*len_divisor, dividend_slice) + dividend[len_divisor]

        len_divisor += 1

    #treating the last bits, to don't take the next bist, witch don't exist
    if dividend_slice[0] == '1':
        dividend_slice = xor(divisor, dividend_slice)
    else:
        dividend_slice = xor('0'*len_divisor, dividend_slice)


    return dividend_slice


def xor(a, b):
 
    # initialize result
    result = []
 
    # Traverse all bits, if bits are
    # same, then XOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
 
    return ''.join(result)