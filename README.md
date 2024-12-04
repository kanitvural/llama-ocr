
# LLama3.2-OCR

This project leverages Llama 3.2 vision and Streamlit to create a 100% locally running OCR app.

## Installation and setup

**Setup Ollama**:
   ```bash
   # setup ollama on linux 
   curl -fsSL https://ollama.com/install.sh | sh
   # pull llama 3.2 vision model
   ollama run llama3.2-vision 
   ```


**Install Dependencies**:
   Ensure you have Python 3.11 or later installed.
   ```bash
   pip install streamlit ollama
   ```

---



# LLama3.2-OCR

LLama3.2-OCR is a locally running OCR (Optical Character Recognition) application built with the Llama 3.2 Vision model and Streamlit. This app extracts structured text from images and presents it in a clean, Markdown-formatted output. It ensures privacy and efficiency by processing all data locally.

---

## Features
- **Advanced OCR**: Powered by Llama 3.2 Vision for superior text extraction and formatting.
- **User-Friendly Interface**: Built with Streamlit, offering a simple and intuitive UI.
- **Local Execution**: All data is processed locally, ensuring security and privacy.

---



### Installation Instructions

#### 1. Set up Ollama
**Linux/macOS:**
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull the Llama 3.2 Vision model
ollama run llama3.2-vision
```

**Windows**
```bash	
# Install Ollama
https://ollama.com/download/windows

# Pull the Llama 3.2 Vision model
ollama run llama3.2-vision
```	
#### 2. Set up Environment

1. Clone the repository:
    ```bash
    git clone https://github.com/kanitvural/llama-ocr.git
    cd llama-ocr
    python -m venv venv
    - Windows: venv\Scripts\activate
    - Linux: source venv/bin/activate
    - Mac: source venv/bin/activate
    ```

2. Install the required packages:
    ```bash
    pip install streamlit ollama
    ```

3. Run app:
    ```bash
    streamlit run app.py
    ```
