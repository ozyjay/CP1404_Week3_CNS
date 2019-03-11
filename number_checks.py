def get_number():
    while True:
        try:
            number = int(input("Enter number: "))
            return number
        except ValueError:
            print("invalid input...")



def main():
    number = get_number()
    if is_even(number):
        print("it's even")
    else:
        print("it's odd")



def is_even(number):
    return number % 2 == 0


main()


