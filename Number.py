import streamlit as st
import random

# Text content
intro_text = (
    "In this game you choose a number between 1 and 1000.\n\n"
    "Your probability of winning is **0.1%**.\n\n"
    "Each time you try, the system generates a new random number."
)

random_thoughts = [
    "Probability doesn't guarantee outcomes, only chances.",
    "0.1% doesn't mean you'll win in exactly 1000 tries.It means you might never win.",
    "Programming is beautiful because logic always stays honest.Not for you by the way.",
    "Randomness is fair, but not kind.But who cares anyway.",
    "Sometimes losing teaches more than winning.Unless you're a looser.",
    "The reason I love programming is because I don't hate programming.",
]

# Page setup
st.set_page_config(page_title="0.1 Probability Game", layout="centered")

st.title("🎲 0.1% Probability Game")
st.write(intro_text)

st.divider()

# User input
user_number = st.number_input(
    "Choose a number between 1 and 1000",
    min_value=1,
    max_value=1000,
    step=1
)

if st.button("Try Your Luck"):
    system_number = random.randint(1, 1000)

    if user_number == system_number:
        st.success(f"🎉 You got lucky! The number was {system_number}")
    else:
        st.error(f"❌ Nope. The number was {system_number}")

    st.info(random.choice(random_thoughts))
