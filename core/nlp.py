from transformers import pipeline

class NLP:
    def __init__(self):
        # Load the pre-trained model for text classification (intent recognition)
        self.intent_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

        print("NLP module initialized with intent classification.")

    def classify_intent(self, text):
        # Define possible intents
        candidate_labels = ["get weather", "set a reminder", "play music", "check news", "system control"]

        # Use the intent classifier to predict the intent
        result = self.intent_classifier(text, candidate_labels)

        # Get the most likely intent
        intent = result['labels'][0]
        print(f"Identified intent: {intent}")

        return intent

# Test the setup
if __name__ == "__main__":
    nlp = NLP()
    test_text = "Can you tell me the weather?"
    nlp.classify_intent(test_text)

