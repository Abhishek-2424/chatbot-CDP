import json
from thefuzz import process

# Load the scraped data
with open("scraped_data.json", "r", encoding="utf-8") as f:
    CDP_DATA = json.load(f)

def get_relevant_answer(question):
    questions = list(CDP_DATA.keys())
    best_match, score = process.extractOne(question, questions)
    
    if score > 60:
        return CDP_DATA[best_match]  # Return the answer from the dataset
    else:
        return "Sorry, I couldn't find an answer to your question."
