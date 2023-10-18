question_data = [
    {"text": "Operační systém Linux byl založen Linusem Torvaldem", "answer": "True"},
    {"text": "HTML jazyk je také nazýván značkovacím jazykem", "answer": "True"},
    {"text": "JavaScript patří mezi frontendové jazyky", "answer": "True"},
    {"text": "Je Slunce největší planetou ve sluneční soustavě?", "answer": "False"},
    {"text": "Byla první lidská mise na Měsíc úspěšná?", "answer": "True"},
    {"text": "Byl Mozart slavným německým hudebním skladatelem?", "answer": "False"},
    {"text": "Byl Apple založen Stevem Jobsem?", "answer": "True"},
    {"text": "Je voda na Zemi nejhojnější chemickou sloučeninou?", "answer": "True"},
]

class QuizBrain:

    def __init__(self, q_list, a_list):
        self.score = 0
        self.question_number = 0
        self.question_li = q_list
        self.answer_li = a_list
    def next_question(self):
        current_question = self.question_li[self.question_number]
        current_answer = self.answer_li[self.question_number]
        self.question_number+=1
        
        
        choice = input(f"Otázka č. {self.question_number}:\n{current_question} (True/False)\n")
        if choice == current_answer:
            print("Správně")
            print("Jdeme dále")
            self.score += 1
        else:
            print("Špatně")
        print(f"Vaše skóre je {self.score} / {self.question_number}")
    def has_question(self):
        if self.question_number < len(self.question_li):
            return True
        else:
            return False

question_list = []
answer_list = []
for one_question in question_data:
    
    question_t = one_question["text"]
    question_a = one_question["answer"]
    question_list.append(question_t)
    answer_list.append(question_a)
    
quiz = QuizBrain(question_list, answer_list)
while quiz.has_question() == True:
    quiz.next_question()

    
