def calculate_luhn_checksum(card_number):
    total_checksum = 0
    is_second_digit = False
    for digit in reversed(card_number):
        digit_value = int(digit)
        if not is_second_digit:
            total_checksum += digit_value
        else:
            digit_value *= 2
            if digit_value >= 10:
                digit_value = digit_value // 10 + digit_value % 10
            total_checksum += digit_value
        is_second_digit = not is_second_digit
    return total_checksum % 10 == 0


def main():
    strNumber = input("NUMBER: ")
    if not strNumber.isdigit():
        print("INVALID")
        return

    if len(strNumber) not in [13, 16, 15]:
        print("INVALID")
        return

    if strNumber.startswith("34") or strNumber.startswith("37"):
        if len(strNumber) == 15 and calculate_luhn_checksum(strNumber):
            print("AMEX")
        else:
            print("INVALID")
    elif strNumber.startswith("4"):
        if len(strNumber) in [13, 16] and calculate_luhn_checksum(strNumber):
            print("VISA")
        else:
            print("INVALID")
    elif strNumber.startswith("5"):
        if len(strNumber) == 16 and strNumber[1] in ['1', '2', '4', '5'] and calculate_luhn_checksum(strNumber):
            print("MASTERCARD")
        else:
            print("INVALID")
    else:
        print("INVALID")


if __name__ == "__main__":
    main()