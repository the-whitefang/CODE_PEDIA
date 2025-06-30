import pandas as pd
import subprocess

# Load the dataset
df = pd.read_csv("loan_data_1.csv")


def ask_llm(prompt):
    # import pdb;pdb.set_trace()
    # Send prompt to LLaMA 3 via Ollama
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()


def generate_code_from_question(question, sample_data):
    # import pdb;pdb.set_trace()
    prompt = f"""
    You are a data analyst. You are given a CSV dataset with the following structure:
    
    {sample_data}
    
    The user asked the following question about the data:
    "{question}"
    
    Write one-line pandas code that produces the final result, and store it in a variable called 'result'.
    Do not include import statements, comments, or multi-line code. Your code should use 'df' as the DataFrame variable.
        """
    print(f"First Prompt Output: {prompt}") # <---
    return ask_llm(prompt)

def clean_code(code: str) -> str:
    # import pdb;pdb.set_trace()
    code = code.strip("`").strip()
    if code.startswith("python"):
        code = code[len("python"):].strip()
    return code



def rephrase_answer(insight, question):
    # import pdb;pdb.set_trace()
    prompt = f"""
    Here is the user's question:
    {question}
    
    Here is the extracted answer from the dataset:
    {insight}
    
    Rephrase the answer into a user-friendly response.
    """
    print(f"Second Prompt Output: {prompt}") # <---
    return ask_llm(prompt)


# for running in the terminal
# def chatbot():
#     import pdb;pdb.set_trace()
#     print("Hi! I'm your friendly neighbourhood CHATBOT")
#     print("Type 'exit' to quit.\n")
#
#     sample_data = df.head(3).to_string()
#     print(f"Sample Data Output: {sample_data}") # <---
#
#     while True:
#         question = input("Fire away the question you want to ask: ")
#         if question.lower() in ["exit", "quit"]:
#             break
#
#         raw_code = generate_code_from_question(question, sample_data)
#         print("raw_code",raw_code)
#         code = clean_code(raw_code)
#         print(f"Generated Code: {code}") # <---
#
#         local_vars = {'df': df}
#         try:
#             # Execute the generated code and capture the result
#
#             exec(code, {}, local_vars)
#             result = local_vars.get("result", "Code executed successfully, check output printed by the code.")
#
#         except Exception as e:
#             print(" Error executing code:", e)
#             continue
#
#         # Send result back to LLaMA 3 for natural explanation
#         response = rephrase_answer(result, question)
#         print("\n Chatbot Answer:")
#         print(response)
#         print("-" * 50)
#
#
# if __name__ == "__main__":
#     chatbot()

#for running with proper ui
def end_process(question: str):
    sample_data = df.head(3).to_string()
    raw_code = generate_code_from_question(question, sample_data)
    code = clean_code(raw_code)

    local_vars = {'df': df}
    try:
        exec(code, {}, local_vars)
        result = local_vars.get("result", "Code executed, but no result found.")
        user_friendly= rephrase_answer(result, question)
        return user_friendly, None
    except Exception as e:
        return None, str(e)