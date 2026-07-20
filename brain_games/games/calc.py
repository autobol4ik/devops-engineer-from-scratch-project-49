from operator import add, mul, sub
from random import choice, randint

DESCRIPTION = "What is the result of the expression?"
MIN_NUMBER = 1
MAX_NUMBER = 100
OPERATIONS = (
    ("+", add),
    ("-", sub),
    ("*", mul),
)


def generate_round():
    left_operand = randint(MIN_NUMBER, MAX_NUMBER)
    right_operand = randint(MIN_NUMBER, MAX_NUMBER)
    operator, calculate = choice(OPERATIONS)

    question = f"{left_operand} {operator} {right_operand}"
    correct_answer = str(calculate(left_operand, right_operand))
    return question, correct_answer
