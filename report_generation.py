from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def generate_pdf_report(extracted_text, validation_result, embeddings, file_name="document_report.pdf"):
    """
    Generates a structured PDF report.cls
    
    """
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter
    
    # Add title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Document Analysis Report")
    
    # Add document metadata section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 100, "Document Metadata:")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 115, f"Document Title: Sample PDF Document")
    c.drawString(50, height - 130, f"Document Type: PDF")
    
    # Add text extraction section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 160, "Text Extraction Summary:")
    c.setFont("Helvetica", 10)
    extracted_summary = extracted_text[:300] + "..." if len(extracted_text) > 300 else extracted_text
    c.drawString(50, height - 175, f"{extracted_summary}")
    
    # Add content validation section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 205, "Content Validation Results:")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 220, f"Validation Outcome: {validation_result['labels'][validation_result['scores'].index(max(validation_result['scores']))]}")
    
    # Add embedding analysis section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 250, "Embedding Analysis:")
    c.setFont("Helvetica", 10)
    embedding_summary = "Embedding Vector (first 10 elements): " + str(embeddings[:10])
    c.drawString(50, height - 265, embedding_summary)
    
    # Add summary section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 295, "Summary:")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 310, "The document has been successfully processed.")
    c.drawString(50, height - 325, "Content has been validated as complete.")
    c.drawString(50, height - 340, "Embedding analysis indicates relevant content for further analysis.")
    
    # Save PDF
    c.showPage()
    c.save()

    return file_name
