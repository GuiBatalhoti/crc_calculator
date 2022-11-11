generator = 0x81


def mod2div(divisor, dividend) -> int:
    #taking in binary and slicing the '0b'
    dividend_bits = bin(dividend)[0:2]
    divisor_bits = bin(divisor)[0:2]

    #length of the binarys
    len_dividend = len(dividend_bits)
    len_divisor = len(divisor_bits)

    #the first dividend slice
    dividend_slice = dividend_bits[0:len_divisor]

    while len_divisor < len_dividend:
        #verifing if is nedded to do the 'XOR'
        if dividend_slice[0] == '1':
            #take the next bit from the binary array and make the 'XOR' as integers
            dividend_slice = format(divisor ^ int(dividend_slice, base=2), f'0{len_divisor - 1}b') + dividend_bits[len_divisor]
        
        else:
            #make the 'XOR' wiht zeros and take the next bits
            dividend_slice = format(int('0'*len_divisor, base=2) ^ int(dividend_slice, base=2), f'0{len_divisor - 1}b') + dividend_bits[len_divisor]

        len_divisor += 1

    #treating the last bits, to don't take the next bist, witch don't exist
    if dividend_slice[0] == '1':
        dividend_slice = format(divisor ^ int(dividend_slice, base=2), f'0{len_divisor - 1}b')
    else:
        dividend_slice = format(int('0'*len_divisor, base=2) ^ int(dividend_slice, base=2), f'0{len_divisor - 1}b')

    return int(dividend_slice, base=2)

def is_valid_crc(message_rcv_with_checksum) -> bool:
    mod = mod2div(int.from_bytes(message_rcv_with_checksum, byteorder='big'), generator)
    print("Division result", mod)
    return mod == 0
