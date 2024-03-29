class Convert:
    def __init__(self):
        self.roman_symbols = {
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def convert_to_roman(self, decimal) -> str:
        output = ""
        if 0 < decimal < 400:
            for key, value in self.roman_symbols.items():
                q = decimal // key
                output += value * q
                decimal %= key
        return output

number = int(input("Enter a number: "))
print(Convert().convert_to_roman(number))
