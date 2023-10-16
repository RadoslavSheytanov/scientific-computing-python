def arithmetic_arranger(problems, show_results=False):

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    
    if len(problems) > 5:
        return "Error: Too many problems."

    
    results = []

    
    for i, problem in enumerate(problems):
        operand1, operator, operand2 = problem.split(' ')

        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        
        result = int(operand1) + int(operand2) if operator == '+' else int(operand1) - int(operand2)
        results.append(str(result))

        
        max_length = max(len(operand1), len(operand2)) + 2  

        
        first_line += operand1.rjust(max_length)
        second_line += operator + ' ' + operand2.rjust(max_length - 2)
        third_line += '-' * max_length

        
        if show_results:
            fourth_line += results[-1].rjust(max_length)

        
        if i < len(problems) - 1:
            first_line += '    '
            second_line += '    '
            third_line += '    '
            if show_results:
                fourth_line += '    '

    
    arranged_problems = f"{first_line}\n{second_line}\n{third_line}"
    if show_results:
        arranged_problems += f"\n{fourth_line}"

    return arranged_problems
