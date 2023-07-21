def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    nums = ""
    not_allowed = ',.!? :;"\')('
    for c in s:
        if c in not_allowed:
            return False
        if c.isdigit():
            nums += c
    if len(s) >= 6 and int(nums[0]) != 0 and (s[0:2]).isalpha() and s[-1].isdigit(): 
        return True
    else:
        return False
    return s

main()