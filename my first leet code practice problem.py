class Solution(object):
    def romanToInt(self, s: str) -> int:
        translations = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        number = 0
        prev_value = 0

        for char in s:
            value = translations[char]
            number += value if prev_value <= value else -prev_value
            prev_value = value

        return number

# Get input from the user
roman_numeral = input("Enter a Roman numeral: ")

# Convert the Roman numeral to an integer
result = Solution().romanToInt(roman_numeral)

# Print the result
print("The equivalent integer value is:", result)
