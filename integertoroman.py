class IntegerToRoman:
    def __init__(self):
        
        self.__roman_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

    def show_mapping(self):
        """Show Roman numerals with values like I = 1"""
        for value, symbol in sorted(self.__roman_map, reverse=True):
            print(f"{symbol} = {value}")

    def convert(self, number: int) -> str:
        """Convert integer to Roman numeral (1 to 3999)"""
        if not isinstance(number, int):
            raise TypeError("Only integers are allowed")

        if number <= 0 or number > 3999:
            raise ValueError("Number must be between 1 and 3999")

        roman_numeral = ""
        for value, symbol in self.__roman_map:
            while number >= value:
                roman_numeral += symbol
                number -= value
        return roman_numeral



converter = IntegerToRoman()


converter.show_mapping()

print("25 =", converter.convert(25))     # XXV
print("999 =", converter.convert(999))   # CMXCIX
print("2025 =", converter.convert(2025)) # MMXXV













            