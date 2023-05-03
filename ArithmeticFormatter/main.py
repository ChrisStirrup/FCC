def arithmetic_arranger(numbers, evaluate=False):
    if len(numbers) > 5:
        print("Error: Too many problems")
    else:
        if evaluate is True:
            for i in numbers:
                problem = i.split()
                if problem[0].isdigit() and problem[2].isdigit():
                    fhproblem = int(problem[0])
                    sign = problem[1]
                    shproblem = int(problem[2])
                    problen = max(len(str(fhproblem)), len(str(shproblem)))
                    if problen > 5:
                        print("Error: Numbers cannot be more than four digits")
                        break
                    else:
                        if sign == '+':
                            solution = fhproblem + shproblem
                            print('''
                                                 {:>4}
                                                {}{:>4}
                                                 {:>4}'''.format(fhproblem, sign, shproblem, solution),
                                  "--" + "-" * problen, end='    ')
                        elif sign == '-':
                            solution = fhproblem - shproblem
                            print('''
                                                 {:>4}
                                                {}{:>4}
                                                 {:>4}'''.format(fhproblem, sign, shproblem, solution),
                                  "--" + "-" * problen, end='    ')
                        else:
                            print("Error: Operator must be '+' or '-'.")
                            break
                else:
                    print("Error: Numbers must only contain digits.")
                    break

        elif evaluate is False:
            for i in numbers:
                problem = i.split()
                if problem[0].isdigit() and problem[2].isdigit():
                    fhproblem = problem[0]
                    sign = problem[1]
                    shproblem = problem[2]
                    problen = max(len(str(fhproblem)), len(str(shproblem)))
                    if problen > 5:
                        print("Error: Numbers cannot be more than four digits")
                        break
                    else:
                        if sign == '-' or sign == '+':
                            print('''
                                     {:>}
                                    {}{:>}
                                    {}'''.format(fhproblem, sign, shproblem, "-" + "-" * problen), end='    ')
                        else:
                            print("Error: Operator must be '+' or '-'.")
                            break
                else:
                    print("Error: Numbers must only contain digits.")
                    break

#example input (for testing)
arithmetic_arranger(["32 - 698", "3081 - 2", "45 + 43", "123 + 49", "2468 - 1234"])
