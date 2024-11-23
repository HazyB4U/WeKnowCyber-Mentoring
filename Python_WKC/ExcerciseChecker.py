#!/usr/bin/python3

#!/usr/bin/env python3

import ast

def check_functions(node, required_functions):
    """Check if the required functions are present in the code."""
    functions = [n.name for n in ast.walk(node) if isinstance(n, ast.FunctionDef)]
    missing_functions = [func for func in required_functions if func not in functions]
    return missing_functions

def provide_feedback(node):
    """Provide feedback on the code."""
    feedback = []
    for n in ast.walk(node):
        if isinstance(n, ast.For):
            feedback.append("Consider using list comprehensions for better efficiency.")
        if isinstance(n, ast.FunctionDef):
            if len(n.body) > 10:
                feedback.append(f"Function '{n.name}' is too long. Consider breaking it into smaller functions.")
    return feedback

def main():
    # Define the required functions for the assignment
    required_functions = ["function1", "function2", "function3"]

    # Read the student's code from a file
    with open("student_code.py", "r") as file:
        code = file.read()

    # Parse the code into an AST
    tree = ast.parse(code)

    # Check for required functions
    missing_functions = check_functions(tree, required_functions)
    if missing_functions:
        print(f"Missing functions: {', '.join(missing_functions)}")
    else:
        print("All required functions are present.")

    # Provide feedback on the code
    feedback = provide_feedback(tree)
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("No feedback. The code looks good!")

if __name__ == "__main__":
    main()