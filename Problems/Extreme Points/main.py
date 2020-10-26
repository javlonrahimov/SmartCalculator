# The following line creates a dictionary from the input. Do not modify it, please
# import operator
#
# test_dict = json.loads(input())
#
# print("min:", min(test_dict.items(), key=operator.itemgetter(1))[0])
# print("max:", max(test_dict.items(), key=operator.itemgetter(1))[0])

operators = ('+', '-', '*', '/', '^', '(', ')')
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def convert_to_postfix(exp):
    exp = exp.replace('(', '( ').replace(')', ' )')
    exp = [i.strip() for i in exp.split()]
    result = ''
    stack = []

    for i in exp:
        if i in operators:
            if len(stack) == 0 or stack[-1] == '(':
                stack.append(i)
            elif i == '(':
                stack.append(i)
            elif i == ')':
                while stack[-1] != '(':
                    result += stack.pop() + ' '
                stack.pop()
            elif precedence[i] > precedence[stack[-1]]:
                stack.append(i)
            elif precedence[stack[-1]] >= precedence[i]:
                while len(stack) > 0 and stack[-1] != '(' and precedence[stack[-1]] >= precedence[i]:
                    result += stack.pop() + ' '
                stack.append(i)
        else:
            result += i + ' '

    while len(stack) > 0:
        result += stack.pop() + ' '

    return result.strip()


def evaluate_postfix(exp):
    exp = [i.strip() for i in exp.split()]
    stack = []
    for i in exp:
        if i not in operators:
            stack.append(i)
        else:
            o1 = stack.pop()
            o2 = stack.pop()
            a = eval(f'{o2} {i} {o1}')
            stack.append(a)
    return stack.pop()


print(convert_to_postfix("8 * 3 + 12 * (4 - 2)"))

print(evaluate_postfix(convert_to_postfix("3 + 8 * ((4 + 3) * 2 + 1) - 6 / (2 + 1)")))
