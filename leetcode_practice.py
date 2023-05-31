



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
print('#######################################')

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
print('#######################################')

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
print('#######################################')

# 155: Min Stack
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.minStack:
            self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        if self.minStack:
            return self.minStack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
print('#######################################')

# 704: Binary search
def myBinarySearch(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        midpoint = (start + end) // 2
        if target == nums[midpoint]:
            return midpoint
        if target < nums[midpoint]:
            end = midpoint - 1
        if target > nums[midpoint]:
            start = midpoint + 1
    return -1

myBinarySearchResult = myBinarySearch([-1,0,3,5,9,12], 2)
print(f'My binary search result: {myBinarySearchResult}')
print('#######################################')

# Two Sum: 2 pointers approach
# The list must be sorted !!!!!!!!
def two_sum_2pointer(numbers: list, target: int):
    first = 0
    last = len(numbers) - 1
    result = []
    sum = 0

    while first < last:
        sum = numbers[first] + numbers[last]
        if target == sum:
            result.append(first + 1)
            result.append(last + 1)
            return result

        if sum < target:
            first += 1
        elif sum > target:
            last -= 1

two_sum_2pointer_result = two_sum_2pointer([-1,0], -1)
print(f'Two sum 2 pointer: {two_sum_2pointer_result}')
print('#######################################')

# 15: 3sum
# Incomplete
def threeSum(nums: list):
    first = 0
    second = 1
    last = len(nums) - 1
    result = []

    nums.sort()

    while second < last:
        sum = nums[first] + nums[second] + nums[last]

        if sum == 0:
            result.append([first, second, last])
        if sum > 0:
            pass



print('#######################################')

# 125: Valid Palindrome
# Remove spaces, remove non alpha or numeric chars
# Compare to reverse
def isPalindrome(s: str) -> bool:
    sNoSpaces = []
    reverse = ''
    for char in s:
        if char != ' ':
            sNoSpaces.append(char)

    if len(sNoSpaces) == 0:
        return True

    sNoSpaces = ''.join(sNoSpaces)

    newString = ''.join(char for char in sNoSpaces if char.isalpha() or char.isnumeric())
    newString = newString.lower()

    reverse = newString[::-1]

    if reverse == newString:
        return True
    else:
        return False

isPalindromeresult = isPalindrome("0p")
print(f'Valid palindrome: {isPalindromeresult}')
print('#######################################')

# 49: Group anagrams
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = {}

    for string in strs:
        sorted_string = ''.join(sorted(string))

        if sorted_string in result:
            result[sorted_string].append(string)
        else:
            result[sorted_string] = [string]

    return list(result.values())


groupAnagrams_result = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(f'Group anagrams {groupAnagrams_result}')
print('#######################################')

# Definition for singly-linked list.
def reverseList1(head: [ListNode]) -> [ListNode]:
    prev = None
    current = head

    if current is None:
        return head

    # Reversing each link
    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    # Return prev as new head
    return prev
print('#######################################')

# Group anagrams practice
def groupAnagrams01(strs: list[str]):
    result = {}

    for string in strs:
        # Sort string
        sorted_string = ''.join(sorted(string))

        # Check if in dictionary
        if sorted_string in result:
            # Add string to list values
            result[sorted_string].append(string)
        else:
            # Add list with string to values
            result[sorted_string] = [string]

    # Convert values to list
    return list(result.values())

groupAnagrams01_result = groupAnagrams01(["eat","tea","tan","ate","nat","bat"])
print(f'Group anagrams {groupAnagrams01_result}')
print('#######################################')

def compareTriplets(a, b):
    result = []
    alice_score = 0
    bob_score = 0
    idx = 0

    while idx <= len(a) - 1:
        if a[idx] > b[idx]:
            alice_score += 1
        elif a[idx] < b[idx]:
            bob_score += 1
        idx += 1
    result.append(alice_score)
    result.append(bob_score)

    return result

compareTriplets_result = compareTriplets([1, 2, 3], [3, 2, 1])
print(f'Compare triplets: {compareTriplets_result}')
print('#######################################')

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





































