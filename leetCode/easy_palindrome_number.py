## O(log10(n))
def is_palindrome(x: int) -> bool:
        if x<0 or (x%10 == 0 and x!= 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        print(x, reverted_number)
        return x == reverted_number or x==reverted_number//10

## convert to str
def is_palindrome1(x: int) -> bool:
        if x<0:
            return(False)
        lst=str(x)[::-1]

        if x==int(lst) and lst:
            return(True)
        else:
            return(False)

if __name__ == "__main__":
    n = 121
    print(is_palindrome(n))
