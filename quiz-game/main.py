from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for qus in question_data:
    ques = qus["text"]
    ans = qus["answer"]
    new_ques = Question(ques, ans)
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)

while quiz.should_countinue():
    quiz.next_question()

print(f"You complete it. Your score is {quiz.score}")