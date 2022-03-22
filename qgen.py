from questiongenerator import QuestionGenerator
from questiongenerator import print_qa

def Qa_Gen(text):
    qg = QuestionGenerator()
    qa_list = qg.generate(
        text, 
        num_questions=5, 
        answer_style='multiple_choice'
    )
    return {'Questions': qa_list}