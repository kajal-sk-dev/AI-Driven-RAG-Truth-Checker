import os
from dotenv import load_dotenv

load_dotenv()

def check_truth(claim: str, knowledge_base: str = "") -> dict:
    """
    Simple Truth Checker logic
    You can integrate ChromaDB + Embeddings here later
    """
    # Dummy scoring for now
    result = {
        "claim": claim,
        "status": "Verified" if len(claim) > 10 else "Needs Review",
        "confidence": "85%",
        "source": "RAG Knowledge Base"
    }
    return result

if __name__ == "__main__":
    test = "The Earth revolves around the Sun"
    print(check_truth(test))
