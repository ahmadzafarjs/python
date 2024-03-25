from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print("""  sSSs_sSSs     .S       S.    .S   sdSSSSSSSbs  
 d%%SP~YS%%b   .SS       SS.  .SS   YSSSSSSSS%S  
d%S'     `S%b  S%S       S%S  S%S          S%S   
S%S       S%S  S%S       S%S  S%S         S&S    
S&S       S&S  S&S       S&S  S&S        S&S     
S&S       S&S  S&S       S&S  S&S        S&S     
S&S       S&S  S&S       S&S  S&S       S&S      
S&S       S&S  S&S       S&S  S&S      S*S       
S*b       d*S  S*b       d*S  S*S     S*S        
S*S.     .S*S  S*S.     .S*S  S*S   .s*S         
 SSSbs_sdSSSS   SSSbs_sdSSS   S*S   sY*SSSSSSSP  
  YSSP~YSSSSS    YSSP~YSSY    S*S  sY*SSSSSSSSP  
                              SP                 
                              Y                  
""")

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