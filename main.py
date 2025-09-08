from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface

question_bank = []

for i in question_data:
    queobject = Question(i["question"], i["correct_answer"])
    question_bank.append(queobject)


quiz = QuizBrain(question_bank)

quiz_interface = QuizInterface()


#while quiz.still_has_questions():
   # quiz.next_question()


print("Congrats. You have completed the quiz")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
















