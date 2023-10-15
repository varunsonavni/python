from art import question_data

from question import Question

question_bank = []

for question in question_data:
    question_data = question["question"]
    question_ans = question["correct_answer"]
    new_question = Question(question_data, question_ans)
    # print(new_question.text)
    question_bank.append(new_question)

# print(question_bank[0].text)



class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0 
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer.lower()
        # print(current_answer)
        answer = input(f"Q.{self.question_number}: {current_question} (True/False): ").lower()
        # print(answer)
        self.question_number += 1
        if current_answer == answer:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {current_answer}")
            print(f"Your current score is: {self.score}/{self.question_number}")

        else:
            print("That's wrong.")
            print(f"The correct answer was: {current_answer}")
            print(f"Your current score is: {self.score}/{self.question_number}")

        

    def still_has_questions(self):
        """return True if there are questions remaining"""
        # print(len(self.question_list))
        # print(self.question_number)
        if len(self.question_list) > self.question_number:
            return True
        else:
            print("DD")
            return False

quiz = QuizBrain(question_bank)

                                                                                                                 
while quiz.still_has_questions():    
    quiz.next_question()


