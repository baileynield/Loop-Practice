def char_count_while(target: str, c: str) -> int:
    count = 0
    i = 0
    while i < len(target):
        if target[i] == c:
            count += 1
        i += 1
    return count

def char_count_for(target: str, c: str) -> int:
    count = 0
    for i in range(len(target)):
        if target[i] == c:
            count += 1
    return count
    
def char_count_foreach(target: str, c: str) -> int:
    count = 0
    for character in target:
        if character in c:
              count += 1
    return count



s = "hello"
c = "l"

for_each = char_count_foreach(s, c)
for_loop = char_count_for(s, c)
while_loop = char_count_while(s, c)

print(for_each) # Expected output: 2
print(for_loop)
print(while_loop)
