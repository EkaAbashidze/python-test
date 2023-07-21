# i = 0

# while i < 3:
#     i += 1
#     print("meaw", i)


# for i in range(1, 11):
#     print("meaw", i)
    
# for _ in range(3):
#     print("meaw")

# print("meaw\n" * 3, end="")

# while True:
#     n = int(input("What's the N?"))
#     if n < 0:
#         continue
#     else:
#         break

# i = 0

# while True:
#     n = int(input("What's the N?"))
#     while i < n:
#         i += 1
#         print("Meaw!!", i)
#     else:
#         break


def main():
    number = get_number()
    print(number)
    meow(number)


def get_number():
    n = int(input("What is your number?"))
    return n   
    
def meow(num):
    for _ in range(num):
        print("meow!", _)
    # i = 0
    # while i < num:
    #     i += 1
    #     print("meaw!", i)

main()