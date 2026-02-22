import streamlit as st

st.set_page_config(page_title="Delete Name Rage Game", page_icon="😈")

warnings = [
    "Are you sure you want to delete this name? (yes/no)",
    "Second check: still sure? (yes/no)",
    "Third check: no turning back... continue? (yes/no)",
    "Do you accept possible regret? (yes/no)",
    "Are you deleting with full confidence? (yes/no)",
    "Final warning before another final warning. Continue? (yes/no)",
    "Would your future self approve this? (yes/no)",
    "Do you promise this is not a typo? (yes/no)",
    "Are you emotionally ready to continue? (yes/no)",
    "Do you confirm this suspicious decision? (yes/no)",
    "Should the name protection shield be ignored? (yes/no)",
    "Do you insist on pressing forward? (yes/no)",
    "Is this your final-final decision? (yes/no)",
    "Still deleting? confirm again. (yes/no)",
    "No joke now, continue with deletion path? (yes/no)",
    "Would you like one more warning anyway? (yes/no)",
    "System asks politely: stop now? (yes/no)",
    "Do you reject the mercy option? (yes/no)",
    "Are you sure this is not a prank? (yes/no)",
    "Do you want to continue this warning marathon? (yes/no)",
    "Do you acknowledge this is getting ridiculous? (yes/no)",
    "Is your patience level still above zero? (yes/no)",
    "Are you prepared for even more prompts? (yes/no)",
    "Should we continue annoying you? (yes/no)",
    "Do you truly mean YES this time too? (yes/no)",
    "Can we record your stubbornness as legendary? (yes/no)",
    "Do you certify this deletion intent again? (yes/no)",
    "Are you willing to face the final hurdles? (yes/no)",
    "Penultimate warning: continue anyway? (yes/no)",
    "Last warning: delete after all this effort? (yes/no)",
]

if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.target_name = "ALEXANDER THE UNDELETABLE"
    st.session_state.deleted = False
    st.session_state.game_over = False
    st.session_state.total_warnings = len(warnings)
    st.session_state.step = 0
    st.session_state.awaiting_captcha = False
    st.session_state.feedback = "Type yes/no to continue. No easy button here."

st.title("Delete Name Frustration Game")
st.write("You must type `yes` or `no` every single round. No dedicated delete button.")
st.write(f"**Name on website:** {st.session_state.target_name}")
st.caption(
    f"Progress: {st.session_state.step}/{st.session_state.total_warnings} warnings accepted"
)

st.info(st.session_state.feedback)

if st.session_state.game_over:
    st.error("Game over. You typed NO, so deletion was canceled.")
    restart = st.text_input("Type `reset` to play again", key="restart_input_no")
    if restart.strip().lower() == "reset":
        st.session_state.target_name = "ALEXANDER THE UNDELETABLE"
        st.session_state.deleted = False
        st.session_state.game_over = False
        st.session_state.total_warnings = len(warnings)
        st.session_state.step = 0
        st.session_state.awaiting_captcha = False
        st.session_state.feedback = "Game reset. Start typing yes/no again."
        st.rerun()
    st.stop()

if st.session_state.deleted:
    st.success("After all that pain, the name is deleted.")
    restart = st.text_input("Type `reset` to play again", key="restart_input_yes")
    if restart.strip().lower() == "reset":
        st.session_state.target_name = "ALEXANDER THE UNDELETABLE"
        st.session_state.deleted = False
        st.session_state.game_over = False
        st.session_state.total_warnings = len(warnings)
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

prompt = warnings[st.session_state.step]
answer = st.text_input(prompt, key=f"ans_{st.session_state.step}")

if answer:
    value = answer.strip().lower()

    if value not in {"yes", "no"}:
        st.session_state.feedback = "Invalid input. Only type yes or no."
        st.rerun()

    if value == "no":
        st.session_state.game_over = True
        st.session_state.feedback = "You typed NO. Game stopped immediately."
        st.rerun()

    st.session_state.step += 1

    if st.session_state.step % 6 == 0 and st.session_state.step < st.session_state.total_warnings:
        st.session_state.awaiting_captcha = True
        st.session_state.feedback = "Nice try. Captcha checkpoint unlocked."
        st.rerun()

    if st.session_state.step >= st.session_state.total_warnings:
        st.session_state.target_name = "(deleted)"
        st.session_state.deleted = True
        st.session_state.feedback = "Unbelievable. You actually survived all 30 warnings."
        st.rerun()

    st.session_state.feedback = "Accepted. Next warning incoming."
    st.rerun()
