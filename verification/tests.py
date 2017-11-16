"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""
TESTS = {
    "Basics": [
        {
            "input": [(1, 1), 2],
            "answer": "series(1, 1)",
            "explanation": ["1 + 1 == 2"],
        },
        {
            "input": [(2, 2), 1],
            "answer": "parallel(2, 2)",
            "explanation": ["2 * 2 / (2 + 2) == 1"],
        },
    ],
    "Extra": [
    
    
    
    ],
}
