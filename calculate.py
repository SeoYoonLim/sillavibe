def add(x, y):
    """더하기 함수"""
    return x + y

def subtract(x, y):
    """빼기 함수"""
    return x - y

def multiply(x, y):
    """곱하기 함수"""
    return x * y

def divide(x, y):
    """나누기 함수"""
    if y == 0:
        return "0으로 나눌 수 없습니다."
    return x / y

while True:
    print("연산을 선택하세요.")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("5. 종료")

    choice = input("선택 (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("첫 번째 숫자를 입력하세요: "))
            num2 = float(input("두 번째 숫자를 입력하세요: "))
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == '5':
        break
    else:
        print("잘못된 입력입니다.")