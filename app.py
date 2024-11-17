import streamlit as st
from ocr import extract_text_from_pdf
from nlp_validation import validate_content
from embeddings import generate_embeddings
from report_generation import generate_pdf_report

st.title("AI Document Analysis Tool")
st.markdown("Upload a scanned PDF to extract text, validate content, generate embeddings, and get a structured PDF report.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    # Extract text from the uploaded PDF
    with st.spinner("Extracting text from PDF..."):
        extracted_text = extract_text_from_pdf(uploaded_file)
        st.success("Text extraction completed.")
        st.text_area("Extracted Text", extracted_text, height=200)

    # Validate content using NLP
    with st.spinner("Validating content..."):
        validation_result = validate_content(extracted_text)
        st.success("Content validation completed.")
        st.json(validation_result)

    # Generate embeddings
    with st.spinner("Generating embeddings..."):
        embeddings = generate_embeddings(extracted_text)
        st.success("Embeddings generated.")
        st.write(f"Embedding Vector (first 10 elements): {embeddings[:10]}")

    # Generate PDF report
    with st.spinner("Generating report..."):
        pdf_report = generate_pdf_report(extracted_text, validation_result, embeddings, "document_report.pdf")
        st.success("PDF report generated.")

    # Provide download button for the PDF report
    with open(pdf_report, "rb") as f:
        st.download_button("Download PDF Report", f, file_name="document_report.pdf", mime="application/pdf")
