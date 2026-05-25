def main():
    plate = input("Plate: ")
    validity = is_valid(plate)
    if validity:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not length_check(s):
        return False
    if not digit_check(s):
        return False
    if not order_check(s):
        return False
    if not punctuation_check(s):
        return False
    return True

def digit_check(s):
    if s[0].isdigit() or s[1].isdigit():
        return False
    for i in range(len(s)):
        if s[i] == "0":
            if s[i-1].isalpha():
                return False
    return True

def length_check(s):
    if len(s) > 6 or len(s) < 2:
        return False
    return True

def order_check(s):
    for i in range(len(s)-1):
        if s[i].isdigit():
            if s[i+1].isalpha():
                return False
    return True

def punctuation_check(s):
    return s.isalnum()


if __name__ == "__main__":
    main()
