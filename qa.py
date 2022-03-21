import torch
import wikipedia
from transformers import AutoTokenizer, AutoModelForQuestionAnswering


def wiki(keyword):
    Error = None
    try:
        page_content = wikipedia.page(keyword)
        Summary = page_content.summary
        wikiContent = '.'.join(Summary.split('\n'))
        return wikiContent
    except Exception as e:
        Error = 1
        return "Sorry, The provided keyword may be invalid or insufficient."
    finally:
        if Error != None:
            pass
        else:
            print("Context Scrapped and Analyzed")

def qa_gen(summaryContent, question):
    PATH = "./Models/bert-large-uncased-whole-word-masking-squad2"
    tokenizer = AutoTokenizer.from_pretrained(PATH)
    model = AutoModelForQuestionAnswering.from_pretrained(PATH)
    inputs = tokenizer.encode_plus(
        question, summaryContent, return_tensors="pt")
    answer_start_scores, answer_end_scores = model(**inputs, return_dict=False)
    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1
    ansGenerated = tokenizer.convert_tokens_to_string(
        tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end]))
    return ansGenerated

def show_suggestion(keyword):
    suggestions=wikipedia.search(keyword, results=10, suggestion=True)
    if suggestions[0]==[]:
        return "Sorry, The provided keyword may be invalid Check for spelling mistakes."
    return suggestions[0]
