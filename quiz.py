import csv


class Question:
    def __init__(self, question_text: str, possible_answers: list):
        self.question_text = question_text
        self.possible_answers = possible_answers


class Answer:
    def __init__(self, answer_text: str, correct: bool = False):
        self.answer_text = answer_text
        self.correct = correct


class Quiz:
    def __init__(self, title: str, questions: list = []):
        self.title = title
        self.questions = questions

    def export_to_csv(self, file_path: str):
        with open(file_path, "w", newline="") as csvfile:
            fieldnames = [
                "Question",
                "Answer 1",
                "Answer 2",
                "Answer 3",
                "Answer 4",
                "Answer 5",
                "Answer 6",
                "Correct Answer",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for question in self.questions:
                writer.writerow(self.get_question_as_dict(question))

    def get_question_as_dict(self, question: Question):
        q_row = {}
        q_row["Question"] = question.question_text
        correct_answer = []
        for i, answer in enumerate(question.possible_answers):
            answer_header = f"Answer {str(i).zfill(2) + 1}"
            q_row[answer_header] = answer.answer_text
            if answer.correct:
                correct_answer.append(answer_header)
        q_row["Correct Answer"] = ", ".join(correct_answer)
        return q_row
