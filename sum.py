import math
import random
import string

alphabet = string.ascii_letters


def remove_duplicate(arr):
    sub = []
    for i in arr:
        if i not in sub:
            sub.append(i)
    return sub


def remove_duplicate_2(arr):
    return list(set(arr))


def max_recursion(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        max_arr = arr[0]
        sub_max = max_recursion(arr[1:])
        return sub_max if sub_max > max_arr else sub_max


def sum_recursion(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_recursion(arr[1:])


def count_recursion(arr):
    # find length of an array by using recursion
    if len(arr) == 1:
        return 1
    else:
        return 1 + count_recursion(arr[1:])


def euclid_gcd_recursion(a, b):
    if a % b == 0:
        return b
    else:
        return euclid_gcd_recursion(b, a % b)


def euclid_gcd(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


def gcd_arr(arr):
    gcd = arr[0]
    for i in arr[1:]:
        gcd = euclid_gcd(gcd, i)
    return gcd


def lcm_num(a, b):
    return int((a*b)/(math.gcd(a, b)))


def lcm_arr(arr):
    lcm = arr[0]
    for i in arr[1:]:
        lcm = lcm_num(lcm, i)
    return lcm


def count_digit(num):
    # python build-in function
    return len(str(num))


def count_digit_2(num):
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count


def split_digit(num):
    digit_arr = []
    for i in str(num):
        digit_arr.append(int(i))
    return digit_arr


def split_digit_2(num):
    # math algorithm
    digit_arr = []
    while num != 0:
        digit = num % 10
        digit_arr.insert(0, digit)
        num = num // 10
    return digit_arr


def binary_search(arr, num):  # O(log(n))
    # return index of num in an array if not return none
    low = 0
    high = len(arr) - 1  # array index start with 0

    while low <= high:  # '=' case due to checking index 0 and n-1
        mid = (low + high) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            high = mid - 1
        else:
            low = mid + 1

    return None


def quick_sort(arr):  # O(nlog(n))         worst case: O(n^2)
    if len(arr) < 2:  # include [] and [1]
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def selection_sort(arr):  # O(n^2)
    sort = []
    while arr:
        select = min(arr)
        sort.append(select)
        arr.remove(select)
    return sort


def bubble_sort(arr):  # O(n^2) (bubble or selection sort?)
    n = len(arr)
    for i in range(n-1):
        for j in range(i, n):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


def bubble_sort_2(arr):  # O(n^2)
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def insertion_sort(arr):  # O(n^2)
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        hole = i
        while hole > 0 and arr[hole-1] > val:
            arr[hole] = arr[hole-1]
            hole = i - 1
        arr[hole] = val
    return arr


def estimate_pi(num):
    num_in_square = 0
    num_in_circle = 0

    for i in range(num):
        x = random.uniform(0, 1)  # get float value from 0 to 1
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            num_in_circle += 1
        num_in_square += 1

    return 4*num_in_circle/num_in_square  # circle area/square area = pi * r**2/(2r)**2 = num in circle/num in square


def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)


def anagram_2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    frequent = {}

    for letter in s1:
        if letter not in frequent:
            frequent[letter] = 1
        else:
            frequent[letter] += 1

    for letter in s2:
        if letter in frequent:
            frequent[letter] -= 1

    if all([frequent[letter] == 0 for letter in frequent]):
        return True

    return False


def pair_sum(arr, k):  # O(n)
    # find an index sum to k
    complement_dict = {}  # a dictionary to store the desire value (k-num) and current index.
    pairs = []
    for i in range(len(arr)):
        num = arr[i]
        complement = k - num
        if num in complement_dict:
            pairs.append((complement_dict[num], i))  # store the result
        else:
            complement_dict[complement] = i  # store complement and index
    return pairs


def pair_sum_2(arr, k):  # O(n^2)
    n = len(arr)
    pairs = []
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] + arr[j] == k:
                pairs.append((i, j))
    return pairs


def max_sum_sub(arr):  # Kadane's algorithm  O(n)
    # find the largest sub array sum
    max_current = arr[0]
    max_global = arr[0]
    for val in arr[1:]:
        max_current = max(max_current + val, val)
        if max_current > max_global:
            max_global = max_current
    return max_global


def max_sum_sub_2(arr):  # brute force algorithm O(n^3)
    n = len(arr)
    res = []
    for size in range(1, n+1):  # loop for size of an array
        for start in range(n-size+1):  # loop for start, end index
            sum_arr = 0
            for i in range(start, start + size):
                sum_arr += arr[i]
            res.append(sum_arr)
    return max(res)


def reverse_arr(arr):
    # return reversed(arr) not return a list but return an address!
    # but how can python execute the return ' '.join(reversed(arr))
    # Python build-in function
    arr.reverse()
    return arr


def reverse_arr_2(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def reverse_string(s):
    # Python build-in function
    return ' '.join(reversed(s.split()))


def reverse_string_2(s):
    # Python build-in function
    return ' '.join(s.split()[::-1])


def reverse_string_3(s):
    n = len(s)
    space = [' ']
    words = []
    i = 0

    while i < n and s[i] not in space:
        if s[i] not in space:
            start = i
            while i < n and s[i] not in space:
                i += 1
            end = i
            words.append(s[start:end])
        i += 1

    return ' '.join(reversed(words))


def rotation(arr):
    pass


def common_elements(arr, brr):
    pass


def most_frequent(arr):
    pass


def unique(s):
    pass


def non_repeating(s):
    pass


brr = list(range(10))
print(reverse_arr(brr))
