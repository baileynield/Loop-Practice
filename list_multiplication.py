def list_multiply_while(a: list[int], b: list[int]) -> list[int]:
    c = []
    i = 0
    while i != len(a):
        d = a[i] * b[i]
        i += 1
        c.append(d)
    print(c)
def list_multiply_for(a: list[int], b: list[int]) -> list[int]:
    c = []
    for i in range(len(a)):
        d = a[i] * b[i]
        c.append(d)
    print(c)

def list_multiply_foreach(a: list[int], b: list[int]) -> list[int]:
    pass

a = [1, 2, 3]
b = [4, 5, 6]
r = []
t = []

list_multiply_for(a, b)
list_multiply_while(a, b)
list_multiply_for(r, t)
list_multiply_while(r, t)
