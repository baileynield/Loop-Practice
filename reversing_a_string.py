def reverse_while(s: str) -> str:
    ns = ""
    i = len(s) -1
    while i >= 0:
        ns += s[i]
        i -= 1
    return ns

def reverse_for(s: str) -> str:
    ns = ""
    for r in range(len(s)):
        index = len(s) - 1 - r
        reversed_char = s[index]
        ns += reversed_char
    return ns

def reverse_foreach(s: str) -> str:
    ns = ""
    for char in s:
        ns = char + ns
    return ns


s = "hello"
print(reverse_while(s))
print(reverse_for(s))
print(reverse_foreach(s))
