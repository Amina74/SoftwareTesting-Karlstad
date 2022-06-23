import sys


def compute(a, b, operation):
    if operation == "subtract":
        return a - b
    if operation == "add":
        return a + b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b
    else:
        return 'Operation is not defined'


if __name__ == '__main__':
    input(compute(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]))

print("Amina Hamza")
