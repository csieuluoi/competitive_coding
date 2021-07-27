import time
# # brute force solution O(n^3)
# def longestPalindrome_BF(s: str) -> str:
#     if len(s) == 1:
#         return s
#     max_length = 1
#     output = ""
#     for i in range(len(s)):
#         for j in range(i, len(s)+1):
#             # print(i, j)
#             sub_str = s[i:j]
#             if len(sub_str) >=2:
#                 if len(sub_str)>max_length:
#                     if sub_str== sub_str[::-1]:
#                         max_length = len(sub_str)
#                         output = sub_str
#     if max_length == 1:
#         return s[0]
#     return output

# # DP
# def longestPalindrome_BFDP(s: str) -> str:
#     if len(s) == 1:
#         return s
#     max_length = 1
#     output = ""
#     palindromes = {}
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             sub_str = s[i:j]
#             if len(sub_str) >=2:
#                 if len(sub_str)>max_length:
#                     if sub_str[1:-1] in palindromes:
#                         # print(sub_str)

#                         if sub_str[1] == sub_str[-1]:
#                             palindromes[sub_str] = len(sub_str)
#                             max_length = len(sub_str)
#                             output = sub_str
#                     elif sub_str == sub_str[::-1]:
#                         # print(sub_str)
#                         if len(sub_str)>max_length:
#                             palindromes[sub_str] = len(sub_str)
#                             max_length = len(sub_str)
#                             output = sub_str

#     # print(palindromes)
#     if max_length == 1:
#         return s[0]
#     return output

# ## around the center method
# def longestPalindrome(s: str) -> str:
#         m = ''  # Memory to remember a palindrome
#         for i in range(len(s)):  # i = start, O = n
#             for j in range(len(s), i, -1):  # j = end, O = n^2
#                 if len(m) >= j-i:  # To reduce time
#                     break
#                 elif s[i:j] == s[i:j][::-1]:
#                     m = s[i:j]
#                     break
#         return m


# ## use binary search: haven't understanded yet ???
# # O(n^2 log n)
# def longestPalindrome(s: str) -> str:
#     best_len = 0
#     best_s = ""
#     n = len(s)
#     for parity in [0, 1]:
#         low = 1
#         high = n
#         if low%2 != parity:
#             low+=1
#         if high%2 != parity:
#             high-=1
#         while low <= high:
#             mid = int((low + high)/2)
#             if mid % 2 != parity:
#                 mid+=1

#             print(mid, high)
#             if mid > high:
#                 break
#             tmp = good(mid, s)
#             if tmp != -1:
#                 if mid > best_len:
#                     best_len = mid
#                     best_s = s[tmp:mid+1]
#                 low = mid + 2
#             else:
#                 high = mid - 2
#     return best_s


# def good(x, s):
#     n = len(s)
#     for L in range(0, n):
#         if L+x <= n:
#             # print(L, x)
#             if is_palindrome(s[L:x+1]):
#                 return L
#     return -1
# def is_palindrome(s):
#     return s==s[::-1]


# Dynamic Programing to get O(n^2)
# check every mid point (there 're 2n-1 mid points in total)
# check all palindromes of any mid point, start from (mid-1:mid+1)
# to longest substring that can be form (balancedly) with that mid point
# there are two cases:
## first: odd # characters palindrome (eg: aba, abcba,...)
## second: even # characters palindrome (eg: aa, abba, abccba,...)
def longestPalindrome(s: str) -> str:
    best_len = 0
    best_s = ""
    n = len(s)
    # palindrome has even # characters eg aba, bcdcb
    for mid in range(n):
        for x in range(n):
            if (mid-x >= 0) and (mid+x < n):
                if s[mid-x] != s[mid+x]:
                    break
                length = 2*x + 1
                if length > best_len:
                    best_len = length
                    best_s = s[mid-x: mid+x+1]

    # palindrome has even # characters eg abba, bcddcb
    for mid in range(n):
        for x in range(1, n):
            if (mid-x+1 >= 0) and (mid+x < n):
                if s[mid-x+1] != s[mid+x]:
                    break
                length = 2*x
                if length > best_len:
                    best_len = length
                    best_s = s[mid-x+1 : mid+x+1]

    return best_s


if __name__ == "__main__":
    s ="abbacddfadf"
    # print(s[0:3])
    # t1 = time.time()
    # print(longestPalindrome_BF(s=s))
    # print(time.time()-t1)

    # t1 = time.time()
    # print(longestPalindrome_BFDP(s=s))
    # print(time.time()-t1)
    t1 = time.time()
    print(longestPalindrome(s))
    print(time.time()-t1)

