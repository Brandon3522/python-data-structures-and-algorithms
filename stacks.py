

def main():
    print('hello')
    reversed_list = reverse_list([1, 5, 6, 10, 15])
    print(f'Reversed list: {reversed_list}')
    list01 = [5, 4, 9, 10, 20]
    print(f'Pop: {list01.pop()}')


def insertion_sort(list: list):
    for n in range(1, len(list)):
        curr = list[n]
        j = n
        while j > 0 and list[j-1] > curr:
            list[j] = list[j-1]
            j -= 1
        list[j] = curr
    return list

def reverse_list(list: list):
    if len(list) == 0:
        print('Error. List is empty.')
        return
    list = insertion_sort(list)
    reverse = []
    for n in range(len(list)):
        reverse.append(list.pop())
    return reverse

if __name__ == '__main__':
    main()