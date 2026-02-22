import random
import streamlit as st

st.set_page_config(page_title="Delete Name Rage Game", page_icon="😈")

if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.target_name = "ALEXANDER THE UNDELETABLE"
    st.session_state.deleted = False
    st.session_state.total_warnings = random.randint(20, 50)
    st.session_state.step = 0
    st.session_state.awaiting_captcha = False
    st.session_state.feedback = "Type yes/no to continue. No easy button here."

warnings = [
    "Are you sure you want to delete that name? (yes/no)",
    "Again, are you 100% sure? (yes/no)",
    "Really really sure? (yes/no)",
    "This might anger the name spirits. Continue? (yes/no)",
    "Last warning before next warning. Continue? (yes/no)",
    "Do you still want to delete it? (yes/no)",
    "Oh really? still yes? (yes/no)",
]

st.title("Delete Name Frustration Game")
st.write("You must type `yes` or `no` every single round. No dedicated delete button.")
st.write(f"**Name on website:** {st.session_state.target_name}")
st.caption(
    f"Progress: {st.session_state.step}/{st.session_state.total_warnings} warnings accepted"
)

st.info(st.session_state.feedback)

if st.session_state.deleted:
    st.success("After all that pain, the name is deleted.")
    restart = st.text_input("Type `reset` to play again", key="restart_input")
    if restart.strip().lower() == "reset":
        st.session_state.target_name = "ALEXANDER THE UNDELETABLE"
        st.session_state.deleted = False
        st.session_state.total_warnings = random.randint(20, 50)
        st.session_state.step = 0
        st.session_state.awaiting_captcha = False
        st.session_state.feedback = "Game reset. Start typing yes/no again."
        st.rerun()
    st.stop()

if st.session_state.awaiting_captcha:
    cap = st.text_input("Solve captcha: what is 3 + 5?", key=f"cap_{st.session_state.step}")
    if cap:
        if cap.strip() == "8":
            st.session_state.awaiting_captcha = False
            st.session_state.feedback = "A robot can easily do that. Continue suffering."
            st.rerun()
        else:
            st.session_state.feedback = "Wrong captcha. Type 8."
            st.rerun()
    st.stop()

prompt = warnings[st.session_state.step % len(warnings)]
answer = st.text_input(prompt, key=f"ans_{st.session_state.step}")

if answer:
    value = answer.strip().lower()

    if value not in {"yes", "no"}:
        st.session_state.feedback = "Invalid input. Only type yes or no."
        st.rerun()

    if value == "no":
        st.session_state.feedback = "You typed no. Deletion canceled. Type yes if you dare."
        st.rerun()

    st.session_state.step += 1

    if st.session_state.step % 6 == 0:
        st.session_state.awaiting_captcha = True
        st.session_state.feedback = "Nice try. Captcha checkpoint unlocked."
        st.rerun()

    if st.session_state.step >= st.session_state.total_warnings:
        st.session_state.target_name = "(deleted)"
        st.session_state.deleted = True
        st.session_state.feedback = "Unbelievable. You actually survived all warnings."
        st.rerun()

    st.session_state.feedback = "Accepted. Next warning incoming."
    st.rerun()
