import streamlit as st
import random

if 'word' not in st.session_state:
    words = ["python", "apple", "robot", "ocean", "music"]
    st.session_state.word = random.choice(words)
    st.session_state.guessed_letters = []
    st.session_state.attempts = 6

st.title("Hangman Game")

word = st.session_state.word
guessed_letters = st.session_state.guessed_letters
attempts = st.session_state.attempts

display = ""

for letter in word:
    if letter in guessed_letters:
        display += letter + " "
    else:
        display += "_ "

st.write("### Word:")
st.write(display)

guess = st.text_input("Enter a letter").lower()

if st.button("Guess"):
    if guess:
        if guess in guessed_letters:
            st.warning("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            st.success("Correct!")
        else:
            guessed_letters.append(guess)
            st.session_state.attempts -= 1
            st.error("Wrong guess!")

if "_" not in display:
    st.success(f"Congratulations! You guessed the word: {word}")

st.write(f"Attempts Left: {st.session_state.attempts}")

if st.session_state.attempts <= 0:
    st.error(f"Game Over! The word was: {word}")

if st.button("Restart Game"):
    words = ["python", "apple", "robot", "ocean", "music"]
    st.session_state.word = random.choice(words)
    st.session_state.guessed_letters = []
    st.session_state.attempts = 6
    st.rerun()
