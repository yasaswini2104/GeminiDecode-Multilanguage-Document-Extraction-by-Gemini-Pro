# GeminiDecode: Multilanguage Document Extraction by Gemini Pro

**GeminiDecode** is a powerful document extraction solution that utilizes advanced natural language processing (NLP) and machine learning to process and categorize information from documents in multiple languages. Built with the Gemini Pro model, this tool is ideal for organizations handling diverse languages, supporting over 50 languages to streamline data extraction, enhance productivity, and improve decision-making.

---

## Table of Contents

- [Features](#features)
- [Scenarios of Use](#scenarios-of-use)
- [Technical Requirements](#technical-requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Technical Architecture](#technical-architecture)
- [Additional Resources](#additional-resources)
- [License](#license)

---

## Features

- **Multilanguage Support**: Extracts information from documents in over 50 languages.
- **Automated Data Processing**: Reduces manual work and enhances accuracy in data extraction.
- **Streamlined Workflow**: Integrates seamlessly into existing processes for legal, financial, and healthcare sectors.
- **Web-Based UI**: Accessible interface for easy document uploads and data viewing.

---

## Scenarios of Use

### 1. Legal Sector
Automatically processes multilingual legal documents such as contracts and affidavits, ensuring compliance with legal standards and reducing manual work.

### 2. Financial Institutions
Facilitates the extraction of financial information from documents in various languages, enhancing processes like loan approvals and financial analysis.

### 3. Healthcare Industry
Extracts critical patient information from multilingual medical records, improving patient care by providing quick access to essential data.

---

## Technical Requirements

To deploy and run **GeminiDecode**, ensure you have the following:

- **Python 3.7 or later**
- **Libraries**: See `requirements.txt` for full library requirements
  - `streamlit`
  - `streamlit_extras`
  - `google-generativeai`
  - `python-dotenv`
  - `PyPDF2`
  - `Pillow`
- **Google API Key** for accessing the Gemini Pro model

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yasaswini2104/GeminiDecode-Multilanguage-Document-Extraction-by-Gemini-Pro.git
   
2. **Install dependencies**: Install the necessary libraries listed in requirements.txt by running:
   ```bash
   pip install -r requirements.txt

---

## Configuration
1. Generate a Google API Key:
   
  * Visit the Gemini API Key page and sign in with your Google account.
  * Navigate to the Get an API Key option.
  * Click Create API Key and choose the relevant project.
  * Copy the generated API key, as you will need it for authentication.
2. Set up Environment Variables:
  * In the root directory of your project, create a file named .env.
  * Add your Google API key to the .env file as follows:
  ```bash
GOOGLE_API_KEY=your_generated_api_key
```
This step securely stores the API key, enabling the application to interact with the Gemini Pro model.

---

## Usage
1. Run the Application:
   Start the application by executing the following command:
   ```bash
   streamlit run app.py

2. Using the Interface:
  * Open the application in your web browser. By default, it runs at http://localhost:8501.
  * Upload documents in supported formats (e.g., PDF).
  * Select the document language and specify the document type if necessary.
  * View the extracted information in real-time as displayed on the interface.

## Technical Architecture
![image](https://github.com/user-attachments/assets/990ed5cc-800c-4e4c-8149-5fb5663edec7)

## Additional Resources

Here are some useful resources to understand the components and technologies used in **GeminiDecode**:

- [Natural Language Processing (NLP)](https://www.tutorialspoint.com/natural_language_processing/index.htm): An introduction to NLP, covering key concepts for language processing tasks.
- [Generative AI Overview](https://en.wikipedia.org/wiki/Generative_artificial_intelligence): Provides an overview of generative AI, its applications, and its significance.
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs/get-started/python): Official documentation for the Gemini API, including setup and usage guides.
- [Streamlit Documentation](https://docs.streamlit.io/): Streamlit documentation to help you build interactive web applications with Python.



## License
This project is licensed under the MIT License - see the LICENSE file for details.

Streamlit Deployment Link - https://geminidecodemultilanguage.streamlit.app/
