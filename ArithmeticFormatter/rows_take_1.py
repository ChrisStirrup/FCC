def arithmetic_arranger(numbers, evaluate=False):
    topline = []
    midline = []
    dotline = []
    solutionline = []
    iterate = 0
    if len(numbers) > 5:
        print("Error: Too many problems")
    else:
        for i in numbers:
            problem = i.split()
            if problem[0].isdigit() and problem[2].isdigit():
                top = int(problem[0])
                topline.append(top)
                sign = problem[1]
                midline.append(sign)
                bottom = int(problem[2])
                midline.append(bottom)
                problength = max(len(str(top)), len(str(bottom)))
                if problength >= 5:
                    print("Error: Numbers cannot be more than four digits")
                    break
                else:
                    dot = '--' + "-" * problength
                    dotline.append(dot)
                    if sign == '+':
                        solution = top + bottom
                        solutionline.append(solution)
                    elif sign == '-':
                        solution = top - bottom
                        solutionline.append(solution)
                    else:
                        print("Error: Operator must be '+' or '-'.")
                        break
            else:
                print("Error: Numbers must only contain digits.")
                break
        for i in topline:
            print(" {:>4}".format(topline[iterate]), end = '    ')
            iterate += 1
        iterate = 0
        print()
        for i in topline:
            print("{}{:>4}".format(midline[iterate], midline[iterate+1]), end = '    ')
            iterate += 2
        iterate = 0
        print()
        for i in dotline:
            print(" {}". format(dotline[iterate]), end = '    ')
            iterate += 1
        iterate = 0
        print()
        if evaluate is True:
            for i in solutionline:
                print(" {:>4}".format(solutionline[iterate]), end = '    ')
                iterate += 1
            iterate = 0
            print()

# To Do make it so that lists of less than 5 problems also work
arithmetic_arranger(["32 + 698", "45 + 43", "123 + 49", ], True)
