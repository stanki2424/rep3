import streamlit as st

st.title("Мини формуляр")

questions = [
    ("Коя е столицата на България?", "София"),
    ("Колко континента има на Земята?", "7"),
    ("Коя е най-дългата река в света?", "Нил"),
    ("Кой е авторът на 'Под игото'?", "Иван Вазов"),
    ("Колко е 5 + 7?", "12")
]

user_answers = []

for i, (question, _) in enumerate(questions):
    answer = st.text_input(question, key=f"q{i}")
    user_answers.append(answer)

if st.button("Провери"):
    score = 0
    for i, (_, correct_answer) in enumerate(questions):
        if user_answers[i].strip().lower() == correct_answer.lower():
            score += 1

    st.info(f"Верни отговори: {score} от {len(questions)}")

    if score == len(questions):
        st.success(" Всички отговори са верни!")
    else:
        st.warning(" Има грешни отговори. Опитай пак!")
