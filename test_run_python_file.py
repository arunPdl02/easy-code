from functions.run_python_file import run_python_file

def test():
    result = run_python_file("calculator", "main.py")
    print("run main.py without args")
    print(result)
    print("\n")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("run main.py with 3 + 5 args")
    print(result)
    print("\n")

    result = run_python_file("calculator", "tests.py")
    print("run tests.py")
    print(result)
    print("\n")

    result = run_python_file("calculator", "../main.py")
    print("run .../main.py expected error")
    print(result)
    print("\n")

    result = run_python_file("calculator", "nonexistent.py")
    print("run nonexistent.py")
    print(result)
    print("\n")

    result = run_python_file("calculator", "lorem.txt")
    print("run lorem.txt which is not a python file")
    print(result)
    print("\n")


if __name__ == "__main__":
    test()