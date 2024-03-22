class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def should_countinue(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current.question} (True/False)? ")
        self.check_answer(user_answer, current)

    def check_answer(self, check_answer, correct_answer):
        if check_answer.lower() == correct_answer.answer.lower():
            self.score += 1 
            print("Yes you got it.")
        else:
            print("That's wrong!")
        print(f"Correct answer is {correct_answer.answer}")
        print(f"Your score is {len(self.question_list)}/{self.score}\n")