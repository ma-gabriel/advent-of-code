def base_3(n):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(str(n % 3))
        n //= 3
    return ''.join(digits[::-1])

total = 0
print("take some time to execute (about 1 minute). Please wait, there are no infinite loops, promise")
with open("entry.txt") as my_file:
    for line in my_file:
        res = int(line.split(':')[0])
        facts = [int(elem) for elem in line.split(':')[1].split()]
        l = len(facts) - 1;
        for i in range(3 ** l):
            chars = f"{base_3(i) :0>{l}}"
            r = facts[0]
            j = 0
            while j < len(facts) - 1:
                nb = facts[j + 1]
                if chars[j] == '0': r += nb
                elif chars[j] == '1' : r *= nb
                else : r = int(str(r) + str(nb))
                if r > res: break 
                j += 1
            if r == res:
                total += res
                break

print(total)
