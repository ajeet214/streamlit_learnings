import streamlit as st
import os

# === Constants ===
SUGGESTION_FILE = "Suggestion.txt"

# === Helper Functions ===
@st.cache_data
def load_suggestions(file_path: str):
    """Load suggestions from a text file if it exists."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    else:
        return None

# === Load Data ===
Suggestions = load_suggestions(SUGGESTION_FILE)

# === Streamlit UI ===
st.title("📊 Sales AI Assistant")

tab1, tab2 = st.tabs(["📁 Data", "💬 Chat History"])

with tab1:
    st.subheader("Ask Questions About Your Data")

    if Suggestions:
        query = st.selectbox(
            "💡 Choose a suggested question:",
            options=Suggestions,
            index=0,
            placeholder="Example: What is the average value in x"
        )
        st.success(f"🔍 You selected: {query}")
    else:
        st.error(f"❌ Suggestion file not found at: `{SUGGESTION_FILE}` or is empty.")
