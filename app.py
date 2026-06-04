import streamlit as st
from difflib import get_close_matches
from faq_data import faq_categories, flat_faq

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .stApp { background-color: #f0f4f8; }
    .main-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        color: white;
    }
    .main-header h1 { margin: 0; font-size: 2rem; }
    .main-header p  { margin: 0.4rem 0 0; opacity: 0.75; font-size: 1rem; }

    .chat-bubble-user {
        background: #0f3460;
        color: white;
        padding: 0.75rem 1.1rem;
        border-radius: 18px 18px 4px 18px;
        margin: 0.4rem 0;
        max-width: 80%;
        margin-left: auto;
        text-align: right;
        font-size: 0.95rem;
    }
    .chat-bubble-bot {
        background: white;
        color: #1a1a2e;
        padding: 0.75rem 1.1rem;
        border-radius: 18px 18px 18px 4px;
        margin: 0.4rem 0;
        max-width: 80%;
        border: 1px solid #e0e7ef;
        font-size: 0.95rem;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    .category-pill {
        display: inline-block;
        background: #e8f0fe;
        color: #0f3460;
        border-radius: 999px;
        padding: 0.3rem 0.9rem;
        font-size: 0.82rem;
        font-weight: 600;
        margin: 0.25rem;
        cursor: pointer;
        border: 1.5px solid #c3d4f7;
    }
    .faq-chip {
        background: white;
        border: 1px solid #d1dce8;
        border-radius: 10px;
        padding: 0.5rem 0.85rem;
        font-size: 0.85rem;
        color: #1a1a2e;
        cursor: pointer;
        margin: 0.2rem;
        display: inline-block;
        transition: background 0.2s;
    }
    .answer-box {
        background: #eaf6f0;
        border-left: 4px solid #27ae60;
        border-radius: 0 12px 12px 0;
        padding: 1rem 1.2rem;
        color: #145a32;
        font-size: 0.97rem;
        margin-top: 0.5rem;
    }
    .no-answer-box {
        background: #fff3cd;
        border-left: 4px solid #f39c12;
        border-radius: 0 12px 12px 0;
        padding: 1rem 1.2rem;
        color: #7d5a00;
        font-size: 0.97rem;
        margin-top: 0.5rem;
    }
    div[data-testid="stButton"] > button {
        background: #0f3460;
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.5rem 1.5rem;
        font-size: 0.95rem;
        transition: background 0.2s;
    }
    div[data-testid="stButton"] > button:hover { background: #16213e; }
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None
if "prefill_question" not in st.session_state:
    st.session_state.prefill_question = ""

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
  <h1>🤖 AI FAQ Chatbot</h1>
  <p>Ask college, technology, AI, or ECE-related questions — or browse by category below.</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📚 Browse Categories")
    st.markdown("Click a category to explore its questions:")
    st.markdown("---")
    for cat_name in faq_categories:
        if st.button(cat_name, key=f"sidebar_{cat_name}", use_container_width=True):
            st.session_state.selected_category = cat_name
    st.markdown("---")
    if st.session_state.history:
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.history = []
            st.rerun()
    st.markdown("---")
    st.caption(f"📖 {len(flat_faq)} questions across {len(faq_categories)} categories")
    st.caption("Built with Python + Streamlit")

# ── Main layout ───────────────────────────────────────────────────────────────
left_col, right_col = st.columns([3, 2], gap="large")

# ── LEFT: Chat area ───────────────────────────────────────────────────────────
with left_col:
    st.markdown("#### 💬 Ask a Question")

    default_val = st.session_state.prefill_question
    user_question = st.text_input(
        "Type your question:",
        value=default_val,
        placeholder="e.g. What is Machine Learning?",
        key="question_input",
        label_visibility="collapsed",
    )
    # Reset prefill after use
    st.session_state.prefill_question = ""

    col_ask, col_clear = st.columns([2, 1])
    with col_ask:
        ask_clicked = st.button("🔍 Get Answer", use_container_width=True)
    with col_clear:
        if st.button("✖ Clear", use_container_width=True):
            st.rerun()

    if ask_clicked and user_question.strip():
        q = user_question.strip()
        answer = None

        # 1. Exact match (case-insensitive)
        for question in flat_faq:
            if q.lower() == question.lower():
                answer = flat_faq[question]
                break

        # 2. Fuzzy match
        if answer is None:
            matches = get_close_matches(q, flat_faq.keys(), n=1, cutoff=0.4)
            if matches:
                answer = flat_faq[matches[0]]
            else:
                # 3. Keyword search fallback
                q_lower = q.lower()
                for question, ans in flat_faq.items():
                    if any(word in question.lower() for word in q_lower.split() if len(word) > 3):
                        answer = ans
                        break

        if answer is None:
            answer = "Sorry, I couldn't find an answer for that question. Try browsing categories on the right, or rephrase your question."
            st.markdown(f'<div class="no-answer-box">⚠️ {answer}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="answer-box">✅ {answer}</div>', unsafe_allow_html=True)

        st.session_state.history.append({"question": q, "answer": answer})

    # Chat history
    if st.session_state.history:
        st.markdown("---")
        st.markdown("#### 📜 Chat History")
        for chat in reversed(st.session_state.history):
            st.markdown(f'<div class="chat-bubble-user">🧑 {chat["question"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="chat-bubble-bot">🤖 {chat["answer"]}</div>', unsafe_allow_html=True)

# ── RIGHT: Category browser ───────────────────────────────────────────────────
with right_col:
    st.markdown("#### 📂 FAQ Categories")

    # Category selector buttons
    cols = st.columns(2)
    for i, cat_name in enumerate(faq_categories):
        with cols[i % 2]:
            if st.button(cat_name, key=f"main_{cat_name}", use_container_width=True):
                st.session_state.selected_category = cat_name

    # Show selected category questions
    if st.session_state.selected_category:
        cat = st.session_state.selected_category
        questions = list(faq_categories[cat].keys())
        st.markdown(f"---\n**{cat}** — click a question to auto-fill:")

        for q in questions:
            if st.button(f"❓ {q}", key=f"q_{q}", use_container_width=True):
                st.session_state.prefill_question = q
                st.rerun()
    else:
        st.markdown("---")
        st.info("👆 Select a category above to browse its questions.")

        # Quick-start suggestions
        st.markdown("**🌟 Popular Questions:**")
        popular = [
            "What is Machine Learning?",
            "How to apply for a scholarship?",
            "What is IoT?",
            "What are placement opportunities?",
            "What is ECE?",
            "What is ChatGPT?",
        ]
        for q in popular:
            if st.button(f"❓ {q}", key=f"pop_{q}", use_container_width=True):
                st.session_state.prefill_question = q
                st.rerun()