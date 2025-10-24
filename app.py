
import streamlit as st
from string_utils import *

st.set_page_config(layout="wide", page_title="String Length Counters", page_icon="📊")

st.title("📊 String Statistics Dashboard")

st.markdown("""
    <style>
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Apply RTL to user-entered text only */
    textarea {
        direction: rtl;
        text-align: right;
        unicode-bidi: plaintext;
        font-family: "Cairo", "Amiri", sans-serif;
    }

    /* Keep placeholder LTR and left-aligned */
    textarea::placeholder {
        direction: ltr !important;
        text-align: left !important;
    }
    </style>
    """, unsafe_allow_html=True)

text = st.text_area(
    "Text to analyze:",
    "", 
    height=500,
    max_chars=None,
    label_visibility="visible",
    placeholder="Type or paste your text here...",
)

char_count, word_count, parag_count = get_string_length_counts(text)

token_count = count_string_tokens(text)

a, b, d, e = st.columns(4)

a.metric("Number of Words", f"{word_count:,}", border=True)
b.metric("Number of Tokens", f"{token_count:,}", border=True)
d.metric("Number of Characters", f"{char_count:,}", border=True)
e.metric("Number of Paragraphs", f"{parag_count:,}", border=True)
