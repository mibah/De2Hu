import streamlit as st
import random
import json

SCORE_FILE = "scores.json"
QUESTION_FILE = "hungarian_questions.json"

def update_score_text(score):
    st.write("Score: {} right, {} wrong".format(score["right"], score["wrong"]))

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
    user_input = st.radio("Select your answer:", options)

    if user_input:
        if user_input == correct_answer:
            st.write("Correct!")
            return True
        else:
            st.write("Wrong! The correct answer is: " + question["correct_answer"])
            return False

def main():
    st.set_page_config(page_title="Hungarian Quiz", page_icon="🧐")
    st.title("Hungarian Quiz")
    st.write("Test your Hungarian knowledge!")

    # Define the available difficulty levels
    difficulty_levels = ["leicht", "mittel", "schwer"]

    # Get the selected difficulty from the user
    difficulty = st.selectbox("Select difficulty", difficulty_levels, index=0, key="difficulty")

    # Load the questions from file
    with open(QUESTION_FILE, "r") as f:
        questions = json.load(f)

    # Initialize the score
    score = {"right": 0, "wrong": 0}

    # Check if the score is already saved in session state
    if 'score' in st.session_state:
        score = st.session_state.score

    # Display the current score
    update_score_text(score)

    # Check if the user has started the quiz
    if st.button("Start"):
        # Display a question and get the user's answer
        answer = display_question(difficulty, questions)
        # Update the score based on the user's answer
        if answer is not None:
            if answer:
                score["right"] += 1
            else:
                score["wrong"] += 1

            # Save the updated score in session state
            st.session_state.score = score

            # Display the current score
            update_score_text(score)

            # Clear the question from the screen
            st.empty()

if __name__ == "__main__":
    main()







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
    user_input = st.radio("Select your answer:", options)

    if user_input:
        if user_input == correct_answer:
            return True
        else:
            return False

def main():
    st.set_page_config(page_title="Hungarian Quiz", page_icon="🧐")
    st.title("Hungarian Quiz")
    st.write("Test your Hungarian knowledge!")

    # Initialize the score
    score = {"right": 0, "wrong": 0}

    # Check if the score is already saved in session state
    if 'score' in st.session_state:
        score = st.session_state.score

    # Display the current score
    st.write("Score: {} right, {} wrong".format(score["right"], score["wrong"]))

    # Define the available difficulty levels
    difficulty_levels = ["leicht", "mittel", "schwer"]

    # Form 1: Select difficulty level
    with st.form(key="difficulty_form"):
        st.write("Select difficulty level")
        difficulty = st.selectbox("Difficulty", difficulty_levels)
        submit_button1 = st.form_submit_button(label="Start quiz")

    # Load the questions from file
    with open(QUESTION_FILE, "r") as f:
        questions = json.load(f)

    # Form 2: Display question and get user's answer
    if submit_button1:
        with st.form(key="question_form"):
            st.write("Question")
            answer = display_question(difficulty, questions)
            st.session_state.answer = answer
            submit_button2 = st.form_submit_button(label="Next question")

    # Update the score based on the user's answer
    if st.session_state.answer is not None and submit_button2:
        if answer:
            st.write("Correct!")
            print("correct")
            score["right"] += 1
        else:
            st.write("Wrong!")
            print("wrong")
            #st.write("Wrong! The correct answer is: " + question["correct_answer"])
            score["wrong"] += 1

        # Save the updated score in session state
        st.session_state.score = score

        # Display the current score
        st.write("Score: {} right, {} wrong".format(score["right"], score["wrong"]))

        # Clear the question from the screen
        st.empty()

    st.session_state.answer = None
if __name__ == "__main__":
    main()





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
    user_input = st.radio("Select your answer:", options)

    if user_input:
        if user_input == correct_answer:
            return True
        else:
            return False

def main():
    st.set_page_config(page_title="Hungarian Quiz", page_icon="🧐")
    st.title("Hungarian Quiz")
    st.write("Test your Hungarian knowledge!")

    # Initialize the score
    score = {"right": 0, "wrong": 0}

    # Check if the score is already saved in session state
    if 'score' in st.session_state:
        score = st.session_state.score

    # Display the current score
    st.write("Score: {} right, {} wrong".format(score["right"], score["wrong"]))

    # Define the available difficulty levels
    difficulty_levels = ["leicht", "mittel", "schwer"]

    if "submit_button2" in st.session_state:
        submit_button2 = True
    else:
        submit_button2 = False

    # Form 1: Select difficulty level
    with st.form(key="difficulty_form"):
        st.write("Select difficulty level")
        difficulty = st.selectbox("Difficulty", difficulty_levels)
        submit_button1 = st.form_submit_button(label="Start quiz")

    # Form 2: Display question and get user's answer
    if submit_button1:
        # Load the questions from file
        with open(QUESTION_FILE, "r") as f:
            questions = json.load(f)
        with st.form(key="question_form"):
            st.write("Question")
            question = get_question(difficulty, questions)
            st.write(question["question"])
            options = question["answers"]
            correct_answer = question["correct_answer"]
            random.shuffle(options)

            # Display radio buttons for the answer options
            answer = st.radio("Select your answer:", options)

            submit_button2 = st.form_submit_button(label="Next question")
            st.session_state.submit_button2 = submit_button2

    # Update the score based on the user's answer
    if submit_button2:
        if answer == correct_answer:
            st.write("Correct!")
            print("correct")
            score["right"] += 1
            del st.session_state["submit_button2"]
        else:
            st.write("Wrong!")
            print("wrong")
            #st.write("Wrong! The correct answer is: " + question["correct_answer"])
            score["wrong"] += 1
            del st.session_state["submit_button2"]
        # Save the updated score in session state
        st.session_state.score = score

if __name__ == "__main__":
    main()
