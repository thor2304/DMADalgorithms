from sympy import *


if __name__ == "__main__":
    print("Use this for calculating O-notation questions."
          "\nIf it says for example log(n) is O(n^0.5)"
          "\nThen output will say that the second function grows faster which means that this is true.")

    n = symbols('n')
    first_function = sympify(input("Input first function:\n"))
    second_function = sympify(input("Input second function:\n"))

    # If first function grows faster it will go towards infinity
    # If second function grows faster it will go towards 0
    # If they're growing at the same rate it's a non 0 number

    limit_expr = limit(first_function/second_function, n, oo)

    first_function = str(first_function).replace('**', '^')
    second_function = str(second_function).replace('**', '^')

    if limit_expr == oo:
        print(f"First function {first_function} grows faster than second function {second_function}")
        print(f"w, Omega")
    elif limit_expr == 0:
        print(f"second function {second_function} grows faster than first function {first_function}")
        print(f"o, O")
    else:
        print("Both functions grow at the same rate")
        print(f"Theta, O, Omega")

    print(f"Limited expression: {limit_expr}")