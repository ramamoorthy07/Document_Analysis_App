from transformers import pipeline

# Explicitly specify the model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    """
    This function summarizes a given text using a pre-trained model from Hugging Face.
    :param text: The input text to be summarized.
    :return: The summarized text.
    """
    if len(text.split()) < 20:
        return "Text is too short to summarize."

    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']
