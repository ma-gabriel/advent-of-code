
import math

with open("entry.txt") as my_file:
    poles = []
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            continue
        poles.append(tuple(int(elem) for elem in line.split(',')))
    dists = []
    for i, pole1 in enumerate(poles):
        for pole2 in poles[i + 1:]:
            dists.append([math.dist(pole1, pole2), pole1, pole2])
    dists.sort()
    circuits = []
    last = None
    for dist, pole1, pole2 in dists:
        added = False
        for circuit in circuits:
            if pole1 in circuit:
                if added == False:
                    circuit.append(pole2)
                    added = circuit
                else:
                    added += circuit
                    circuit.clear()
                    last = pole1[0] * pole2[0]
            elif pole2 in circuit:
                if added == False:
                    circuit.append(pole1)
                    added = circuit
                else:
                    added += circuit
                    circuit.clear()
                    last = pole1[0] * pole2[0]
        if not added:
            circuits.append([pole1, pole2])
        if len(set(circuits[0])) == len(poles):
            print(pole1[0] * pole2[0])
            break
