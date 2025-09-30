# solver.py -- Updated solve_equation function

# (ফাইলের উপরের import অংশগুলো একই থাকবে)
import sympy
from sympy.core.sympify import SympifyError

def solve_equation(equation_str: str) -> str:
    """
    This function takes a mathematical equation as a string
    and uses SymPy to find its solution.
    It can now handle inputs like '2*x = 10' and 'x**2 - 9',
    and also differentiate between real and complex solutions.
    """
    try:
        x, y = sympy.symbols('x y')
        
        if '=' in equation_str:
            left_side_str, right_side_str = equation_str.split('=', 1)
            left_expr = sympy.sympify(left_side_str.strip())
            right_expr = sympy.sympify(right_side_str.strip())
            equation = sympy.Eq(left_expr, right_expr)
            user_query = f"{left_side_str.strip()} = {right_side_str.strip()}"
        else:
            expr = sympy.sympify(equation_str)
            equation = expr
            user_query = f"{equation_str} = 0"

        solution = sympy.solve(equation, x)

        # --- NEW LOGIC STARTS HERE ---
        # Step 3: Check the solution type and format the result
        if not solution:
            return f"No solution found for the equation '{user_query}'."
        else:
            # Check if any solution in the list is not a real number
            has_complex_solution = any(not sol.is_real for sol in solution)
            
            if has_complex_solution:
                return f"No real solution found for the equation '{user_query}'."
            else:
                return f"The solution for the equation '{user_query}' is: {solution}"
        # --- NEW LOGIC ENDS HERE ---

    except SympifyError:
        return f"Sorry, '{equation_str}' could not be understood as a valid mathematical equation."
    except Exception as e:
        return f"Sorry, an unexpected error occurred: {e}"

# (ফাইলের নিচের if __name__ == "__main__": অংশটি একই থাকবে)
if __name__ == "__main__":
    print("AI Math Solver v1.0 is running. Type 'exit' to close.")
    
    while True:
        user_input = input("Enter your equation: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
            
        result = solve_equation(user_input)
        print(result)