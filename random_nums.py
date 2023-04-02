import random


def random_num(start, end):
    result = []

    for i in range(start, end):
        num = random.randint(1, 49)
        if num not in result:
            result.append(num)

    while len(result) < 15:
        num = random.randint(1, 49)
        if num not in result:
            result.append(num)

    return result


def main():
    print('Hello')

    for i in range(10):
        random_numbers = random_num(0, 15)
        print(f'Random Numbers: {random_numbers}')


if __name__ == '__main__':
    main()