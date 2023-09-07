class Question():
    def __init__(self, question_text: str, possible_answers: list):
        self.question_text = question_text
        self.possible_answers = possible_answers


class Answer():
    def __init__(self, answer_text: str, correct: bool = False):
        self.answer_text = answer_text
        self.correct = correct


class Quiz():
    def __init__(self, title: str, questions: list = []):
        self.title = title
        self.questions = questions
