# test_solver.py (English Version)

from solver import solve_equation
import pytest

def test_simple_linear_equation():
    """Testing a simple linear equation."""
    input_str = "2*x = 10"
    expected_output = "The solution for the equation '2*x = 10' is: [5]"
    assert solve_equation(input_str) == expected_output

def test_quadratic_equation():
    """Testing a quadratic equation."""
    input_str = "x**2 = 49"
    actual_output = solve_equation(input_str)
    # The order of solutions can vary, so we check for both possibilities
    assert "[-7, 7]" in actual_output or "[7, -7]" in actual_output

def test_expression_format():
    """Testing the old format (... = 0) to ensure it still works."""
    input_str = "x**2 - 9"
    expected_output = "The solution for the equation 'x**2 - 9 = 0' is: [-3, 3]"
    assert solve_equation(input_str) == expected_output

def test_invalid_equation():
    """Testing if the program correctly handles an invalid input string."""
    input_str = "what is my name?"
    expected_output = "Sorry, 'what is my name?' could not be understood as a valid mathematical equation."
    assert solve_equation(input_str) == expected_output

def test_no_real_solution():
    """Testing an equation with no real solutions."""
    input_str = "x**2 = -4"
    expected_output = "No real solution found for the equation 'x**2 = -4'."
    assert solve_equation(input_str) == expected_output