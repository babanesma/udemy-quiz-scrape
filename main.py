from quiz import Quiz, Question, Answer
from lxml import html
from lxml.cssselect import CSSSelector


def import_dumped_quiz_html(file_path):
    f = open(file_path)
    tree = html.parse(f)
    return tree


def parse_questions(file_path):
    html_file = import_dumped_quiz_html(file_path)
    questions = []
    question_form_selector = CSSSelector("div.detailed-result-panel--panel-row--2aE8z")
    for question_group in question_form_selector(html_file):
        # fetch question text
        question_selector = CSSSelector("div#question-prompt")
        question_text = None
        for question_div in question_selector(question_group):
            question_text = question_div.text_content()
        if question_text is None:
            continue

        # fetch answers
        answers = []
        answer_selector = CSSSelector("li.mc-quiz-question--answer--eCdL3")
        for answer_div in answer_selector(question_group):
            answer_text = answer_div.text_content()
            correct = "(Correct)" in answer_text
            answer = Answer(
                answer_text.replace("(Correct)", "").strip(),
                correct
            )
            answers.append(answer)

        # append question to list of questions
        question = Question(question_text, answers)
        questions.append(question)

    return questions


if __name__ == "__main__":
    questions = parse_questions(
        "exam practices/Practice Exams _ AWS Certified Cloud Practitioner CLF-C01_02 _ Udemy.html"
    )
    quiz = Quiz("AWS Certified Cloud Practitioner CLF-C01_02", questions)

    
