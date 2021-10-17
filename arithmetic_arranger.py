def arithmetic_arranger(*problems):
    first_row, second_row, operation, results = [], [], [], []

    # saving data in lists and error checking
    for equation in problems[0]:
        # consider change loops for one big loop
        equation = equation.split()
        val1 = equation[0].isdigit()
        val2 = equation[2].isdigit()

        # Checking if number's lenght is no more than 4
        if len(equation[0]) > 4 or len(equation[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Checking if there's no other signs in input
        if val1 is False or val2 is False:
            return "Error: Numbers must only contain digits."
        first_row.append(equation[0])
        second_row.append(equation[2])

        # Only sums and difference
        if equation[1] == '+' or equation[1] == '-':
            operation.append(equation[1])
        else:
            return "Error: Operator must be '+' or '-'."

    # No more than 5 problems to solve
    if len(first_row) > 5:
        return "Error: Too many problems."

    line1, line2, result, just_line = str(), str(), str(), str()

    if len(problems) > 1:
        if problems[1] is True:
            result = "\n"

    # Taking elements from strings and adding them to lines
    for x in range(len(problems[0])):

        # Counting operations
        if operation[x] == '+':
            results.append(int(first_row[x]) + int(second_row[x]))
        else:
            results.append(int(first_row[x]) - int(second_row[x]))

        # Arranging arithmetic problems vertically
        if len(first_row[x]) > len(second_row[x]):
            line1 = line1 + " " + first_row[x].rjust(len(first_row[x]) + 1) + 4 * " "
            line2 = line2 + operation[x].ljust(0) + second_row[x].rjust(len(first_row[x]) + 1) + 4 * " "
            just_line = just_line + (len(first_row[x]) + 2) * "-" + 4 * " "
            if len(problems) > 1 and problems[1] is True:
                result = result + str(results[x]).rjust(len(first_row[x]) + 2) + 4 * " "
        else:
            line1 = line1 + " " + first_row[x].rjust(len(second_row[x])+1) + 4 * " "
            line2 = line2 + operation[x].ljust(0) + second_row[x].rjust(len(second_row[x]) + 1) + 4 * " "
            just_line = just_line + (len(second_row[x]) + 2) * "-" + 4 * " "
            if len(problems) > 1 and problems[1] is True:
                result = result + str(results[x]).rjust(len(second_row[x]) + 2) + 4 * " "

    return line1.rstrip() + "\n" + line2.rstrip() + "\n" + just_line.rstrip() + result.rstrip()
