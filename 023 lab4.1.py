def luhn_algorithm(card_number):
    digits = [int(digit) for digit in str(card_number)]
    
    checking_digit = digits.pop()
    
    digits.reverse()
    
    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    total_sum = sum(digits) + checking_digit
    
    return total_sum % 10 == 0

card_number = 5893804115457289
if luhn_algorithm(card_number):
    print(f"The card number {card_number} is valid.")
else:
    print(f"The card number {card_number} is invalid.")