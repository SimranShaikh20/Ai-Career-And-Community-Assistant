# Ai-Career-And-Community-Assistent


An AI-powered Streamlit application to boost your tech career journey!  
Helps users with job searching, resume analysis, event discovery, and answering FAQs. ✨

---
## 📌 Project Overview

The **AI Career and Community Assistant** is designed to **empower individuals in their tech career journey** by simplifying the process of:

- **Finding suitable jobs** based on extracted keywords.
- **Analyzing resumes** to provide instant improvement suggestions.
- **Discovering technical events** (like hackathons, meetups).
- **Answering career-related FAQs** using AI knowledge.

---

## ❓ Why I Selected This Model (Groq - Llama3-8B)

- **High Accuracy**: Llama3-8B provides precise and contextually rich answers compared to many smaller models.
- **Faster Inference**: Groq's API is optimized for extremely fast responses, critical for a real-time assistant.
- **Cost-Effective**: Delivers great performance at a lower API cost than alternatives like GPT-4.
- **Open-Weight Model**: Llama3 promotes openness and flexibility for customization in future versions.

**Compared to others (like GPT-3.5, GPT-4, Bard, Claude)**,  
Llama3-8B (via Groq) was selected because it **balances performance, speed, and affordability**, perfectly fitting a **community-focused app**.

---

## 🎯 Benefits of This Application

- **Personalized Job Search**: Extracts important skills and keywords from your search queries.
- **Instant Resume Feedback**: Helps you identify improvements without paying for premium resume services.
- **Event Discovery**: Helps users stay updated with tech events using Eventbrite API.
- **Community Support**: Answers your common career doubts instantly through AI.
- **Easy to Use**: Built on Streamlit with a clean and responsive UI.

---
## 🧠 Core Features

| Feature                  | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| 🤖 AI Q&A Assistant        | Get career & tech community related advice instantly.                       |
| 📄 Resume Analyzer         | Upload your PDF resume and receive a professional Eventbrite.                             |
| 🔎 Smart Job Search        | Extracts keywords from your search queries for better matching opportunities. |
| 📚 FAQ Knowledge Base      | Answers frequently asked technical, career, and general questions.           |
| 🧹 PDF Text Extraction     | Automatically extracts text from PDFs (like resumes).                       |

---

## ⚙️ Tech Stack

- 🐍 Python 3.10+
- 🌐 Streamlit (Frontend UI)
- 🧠 Groq LLM (Llama3-8B model)
- 🎫 Eventbrite API (Event Discovery)
- 📄 PyPDF2 (Resume text extraction)
- 🌎 BeautifulSoup ( scraping)
- 🧹 Requests, Pytz, Datetime
- 🪵 Logging for debugging

---

## 🔧 System Architecture

```mermaid
graph TD
    A[User Interaction<br>Streamlit App] -->|Career Questions| B[LLM<br>Groq API]
    A -->|Resume Upload| C[Resume Parser<br>PyPDF2]
    A -->|Event Search| D[Event APIs<br>Eventbrite/GDG]
    B --> E[AI Response]
    C --> F[Resume Analysis]
    D --> G[Event Recommendations]

> 🖼️ **Visualization**: The user interacts with the Streamlit UI ➡️ which talks to the LLM, Resume Analyzer, and Event Engines.

---

## 🛠️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/SimranShaikh20/Ai-Career-And-Community-Assistent.git
   cd career-community-assistant
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # (Windows: venv\Scripts\activate)
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Environment Variables**
   - Create a `.env` file:
     ```
     GROQ_API_KEY=your_groq_api_key
     
     ```

5. **Run the App**
   ```bash
   streamlit run app.py
   ```

---

## 📂 Folder Structure

```bash
.
├── utils/
│   ├── events_utils.py        # Event fetching logic (GDG, Eventbrite)
│   ├── resume_utils.py        # Resume text extraction
│   └── llm_utils.py           # LLM interactions (Q&A, resume analysis)
|               # FAQs knowledge base
├── app.py                     # Main Streamlit application
├── requirements.txt           # List of dependencies
└── README.md                  # You are here!
```

---

## 🔑 API Keys Needed

| Service      | Purpose                           | Link to Get API |
|--------------|------------------------------------|-----------------|
| Groq LLM     | AI responses (Llama3 model)        | [Groq Cloud](https://console.groq.com/) |
---

## 📸 Demo Screenshots (optional)

> (You can add some screenshots here later, like: Home Page, Resume Upload, Event Results, etc.)

---

## ✨ Future Improvements

- ✅ Add personalized event recommendations based on skills
- ✅ Integrate LinkedIn job scraping
- ✅ Add multi-language support (Hindi, English, etc.)
- ✅ Dark mode for Streamlit app

---

## 🤝 Contribution Guide

Contributions are welcome! 🎉  
Feel free to fork, create a feature branch, and submit a Pull Request.  
Please make sure to update tests as appropriate.

---

## 📜 License

This project is licensed under the **MIT License**.  
Free to use and modify!

---

## 👨‍💻 Author

Made with 💖 by **Simran Shaikh**

> If you like it, don't forget to ⭐ the repo!

---
