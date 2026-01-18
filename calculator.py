

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def main():
    print("Calculator")

    while True:
        print("\nChoose an operation:")
        print("1 - Add")
        print("2 - Subtract")
        print("3 - Multiply")
        print("5 - exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Done")
            break

        if choice not in ("1", "2", "3"):
            print("Invalid choice.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == "1":
            result = add(num1, num2)

        elif choice == "2":
            result = subtract(num1, num2)

        elif choice == "3":
            result = multiply(num1, num2)

        print("Result:", result)


if __name__ == "__main__":
    main()
