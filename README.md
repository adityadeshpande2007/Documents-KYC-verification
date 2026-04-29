# Automated KYC Verification System

An intelligent KYC (Know Your Customer) verification system powered by **Google Gemini AI**. This application automates the extraction and validation of identity documents, reducing manual effort and improving accuracy.

## 🚀 Features
- **AI-Powered OCR**: Uses Google Gemini API to extract data from ID documents.
- **Automated Validation**: Checks for missing fields and basic data integrity.
- **Clean UI**: Built with Streamlit for a smooth user experience.
- **Scalable Backend**: Flask API for handling document processing.
- **Database Integration**: Saves verified data to a local SQLite database.

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: Flask
- **AI Model**: Google Gemini API
- **Database**: SQLite
- **Language**: Python

## 📂 Project Structure
```text
kyc_app/
├── app.py              # Streamlit frontend
├── backend.py          # Flask backend API
├── database.py         # SQLite database operations
├── gemini_api.py       # Gemini AI integration
├── utils.py            # Utility functions for parsing & validation
├── requirements.txt    # Project dependencies
└── data.db             # Local SQLite database
```

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/adityadeshpande2007/Documents-KYC-verification.git
   cd Documents-KYC-verification
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**
   - Open `gemini_api.py`
   - Replace the API key with your own Google AI Studio key.

## 🏃 Running the Application

You need to run both the backend and the frontend.

1. **Start the Flask Backend**
   ```bash
   python backend.py
   ```

2. **Start the Streamlit Frontend** (Open a new terminal)
   ```bash
   streamlit run app.py
   ```

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---
Developed by [Aditya Deshpande](https://github.com/adityadespande2007)
