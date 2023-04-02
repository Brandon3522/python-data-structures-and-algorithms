



# 217: Contains duplicate
# Needed help
def containsDuplicate(nums: list[int]) -> bool:
    # Create set, contains no duplicates
    remove_duplicates = set()

    # Loop over list,
    # If the number is in set return True,
    # Otherwise return False
    for num in nums:
        if num in remove_duplicates:
            return True
        remove_duplicates.add(num)
    return False

print(containsDuplicate([1,2,3,4]))
print('#######################################')

# 242: Valid anagram
# Correct
def isAnagram(s: str, t: str) -> bool:
    s_list = []
    t_list = []

    for char in s:
        s_list.append(char)
    for char in t:
        t_list.append(char)

    s_list.sort()
    t_list.sort()

    if s_list == t_list:
        return True
    else:
        return False
# Hash answer
def isAnagram(s: str, t: str) -> bool:
    pass

print('#######################################')
# two sum practice
# brute force
def two_sum(nums: list, target: int):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                return result  # return since only one match expected

# two sum hash
def two_sum_hash(nums: list, target: int):
    hash = {}  # val : index

    for i, val in enumerate(nums):
        diff = target - val
        if diff in hash:
            return [hash[diff], i]
        hash[val] = i



two_sum_result = two_sum([2,7,11,15], 9)
print(f'Two sum result: {two_sum_result}')

two_sum_hash_result = two_sum_hash([2,7,11,15], 9)
print(f'Two sum hash: {two_sum_hash_result}')
print('#######################################')

# Leetcode #20
def valid_parentheses(s: str):
    stack = []
    hash = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in hash:
            if stack and stack[-1] == hash[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    if not stack:
        return True
    else:
        return False
valid_paretheses_result = valid_parentheses(']')
print(f'Valid Parentheses: {valid_paretheses_result}')
print('#######################################')

# 9: Palindrome Number
# Including negative numbers
# O(n)
def isPalidrome(x: int) -> bool:
    nums = [num for num in str(x)]
    print(nums)
    nums_reverse = nums[::-1]
    # If first value is neg, return false
    if nums[0] == '-':
        return False
    elif nums == nums_reverse:
        return True
    else:
        return False
isPalindrome_result = isPalidrome(10)
print(f'Is Palindrome: {isPalindrome_result}')
print('#######################################')


def isAnagram_0(s: str, t: str) -> bool:
    if len(s) == 1 and len(t) == 1:
        return True
    s_list = [char for char in s]
    t_list = [char for char in t]
    s_list.sort()
    t_list.sort()

    if len(s) == len(t):
        if s_list == t_list:
            return True
        else:
            return False
    else:
        return False

is_anagram_result = isAnagram_0('anagram', 'nagaram')
print(f'Is Anagram: {is_anagram_result}')
print('#######################################')


def isAnagram01(s: str, t: str) -> bool:
    s_list = []
    t_list = []

    for char in s:
        s_list.append(char)
    for char in t:
        t_list.append(char)

    s_list.sort()
    t_list.sort()

    if s_list == t_list:
        return True
    else:
        return False

is_anagram_result01 = isAnagram01('anagram', 'nagaram')
print(f'Is anagram 01: {is_anagram_result01}')

test_list = ['a', 'n', 'a', 'g', 'r', 'a', 'm']
test_list.remove('a')
print('#######################################')


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: [ListNode]):
        prev = None
        current = head

        if current is None:
            return current

        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev

# solution = Solution()
# node1 = ListNode(1)
# node2 = ListNode(2)
# node1.next = node2
# reverseList_result = solution.reverseList([1, 2])
# print(f'Reverse List: {reverseList_result}')
print('#######################################')


# 704: Binary Search
# O(log n)
def binarySearch(nums: list, target: int):
    start = 0
    end = len(nums) - 1
    mid = len(nums) // 2

    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return nums.index(target)  # OR return mid since we need index
        if target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1



binarySearch_result = binarySearch([-1,0,3,5,9,12], 9)
print(f'Binary search: {binarySearch_result}')
print('#######################################')

# Not solved correctly yet
def my_validParenth(s):
    if len(s) == 1:
        return False
    hashMap = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []

    for char in s:
        if char in hashMap:
            if len(stack) > 0 and stack[-1] == hashMap[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    if len(stack) == 0:
        return True
    else:
        return False


my_validParenth_result = my_validParenth('()')
print(f'Valid parentheses: {my_validParenth_result}')
print('#######################################')

# 49: Group Anagrams
def my_groupAnagrams(strs: list[str]):
    result = {}

    if strs[0] == '' and len(strs) == 1:
        return [['']]
    elif len(strs) == 1:
        return [strs[0]]

    for word in strs:
        if word == '':
            result[word] = ['']
        sorted_string = ''.join(sorted(word))

        if sorted_string in result:
            result[sorted_string].append(word)
        else:
            result[sorted_string] = [word]

    return list(result.values())

my_groupAnagrams_result = my_groupAnagrams(["",""])
print(f'My group anagrams: {my_groupAnagrams_result}')

# Reverse a string
def reverseString(string):
    reverse = ''
    index = len(string) - 1

    while index >= 0:
        reverse += string[index]
        index -= 1
    return reverse

reverseStringResult = reverseString('reverse')
print(f'Reverse string {reverseStringResult}')

# Fizz buzz
def my_fizzBuzz(n):
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            print(f'{num}: FizzBuzz')
        if num % 3 == 0:
            print(f'{num}: Fizz')
        if num % 5 == 0:
            print(f'{num}: Buzz')

my_fizzBuzz(100)
