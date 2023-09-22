"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {"input": [10, 3], "answer": 1},
        {"input": [14, 4], "answer": 2},
        {"input": [27, 4], "answer": 3},
        {"input": [10, 5], "answer": 0},
        {"input": [10, 1], "answer": 0},
        {"input": [5, 7], "answer": 5},
        {"input": [7, 5], "answer": 2}
    ],
    "Extra": [
        {"input": [100, 17], "answer": 15},
        {"input": [98765, 1234], "answer": 45}
    ]
}
