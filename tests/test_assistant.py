from core.assistant import PersonalAssistant
from core.nlp import NLP

def test_assistant():
    assistant = PersonalAssistant()
    assert assistant is not None
    print("Basic setup test passed.")

def test_nlp():
    nlp = NLP()
    result = nlp.process_text("Test NLP processing")
    assert result is not None
    print("NLP test passed.")

if __name__ == "__main__":
    test_assistant()
    test_nlp()

