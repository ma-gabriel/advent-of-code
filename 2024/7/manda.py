

total = 0
with open("entry.txt") as my_file:
    for line in my_file:
        res = int(line.split(':')[0])
        facts = [int(elem) for elem in line.split(':')[1].split()]
        l = len(facts) - 1;
        for i in range(2 ** l):
            chars = f"{bin(i)[2:] :0>{l}}"
            r = facts[0]
            for j, nb in enumerate(facts[1:]):
                if chars[j] == '0': r += nb
                else : r *= nb
                if r > res: break 
            if r == res:
                total += res
                break


print(total)
