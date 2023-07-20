# Hacker Rank: Lonely integer
# O(n)
def lonelyinteger(a):
    # Write your code here
    if len(a) == 1:
        return a[0]

    hash = {}

    # add each value and count to hash
    for i, val in enumerate(a):
        if val in hash:
            hash[val] = hash.get(val, 0) + 1
            continue
        hash[val] = 1


    # return the key with the min value
    minimum = 10000000000
    min_key = 0
    for key, value in hash.items():
        if value < minimum:
            minimum = value
            min_key = key

    return min_key

print(lonelyinteger([1, 1, 2]))
print('#######################################')

# Hacker rank: Plus Minus
def plusMinus(arr):
    numPos = 0
    numNeg = 0
    numZero = 0
    posRatio = 0
    negRatio = 0
    zeroRatio = 0
    arrLength = len(arr)

    for n in arr:
        if n > 0:
            numPos += 1
        elif n == 0:
            numZero += 1
        elif n < 0:
            numNeg += 1

    posRatio = numPos / arrLength
    negRatio = numNeg / arrLength
    zeroRatio = numZero / arrLength

    print(f'{posRatio:.6f}')
    print(f'{negRatio:.6f}')
    print(f'{zeroRatio:.6f}')

print(f'Plus minus: {plusMinus([-4, 3, -9, 0, 4, 1])}')
print('#######################################')

# Hacker rank: Time conversion
# O(1)
def timeConversion(s):
    result = ''
    new_hours = ''
    hours = s[:2]
    am_pm = s[8:]
    mm_ss = s[3:8]

    if hours == '12' and am_pm == 'AM':
        new_hours = '00:'
        result = new_hours + mm_ss
    elif hours == '12' and am_pm == 'PM':
        result = hours + ':' + mm_ss
    elif int(hours) in range(1, 12) and am_pm == 'AM':
        new_hours = hours + ':'
        result = new_hours + mm_ss
    elif int(hours) in range(1, 12) and am_pm == 'PM':
        new_hours = int(hours) + 12
        result = str(new_hours) + ':' + mm_ss

    return result



print(timeConversion('11:59:59PM'))