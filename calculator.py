

def add(a, b):
    return a + b


def main():
    print("Calculator")

    while True:
        print("\nChoose an operation:")
        print("1 - Add")
        

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Done.")
            break

        if choice != "1":
            print("Only ADD is available for now.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input.")
            continue

        result = add(num1, num2)
        print("Result:", result)


if __name__ == "__main__":
    main()
