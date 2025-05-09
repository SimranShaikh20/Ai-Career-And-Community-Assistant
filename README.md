# 🚀 AI Career and Community Assistant

An AI-powered **Streamlit** application to supercharge your tech career journey!  
Helps with **job searching**, **resume feedback** and **career Q&A** – all in one place. ✨

---
[Live App ](https://ai-career-and-community-assistant-7voz2ccvpofdntk7rntseh.streamlit.app/)

---
## 📌 Project Overview

The **AI Career and Community Assistant** is your personal AI companion designed to:

* 🔍 **Find Jobs**: Smart keyword-based job suggestions.
* 📄 **Analyze Resumes**: Get AI-powered resume feedback instantly.
* 🗓️ **Explore Tech Events**: Discover hackathons, meetups, and more.
* 🤖 **Ask Career FAQs**: Instant answers to common career questions.

---

## 🤖 Why Llama3-8B via Groq?

* 🎯 **Accurate**: Delivers context-rich, intelligent responses.
* ⚡ **Lightning Fast**: Ultra-fast inference with Groq.
* 💸 **Cost-Efficient**: Great performance at lower cost than GPT-4.
* 🛠️ **Customizable**: Open weights for future enhancements.

---

## 🎯 Key Benefits

* 💼 Personalized job search suggestions
* 📈 On-the-spot resume feedback
* 🧳 Stay updated on relevant tech events
* 🧠 Get reliable answers to career questions
* 🎨 Sleek and responsive Streamlit UI

---

## 🧠 Core Features

| 💡 Feature                | 📝 Description                                                   |
| ------------------------- | ---------------------------------------------------------------- |
| 🤖 **AI Q&A Assistant**    | Answers your tech career questions instantly using LLM.         |
| 📄 **Resume Analyzer**     | Upload your resume (PDF) for instant, actionable feedback.      |
| 🔍 **Smart Job Search**    | Extracts relevant skills from your input for better job matches.|
| 📚 **FAQ Knowledge Base**  | Preloaded answers to common tech and career questions.          |
| 🧹 **PDF Text Extractor**  | Extracts and processes resume content using PyPDF2.             |

---

## ⚙️ Tech Stack

| ⚙️ Tool/Library     | 🔧 Usage                             |
| ------------------- | ------------------------------------ |
| 🐍 Python 3.10+     | Core programming language            |
| 🌐 Streamlit        | Frontend web app framework           |
| 🧠 Groq (Llama3-8B) | Language model for Q&A and feedback  |
| 📄 PyPDF2           | Extracting text from resume PDFs     |
| 🧽 BeautifulSoup    | Web scraping for job listings        |

---

## 🗂️ Folder Structure

```bash
ai-career-and-community-assistant/
├── app.py                   # 🚀 Main Streamlit app entry point
├── .env                     # 🔐 Environment variables (not committed)
├── requirements.txt         # 📦 Python dependencies
├── README.md                # 📘 Project documentation

├── utils/
│   ├── events_utils.py      # 📅 Fetches tech events from APIs
│   ├── resume_utils.py      # 📄 Resume parsing and feedback logic
│   └── llm_utils.py         # 🤖 Interacts with LLM for Q&A and feedback

├── pages/
│   ├── job_search.py        # 🔍 Smart job search UI
│   ├── resume_analyzer.py   # 📄 Resume upload and analysis page
│   ├── event_finder.py      # 🗓️ Event discovery page
│   └── community.py         # 🧠 Career Q&A assistant

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

---
