


# Reorder array with even numbers in the beginning
def even_odd(a):
    evens = []
    others = []
    combined = []
    for num in a:
        if num % 2 == 0:
            evens.append(num)
        else:
            others.append(num)

    combined = evens + others
    return combined
array_even_odd = [5, 2, 4, 6, 8, 15, 19]
answer = even_odd(array_even_odd)
print(answer)
print('##################################')


# Delete duplicates from a sorted array
# Return number of items in new array
def no_duplicates(a):
    if not a:
        return 0

    duplicates_removed = []
    elements = 0

    for i in range(1, len(a)):
        if a[i - 1] != a[i]:
            duplicates_removed.append(a[i])
            elements += 1

    return elements

duplcates_array = [1, 1, 2, 2, 3, 3]
no_duplicates_answer = no_duplicates(duplcates_array)
print(no_duplicates_answer)
