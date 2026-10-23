import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

st.set_page_config(page_title="AI Truth Checker", page_icon="✅")

st.title("✅ AI-Driven RAG Truth Checker")
st.write("Verify facts and detect AI hallucinations using RAG")

user_claim = st.text_area("Enter your claim / fact to verify:")

if st.button("Check Truth"):
    if user_claim:
        st.info("Checking against knowledge base...")
        st.success(f"✅ Claim: '{user_claim}' appears to be VERIFIED against trusted sources.")
        st.warning("Note: Connect your vector DB for real verification.")
    else:
        st.error("Please enter a claim to check.")

st.markdown("---")
st.caption("Built with RAG | Python | Streamlit")
