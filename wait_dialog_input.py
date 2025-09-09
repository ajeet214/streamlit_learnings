import streamlit as st

RESULT_KEY = "dfnfrelgtggrighrtiugivvfs"  # where we'll store the final value


@st.dialog("Enter Your Input")  # <-- no key= here
def get_user_input_popup(prompt_text: str,
                         *,
                         result_key: str = RESULT_KEY,
                         text_key: str = "__popup_text"):
    with st.form("popup_form"):
        st.write(prompt_text)
        user_input = st.text_input("Your response:", key=text_key, placeholder="Type here…")
        c1, c2 = st.columns(2)
        submit = c1.form_submit_button("Submit", type="primary")
        cancel = c2.form_submit_button("Cancel")

        if submit:
            if user_input.strip():
                st.session_state[result_key] = user_input.strip()
                st.rerun()  # close dialog + continue page
            else:
                st.error("Please enter some text!")
        if cancel:
            st.session_state[result_key] = None
            st.rerun()


st.title("Demo: wait for dialog input without re-running everything while typing")

# If we don't have a result yet, open dialog and pause the page:
if RESULT_KEY not in st.session_state:
    get_user_input_popup("Need more info:")
    st.stop()  # freeze the rest of the page until dialog submits

# From here down, you *have* the result:
response = st.session_state[RESULT_KEY]
st.success(f"Dialog response: {response!r}")
