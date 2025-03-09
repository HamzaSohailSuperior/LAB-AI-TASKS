def dynamic_calculator(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

expression = "1 + 2 * 3 * (4 - 5 / 4) - (3 / 5)"
result = dynamic_calculator(expression)
print(f"The result of the expression '{expression}' is: {result}")