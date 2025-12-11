
from functools import lru_cache

@lru_cache(maxsize = None)
def small_rec(init, dac, fft):
    if init == "out":
        return dac and fft
    res = 0
    for to in data[init]:
        res += small_rec(to, dac or (init == "dac"), fft or (init == "fft"))
    return res


with open("entry.txt") as my_file:
    data = dict()
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            continue
        data[line[:3]] = tuple(line[4:].split())
    res = small_rec("svr", False, False)

print(res)
