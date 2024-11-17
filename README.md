# Document Analysis App 📄🔍

### Automate Document Analysis with AI-powered OCR and NLP Solutions

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

The **Document Analysis App** is an AI-powered solution designed to automate the process of extracting, validating, and transforming content from scanned PDF documents into structured, actionable outputs. Leveraging Optical Character Recognition (OCR), Natural Language Processing (NLP), and document processing tools, this application provides a streamlined way to analyze and generate reports from unstructured data.

### Key Use Cases:
- Extracting text from scanned PDFs using OCR.
- Validating content accuracy with NLP models (e.g., GPT, BERT).
- Generating vector embeddings for advanced content analysis.
- Automated report generation in structured formats (PDF, JSON, etc.).

## Features

- **OCR Text Extraction**: Leverage OCR tools like Tesseract to extract text from scanned PDFs.
- **NLP Content Validation**: Use NLP models for validating the content against predefined criteria.
- **Vector Embedding Analysis**: Generate and analyze embeddings for advanced document classification.
- **Automated Report Generation**: Generate structured reports summarizing findings, including gap analysis.
- **Interactive Web Interface**: User-friendly interface built with Streamlit for ease of use.

## Tech Stack

- **Programming Language**: Python 3.11
- **Libraries**: 
  - OCR: `Tesseract`, `EasyOCR`
  - NLP: `Transformers`, `torch`, `sentence-transformers`
  - Document Processing: `PyPDF2`, `PDFplumber`, `ReportLab`
  - Frontend: `Streamlit`
- **Machine Learning**: `PyTorch`, `Hugging Face Transformers`
- **Deployment**: Local deployment with `venv`

## Demo
[![Document Analysis App Demo](https://img.shields.io/badge/Streamlit-Demo-brightgreen)](https://your-demo-link.com)

## Installation

### Prerequisites
- **Python 3.11**
- **Git**

### Step-by-Step Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Document_Analysis_App.git
   cd Document_Analysis_App
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Download OCR and NLP Models**:
   - Ensure you have Tesseract installed and set up (for Windows users, add Tesseract to your PATH).
   - Download pre-trained models (e.g., `facebook/bart-large-mnli`) using Hugging Face:
     ```python
     from transformers import pipeline
     classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
     ```

6. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

7. **Access the Web Interface**:
   - Open your browser and go to: [http://localhost:8501](http://localhost:8501)

## Usage

1. **Upload Your Document**:
   - Use the "Upload" button to upload a scanned PDF document.

2. **Extract and Analyze**:
   - The app will automatically extract text, validate content, and generate structured outputs.

3. **Download Reports**:
   - Download the generated reports in PDF format.

## Project Structure

```
Document_Analysis_App/
├── app.py                    # Streamlit frontend application
├── nlp_validation.py         # NLP validation logic
├── ocr_extraction.py         # OCR extraction logic
├── requirements.txt          # Python dependencies
├── report_generator.py       # PDF report generation using ReportLab
├── sample_documents/         # Sample PDFs for testing
├── utils.py                  # Utility functions
└── README.md                 # Project documentation
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [PyTorch](https://pytorch.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
