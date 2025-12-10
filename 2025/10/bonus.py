
import scipy
import numpy

res = 0
with open("entry.txt") as my_file:
    for line in my_file:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line) == 0:
            continue

        # This one was so hard i am starting to write doc

        lights, *buttons, joltage = line.split()
        buttons = tuple(tuple(int(elem) for elem in button[1:-1].split(',')) for button in buttons)
        joltage = [int(elem) for elem in joltage[1:-1].split(',')]

        # 1 is for a light that will be triggered, so i can have a matrix
        M_buttons = [[1 if i in button else 0 for i in range(len(joltage))] for button in buttons]

        # A x B = C     where B is M_Buttons and C is the joltage
        # For now it works, that's the first line of the example, see website below (in the history)
        # https://matrixcalc.org/fr/#%7B%7B1,3,0,3,1,2%7D%7D*%7B%7B0,0,0,1%7D,%7B0,1,0,1%7D,%7B0,0,1,0%7D,%7B0,0,1,1%7D,%7B1,0,1,0%7D,%7B1,1,0,0%7D%7D

        # But we need to find A when we have B and C
        # Sadly, we can't just A = C x invert(B) because B is nor a squared matrix, nor have only one solution, so can't be inverted

        # SO we need an algorithm to do it, algo which need to be smarter than me
        # And for that we have linprog, that uses the HiGHS algorithm (by default)
        # it's basically an algorithm that will just see an array of variables (for me only 1s, the first arg) 
        #   and multiply those by A_eq to see if it's b_eq
        # because linprog don't know what we want it to do, we have to adapt and reshape its input to fit the equation,
        #   like transposing T (rotating) so that the rows and columns correspond to the sizes of our solutions, and it can multiply them
        
        # And also by default : the bound of the solutions linprog will search is between 0 and inf
        # so great, that's what we want

        A_eq = numpy.array(M_buttons).T
        b_eq = numpy.array(joltage)

        # integrality is to only have integers in it, not floats (found in the doc below)
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
        res += sum(scipy.optimize.linprog([1] * len(buttons), A_eq=A_eq, b_eq=b_eq, integrality=1).x)
        # we take sum(... .x) because the solution is in x, 
        #   => it's an array corresponding to a 1D matrix that contains all of our buttons presses, so we just sum them
print(int(res))
