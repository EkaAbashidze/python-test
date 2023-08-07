def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(str):
    nums = ""
    not_allowed = ',.!? :;"\')('
    for c in str:
        if c in not_allowed:
            return False
        if c.isdigit():
            nums += c
    if len(str) >= 6 and int(nums[0]) != 0 and (str[0:2]).isalpha() and str[-1].isdigit(): 
        return True
    else:
        return False
    return str

if __name__ == "__main__":
    main()