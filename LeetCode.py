import collections


# If n mod 3 and 5, add fizzbuzz into index n
# If n mod 3, add fizz into index n
# If n mod 5, add buzz into index n
# Else, add number as a string into list
import heapq

print('FizzBuzz')
def fizzBuzz(n: int):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result

result = fizzBuzz(15)
print(result)
print('#####################################')


# Brute Force, Two sum
# O(n^2)
print('Two sum: brute')
def twoSum(nums: list[int], target: int):
    result = []
    num_length = range(len(nums))
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                return result

result0 = twoSum([2,1,5,3], 4)
print(result0)
print('#####################################')

# Two sum hash map
# Map each value to the index
# O(n)
print('Two sum: hash')
def twoSum_hash(nums: list[int], target: int):
    # add value : index to hashMap
    prevHash = {}
    # loop through hash
    for i, val in enumerate(nums):
        diff = target - val
        if diff in prevHash:
            print(f'Hash: {prevHash}')
            return [prevHash[diff], i]
        prevHash[val] = i
    print(f'Hash: {prevHash}')

twoSumHash = twoSum_hash([2,1,5,3], 4)
print(twoSumHash)
print('#####################################')

# contains duplicate
print('Contains duplicate')
def containsDuplicate(nums: list[int]) -> bool:
    # create hash set
    hash = set()  # only stores values
    # loop through list
    # add value to hash
    # if value in hash
    # return true
    for n in nums:
        if n in hash:
            return True
        hash.add(n)
    return False
print(containsDuplicate([3, 3]))
print('#####################################')



print('palindrome')
# Palindrome
# O(n)
class Solution:
    def isPalindrome(self, x: str) -> bool:
        sep_word = [char for char in x]
        print(sep_word)

        reverse = sep_word[::-1]
        print(reverse)

        if sep_word == reverse:
            return True
        else:
            return False


palindrome = Solution()
word = 'bob'
result = palindrome.isPalindrome(word)

print(f'Palindrome: {word}, {result}')
print('#####################################')

print('Valid anagram')
def isAnagram(s: str, t: str):
    if len(s) != len(t):
        return False

    s_split = [char for char in s]
    print(s_split)
    t_split = [char for char in t]

    for x in s_split:
        if x not in t_split:
            return False
        else:
            t_split.remove(x)
    return True

def isAnagram_hash(s: str, t:str):
    # check lengths
    if len(s) != len(t):
        return False

    s_hash, t_hash = {}, {}

    # populate hash maps
    for i in range(len(s)):
        s_hash[s[i]] = 1 + s_hash.get(s[i], 0)  # get returns the value of the key if the key is in the dictionary
        t_hash[t[i]] = 1 + t_hash.get(t[i], 0)
    print(s_hash)
    print(t_hash)

    if s_hash == t_hash:
        return True
    else:
        return False

s = 'anagram'
t = 'nagaram'
print(f'Valid anagram: {isAnagram(s, t)}')

print(f'Anagram hash: {isAnagram_hash(s, t)}')
print('#####################################')

# Best time to buy and sell stock
def maxProfit(prices: list[int]):
    buy = 0
    sell = 1
    profit = 0
    maxProfit = 0
    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            maxProfit = max(maxProfit, profit)
        else:
            buy = sell
        sell += 1

    return maxProfit


print('#####################################')

# 20: valid parentheses
def validParentheses(s: str):
    stack = []
    hash = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in hash:
            if stack and stack[-1] == hash[char]: # if stack is not empty and has a matching brace
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    if not stack:  # if stack is empty
        return True
    else:
        return False

valid_result = validParentheses('({})')
print(f'Valid parentheses: {valid_result}')
print('#####################################')

# 704: binary search
# O(log n)
def search(nums: list[int], target: int):
    first = 0
    last = len(nums) - 1

    while first <= last:
        mid = (first + last) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            last = mid - 1
        elif nums[mid] < target:
            first = mid + 1
    return -1

binary = [-1,0,3,5,9,12]
print(f'Binary search: {search(binary, 2)}')
print('#####################################')

# 206: reverse linked list

# class ListNode:
#      def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def reverseList(head: [ListNode]) -> [ListNode]:
#     prev = None
#     curr = head
#
#     while curr:  # curr is not null
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt
#
# print(f'Reverse list: {reverseList([1, 2, 3])}')
print('#####################################')

# 21: Merge two sorted lists
# compare nodes from each list
# add node depending on which is the least
# def mergeLists(list1: list, list2: list):
#     sorted = []
#     # add nodes from list 2 and list 1 to sorted
#     while list1:
#         sorted.append(val)
#     # sort sorted
print('#####################################')

# 49: group anagrams
# group anagrams into their own lists
# def groupAnagrams(strs: list[str]):
#     result = []
#     hash = {[]}
#     if strs == ['']:
#         return [strs]
#     elif len(strs) == 1:
#         return [strs]
#
#     # create hash of each string in strs
#     for i in range(len(strs)):
#         hash[strs[i]] = 1 + hash.get(strs[i], 0)
#         print(hash)
#
#
# group_anagrams = ['']
# group_anagrams1 = ["eat","tea","tan","ate","nat","bat"]
# print(f'Group anagrams: {groupAnagrams(group_anagrams)}')
# print(f'Group anagrams1: {groupAnagrams(group_anagrams1)}')

# Use hashmap
# Key = number of each letter
# Value = list of anagrams
def groupAnagrams(strs: list[str]):
    result = {}
    if len(strs) == 0:
        return [['']]
    elif len(strs) == 1:
        return [strs[0]]

    for i in strs:
        x = ''.join(sorted(i))
        if x in result:
            result[x].append(i)
        else:
            result[x] = [i]
    return list(result.values())

strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print('Group anagrams')
print(groupAnagrams(strings))

print('#####################################')

# 226: Invert binary tree
# invert each node, except for the root
# visit every node, swap position of two children, recursively do the rest
# DFS
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

print('#####################################')

# 104: Maximum depth of binary tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n)
class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


print('#####################################')

# 347: Top K frequent elements
# O(n)
def topKFrequent(nums, k):
    frequent = [[] for i in range(len(nums) + 1)]  # create list for each number in nums
    hash = {}
    res = []

    # create hash to count each num
    for num in nums:
        hash[num] = 1 + hash.get(num, 0)

    for n, count in hash.items():
        # index of frequent = the number from nums
        # insert number of counts into index location of number
        frequent[count].append(n)  # value n occurs count number of times

    # descending for loop through frequent
    for i in range(len(frequent) - 1, 0, -1):
        for n in frequent[i]:
            res.append(n)
            if len(res) == k:
                return res

    return res

def topKFrequent_heap(nums, k):
    pass


most_frequent = topKFrequent([1,1,1,2,2,3], 2)
print(f'Top K frequent: ', most_frequent)
print('#####################################')

# 1046: Last stone weight - priority queue
# min heap with negatives, later transferred to absolute value
# O(n logn)
def last_stone_weight(stones):
    stones = [s * -1 for s in stones]  # make all values negative
    heapq.heapify(stones)  # O(n)

    while len(stones) > 1:
        first = heapq.heappop(stones)  # retrieve largest from min heap
        second = heapq.heappop(stones)  # second largest from min heap
        first = abs(first)
        second = abs (second)
        if second < first:
            heapq.heappush(stones, second - first)

    stones.append(0)  # add 0 if no stones

    return abs(stones[0])

last_stone_answer = last_stone_weight([2,7,4,1,8,1])
print(f'Last stone weight: ', last_stone_answer)

# 155: Min stack - stack
# one stack for values
# one stack to maintain minimum values
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        # if len(self.minStack) == 0:
        #     self.minStack.append(val)
        # elif val < self.minStack[-1]:
        #     self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# 128: Longest consecutive sequence
# O(n logn) due to sorting the array
# does not pass all test cases, length adds to any sequence, not the longest sequence
def my_longest_consecutive(nums: list):
    nums.sort()
    length = 1
    # if the num plus 1 equals next value,
    # increment length
    for i in range(len(nums) - 1):
        if (nums[i] + 1) == nums[i + 1]:
            length += 1

    return length

longest_answer = my_longest_consecutive([9,1,4,7,3,-1,0,5,8,-1,6])
print(f'Longest consecutive: {longest_answer}')

# Does the array contain a left neighbor of starting sequence
# O (n)
def neet_longest_consecutive(nums: list):
    nums_set = set(nums)
    longest = 0
    length = 0

    for n in nums:
        # check if its the start of a sequence
        if (n - 1) not in nums_set:  # If the left neighbor is not in the set
            while(n + length) in nums_set:  #
                length += 1
            longest = max(length, longest)
    return longest


print(f'Longest consecutive O(n): {neet_longest_consecutive([0,3,7,2,5,8,4,6,0,1])}')
sort_array = [9,1,4,7,3,-1,0,5,8,-1,6]
sort_array.sort()
print(f'Sorted: {sort_array}')


# 739: Daily temps - stack
# brute force O(n^2)
def dailyTemps(temps: list):
    result = [0] * len(temps)  # array of 0s

    for i in range(len(temps)):
        for j in range(i + 1, len(temps)):
            if temps[i] < temps[j]:
                result[i] = j - i
                break

    return result

print(f'Daily temps: {dailyTemps([73,74,75,71,69,72,76,73])}')

# optimized
def neet_dailyTemps(temps):
    pass


print('#####################################')
# 238: Product of Array Except Self
# Incomplete
def productExceptSelf(nums: list[int]):
    result = []
    for val in range(len(nums)):
        for j in range(val + 1, len(nums)):
            print(f'val: {val} j: {j}')


product = productExceptSelf([24,12,8,6])
print(f'Product of array except self: {product}')
print('#####################################')


# def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#     if list1 and list2 is None:
#         return []
#     elif list1 is None:
#         return list2
#     elif list2 is None:
#         return list1
#
#     dummyNode = ListNode()
#     while list2 is not None and list2 is not None:
#         if list1.val < list2.val:
#             dummyNode.next = list1
#             list1 = list1.next
#         else:
#             dummyNode.next = list2
#             list2 = list2.next
#         dummyNode = dummyNode.next
#
#     return dummyNode.next
print('#####################################')

def neetcode_groupAnagrams(strs: list[str]):
    ans = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    return ans.values()

neetcode_groupAnagrams_result = neetcode_groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(f'Neetcode group anagrams: {neetcode_groupAnagrams_result}')
print('#####################################')











