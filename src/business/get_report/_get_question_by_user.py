# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
def get_question_by_user(id_user, question_list):
    user_questions = {}

    for quest in question_list:
        id_user_ques = quest[1]

        count_quest = quest[2]

        question = quest[3]

        answer = quest[4]

        if str(id_user) != id_user_ques:
            continue

        user_questions[count_quest] = {
            'question': question,
            'answer': answer
        }

    return user_questions
