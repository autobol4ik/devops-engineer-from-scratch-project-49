from random import randint

DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_LENGTH = 10
MIN_START = 0
MAX_START = 100
MIN_STEP = 1
MAX_STEP = 10
HIDDEN_MARKER = ".."


def make_progression(start, step, length=PROGRESSION_LENGTH):
    return [start + index * step for index in range(length)]


def generate_round():
    start = randint(MIN_START, MAX_START)
    step = randint(MIN_STEP, MAX_STEP)
    progression = make_progression(start, step)
    hidden_index = randint(0, len(progression) - 1)

    correct_answer = str(progression[hidden_index])
    question_items = [str(number) for number in progression]
    question_items[hidden_index] = HIDDEN_MARKER
    question = " ".join(question_items)
    return question, correct_answer
