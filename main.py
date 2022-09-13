

def main():
    try:
        a = int(input('Введите A: '))
        b = int(input('Введите B: '))
        x = int(input('Введите X: '))
        if x >= 8:
            y = (a*a)+ 4 *(x*x)+b/2*x
        else:
            y = (a*a) - 2*x

        print("y = %.1f" % y)
    except ValueError:
        print('Ошибка данные не верны')
    except ZeroDivisionError:
        print('Ошибка деление на ноль')

    input ('Нажмите Enter для выхода')

if __name__ == '__main__':
    main()
