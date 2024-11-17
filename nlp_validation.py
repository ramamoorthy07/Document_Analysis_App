from transformers import pipeline

# Explicitly specify the model for zero-shot classification
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def validate_content(text):
    # Check if text is not empty
    if not text:
        return {"error": "No text provided for validation."}

    # Define some candidate labels
    candidate_labels = ["finance", "legal", "medical", "technology", "general"]

    try:
        # Ensure the classifier gets the correct input format
        result = classifier(text, candidate_labels)
        return result
    except ValueError as e:
        return {"error": str(e)}

