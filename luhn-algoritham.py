def main(card_number):
    card_translation = str.maketrans({"-": ""})
    translated_card_number = card_number.translate(card_translation)
    verify_card_number(translated_card_number)

def verify_card_number(card_number):
    reverse_card_number = card_number[::-1]
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    
    # Get odd numbers
    odd_digits = reverse_card_number[::2]
    for odd in odd_digits:
        sum_of_odd_digits += int(odd)
    
    
    # Get even numbers
    even_digits = reverse_card_number[1::2]
    for even in even_digits:
        int_even = int(even)
        int_even *= 2
        # Check if even > 10 and resolve it
        if int_even > 10:
            
            # ---- Beginner Approach
            # str_even = str(int_even)
            # digit_one = int(str_even[0])
            # digit_sec = int(str_even[1])
            # int_even = digit_one + digit_sec

            # ----- Advance
            int_even = (int_even % 10) + (int_even // 10)

        sum_of_even_digits += int_even 
    
    # Sum of odd and even
    sum_of_even_odd = sum_of_even_digits + sum_of_odd_digits
    
    # Check if sum of even and odd is divisible by 10
    if sum_of_even_odd % 10 == 0:
        print("Valid")
    else:
        print("Not valid")


main("4782-7800-0066-9211")
