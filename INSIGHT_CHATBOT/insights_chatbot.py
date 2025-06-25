from langchain_community.llms import ollama
from langchain_community.llms.ollama import Ollama

from insights_model import get_summary_insights
from sales_insights import get_regional_trends, get_seasonal_trends, get_churn_percentage
from langchain.prompts import  PromptTemplate

llm = Ollama(model="llama3")

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a customer analytics expert. Use only the data in the context below to answer the question.

Context:
{context}

Question:
{question}

Start your answer directly. Be clear and precise.
    """
)

def format_trend(trend_data, label):
    result = f"\n{label}:\n"
    for entry in trend_data:
        result += " - "+", ".join(f"{k}: {round(v, 2) if isinstance(v, float) else v}" for k, v in entry.items()) + "\n"
    return result
def query_chatbot(question):
    summary_insights= get_summary_insights()
    seasonal= get_seasonal_trends()
    regional= get_regional_trends()
    churn_percent= get_churn_percentage()

    context = "Overall Insights:\n"
    context += "\n".join([f"{k.replace('_', ' ').title()}:{v}" for k, v in summary_insights.items()])
    context += format_trend(seasonal, "Seasonal Sales Trend")
    context += format_trend(regional, "Reginal Sales Trend")
    context += f"\nChurn Rate: {churn_percent}%\n"

    prompt = prompt_template.format(context=context, question=question)
    return llm.invoke(prompt)

if __name__ == "__main__":
    while True:
        user_question = input("\nAsk a question (or type 'exit'): ")
        if user_question.lower() in ["exit", "quit"]:
            break
        answer = query_chatbot(user_question)
        print("\n Chatbot: ")
        print(answer)
