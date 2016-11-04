
class Decimal:
    def __init__(self, param):
        self.num = param

    def to_bin(self):
        binary_result = []
        bitcount = 0
        num = self.num
        while num >= 1:
            num = int(num)
            if bitcount > 1 and bitcount % 4 == 0:
                binary_result.append(' ')
            binary_result.append(num % 2)
            num /= 2
            bitcount += 1
        while bitcount % 4 != 0:
            binary_result.append(0)
            bitcount += 1
        binary_result.reverse()
        return binary_result

    def to_hex(self):
        pass


class Hexadecimal:
    hexconv = {
        '0': ['0', '0000'],
        '1': ['1', '0001'],
        '2': ['2', '0010'],
        '3': ['3', '0011'],
        '4': ['4', '0100'],
        '5': ['5', '0101'],
        '6': ['6', '0110'],
        '7': ['7', '0111'],
        '8': ['8', '1000'],
        '9': ['9', '1001'],
        'A': ['10', '1010'],
        'B': ['11', '1011'],
        'C': ['12', '1100'],
        'D': ['13', '1101'],
        'E': ['14', '1110'],
        'F': ['15', '1111'],
    }

    def __init__(self, param):
        self.hex = param

    def to_bin(self):
        pass

    def to_dec(self):
        pass


class Binary:
    def __init__(self, param):
        self.bin = list(param)

    def to_dec(self):
        self.bin.reverse()
        count = 0
        dec = 0
        for bit in self.bin:
            if int(bit) == 1:
                dec += 2**count
            count += 1
        return dec

    def to_hex(self):
        pass

# numin = 43  # input('Enter a decimal number: ')
# mynum = Decimal(int(numin))
# print(''.join("{0}".format(n) for n in mynum.to_bin()))
#
# binin = Binary('101011')
# print('Decimal: {}'.format(binin.to_dec()))
