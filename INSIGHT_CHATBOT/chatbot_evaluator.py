from insights_chatbot import query_chatbot

test_cases = [
    {
        "question": "what is the total sales?",
        "expected_answer_contains": "Total"
    },
    {
        "question": "which season has the highest sales?",
        "expected_answer_contains": "winter"
    },
    {
        "question": "what is the churn percentage?",
        "expected_answer_contains": "50.38%"
    },
    {
        "question": "which region has the highest revenue?",
        "expected_answer_contains": "North America"
    }
]

def evaluate_chatbot(test_cases):
    correct = 0

    for case in test_cases:
        print(f"Question: {case['question']}")
        response = query_chatbot(case['question'])
        print(f"Response: {response}")

        if case["expected_answer_contains"].lower() in response.lower():
            print("Correct")
            correct += 1
        else:
            print("Wrong Answer!")

    total = len(test_cases)
    accuracy = (correct/ total) *100
    print(f"Chatbot Accuracy: {accuracy: .2f}%")

if __name__ == "__main__":
    evaluate_chatbot(test_cases)