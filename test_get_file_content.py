from functions.get_file_content import get_file_content

def test():
    result = get_file_content("calculator", "lorem.txt")
    print("Result for lorem.txt")
    print(len(result))
    print(result[-100:])

    print("\n")

    result = get_file_content("calculator", "main.py")
    print("Result for main.py")
    print(len(result))
    print(result)

    print("\n")


    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for pkg/calculator.py")
    print(len(result))
    print(result)

    print("\n")


    result = get_file_content("calculator", "/bin/cat")
    print("Result for /bin/cat")
    print(len(result))
    print(result)

    print("\n")


    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for pkg/does_not_exist.py")
    print(len(result))
    print(result)


if __name__ == "__main__":
    test()