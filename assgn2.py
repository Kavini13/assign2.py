class Calculator:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition_of_numbers(self):
        return self.number1 + self.number2

    def subtraction_of_numbers(self):
        return self.number1 - self.number2

    def multiplication_of_numbers(self):
        return self.number1 * self.number2

    def division_of_numbers(self):
        return self.number1 / self.number2


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

obj = Calculator(number1, number2)
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter the choice:"))

    if choice == 1:
        print("Result: ", obj.addition_of_numbers())
    elif choice == 2:
        print("Result: ", obj.subtraction_of_numbers())
    elif choice == 3:
        print("Result: ", obj.multiplication_of_numbers())
    elif choice == 4:
        try:

            result = number1 / number2
        except ZeroDivisionError:

            print("Error! number is not divisible by zero")
        else:

            print(result)

    else:

        print("Invalid choice!!")
