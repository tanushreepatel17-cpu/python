#ques gem using list tuple set

question = ("how many elements are in the periodic table?:",
" which animal leys the largest eggs?:",
"what is the most abundant gas in earth's atmosphere?:",
"how many bones are in the human body?:", 
"which element in the solar sytem is the hotest?:")

options = (("A. 116", "B. 108", "C. 104", "D. 100 "),
          ("A. whale", "B. panda", "C. ostrich", "D. elephant"),
          ("A. nitrogen", "B. oxygen", "C. carbon dioxide", "D. hydrogen"),
          ("A. 122", "B. 102", "C. 100", "D. 206"),
          ("A. mercury", "B. venus", "C. earth", "D. jupiter"))

answer = ("B", "C", "A", "D", "B")
guesses = []
score = 0
ques_num = 0

for question in question:
    print("----------------------------")
    print(question)

    for option in options[ques_num]:
        print(option)
        
    
    guess = input("enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answer[ques_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answer[ques_num]} is the correct answer")
    ques_num += 1

print("--------------------------------------")
print("               result                 ")
print("--------------------------------------")

print ("answer: ", end=" ")
for answer in answer: 
    print(answer, end=" ")
print()


print("guesses: ", end=" ")
for guess in guesses:
    print("guess", end=" ")
print()

score = int(score/ len(question) * 100)
print(f" your score is: {score}%")