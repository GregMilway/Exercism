#detect when a word is an anagram
#Given `"listen"` and a list of candidates like `"enlists" "google"
#"inlets" "banana"` the program should return a list containing
#`"inlets"`.

def is_anagram(a,b):
    return sorted(a) == sorted(b)

def detect_anagrams(keyword,candidates):
    return [cand for cand in candidates if keyword.lower() != cand.lower() and is_anagram(keyword.lower(),cand.lower())]
