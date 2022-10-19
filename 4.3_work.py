num_1 = int(input("Введите первое число: "))
mathematical_sign = (input("Введите знак: "))
num_2 = int(input("Введите второе число: "))
match mathematical_sign:
    case "+":
        print(num_1, "+", num_2, "=", (num_1+num_2))
    case "-":
        print(num_1, "-", num_2, "=", (num_1-num_2))
    case "*":
        print(num_1, "*", num_2, "=", (num_1*num_2))
    case "/":
        print(num_1, "/", num_2, "=", (num_1/num_2))
