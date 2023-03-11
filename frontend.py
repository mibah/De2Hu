import streamlit as st
import random
import json

SCORE_FILE = "scores.json"
QUESTION_FILE = "hungarian_questions.json"


def get_question(difficulty, questions):
    selected_questions = [q for q in questions if q["difficulty"] == difficulty]
    question = random.choice(selected_questions)
    return question

def display_question(difficulty, questions):
    question = get_question(difficulty, questions)
    st.write(question["question"])
    options = question["answers"]
    correct_answer = question["correct_answer"]
    random.shuffle(options)

    # Display radio buttons for the answer options
    user_input = st.radio("Wähle deine Antwort:", options)

    if user_input:
        if user_input == correct_answer:
            return True
        else:
            return False

def main():
    st.set_page_config(page_title="Hungarian Quiz", page_icon="🧐")
    st.title("Hungarian Quiz")
    st.write("Teste dein Ungarisch Wissen!")

    # Initialize the score
    score = {"right": 0, "wrong": 0}

    # Check if the score is already saved in session state
    if 'score' in st.session_state:
        score = st.session_state.score

    if 'ask' not in st.session_state:
        st.session_state.ask = True

    # Display the current score
    st.write("Punkte: {} richtig, {} falsch".format(score["right"], score["wrong"]))

    # Define the available difficulty levels
    difficulty_levels = ["leicht", "mittel", "schwer"]

    #load questions
    with open(QUESTION_FILE, "r") as f:
        questions = json.load(f)

    if "submit_button2" in st.session_state:
        submit_button2 = True
    else:
        submit_button2 = False

    # Form 1: Select difficulty level
    with st.form(key="difficulty_form"):
        st.write("Wähle eine Schwierigkeitsstufe")
        difficulty = st.selectbox("Schwierigkeit", difficulty_levels)
        st.form_submit_button(label="Quiz starten")

    # Form 2: Display question and get user's answer
    # Load the questions from file
    with st.form(key="question_form"):
        if st.session_state.ask == True:
            st.write("Frage")
            question = get_question(difficulty, questions)
            st.write(question["question"])
            options = question["answers"]
            correct_answer = question["correct_answer"]
            random.shuffle(options)

            #store old state
            st.session_state.question = question
            st.session_state.options = options
            st.session_state.correct_answer = correct_answer
        else:
            st.write("Frage")
            question = st.session_state.question
            st.write(question["question"])
            options = st.session_state.options
            correct_answer = st.session_state.correct_answer

        # Display radio buttons for the answer options
        answer = st.radio("Wähle deine Antwort:", options)

        submit_button2 = st.form_submit_button(label="Prüfe")
        st.session_state.ask = False
        st.session_state.submit_button2 = submit_button2

    # Update the score based on the user's answer
    if submit_button2:
        if correct_answer == answer:
            st.write("Correct!")
            print("korrekt")
            score["right"] += 1
        else:
            st.write("Wrong!")
            print("falsch")
            #st.write("Wrong! The correct answer is: " + question["correct_answer"])
            score["wrong"] += 1
        # Save the updated score in session state
        del st.session_state["submit_button2"]
        st.session_state.score = score
        st.session_state.ask = True

if __name__ == "__main__":
    main()
