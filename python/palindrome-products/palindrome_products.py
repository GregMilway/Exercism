# palindrome_products.py
#calculate the smallest, and largest palindrome based on smallest and largest factors

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def smallest_palindrome(max_factor, min_factor = 0):
    cands = [(n*m,(n,m)) for n in range(min_factor,max_factor+1)
                            for m in range(min_factor,max_factor+1) if is_palindrome(n*m)]
    return min(cands)

def largest_palindrome(max_factor, min_factor = 0):
    cands = [(n*m,(n,m)) for n in range(max_factor,min_factor-1,-1)
                            for m in range(max_factor,min_factor-1,-1) if is_palindrome(n*m)]
    return max(cands)
