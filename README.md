# 🚀 AI Career and Community Assistant

An AI-powered **Streamlit** application to supercharge your tech career journey!  
Helps with **job searching**, **resume feedback**, **event discovery**, and **career Q&A** – all in one place. ✨

---

## 📌 Project Overview

The **AI Career and Community Assistant** is your personal AI companion designed to:

- 🔍 **Find Jobs**: Smart keyword-based job suggestions.
- 📄 **Analyze Resumes**: Get AI-powered resume feedback instantly.
- 🗓️ **Explore Tech Events**: Discover hackathons, meetups, and more.
- 🤖 **Ask Career FAQs**: Instant answers to common career questions.

---

## 🤖 Why Llama3-8B via Groq?

- 🎯 **Accurate**: Delivers context-rich, intelligent responses.
- ⚡ **Lightning Fast**: Ultra-fast inference with Groq.
- 💸 **Cost-Efficient**: Great performance at lower cost than GPT-4.
- 🛠️ **Customizable**: Open weights for future enhancements.

---

## 🎯 Key Benefits

- 💼 Personalized job search suggestions
- 📈 On-the-spot resume feedback
- 🧳 Stay updated on relevant tech events
- 🧠 Get reliable answers to career questions
- 🎨 Sleek and responsive Streamlit UI

---

## 🧠 Core Features

| 💡 Feature              | 📝 Description                                                                 |
|------------------------|---------------------------------------------------------------------------------|
| 🤖 **AI Q&A Assistant**     | Answers your tech career questions instantly using LLM.                      |
| 📄 **Resume Analyzer**      | Upload your resume (PDF) for instant, actionable feedback.                  |
| 🔍 **Smart Job Search**     | Extracts relevant skills from your input for better job matches.            |
| 📚 **FAQ Knowledge Base**   | Preloaded answers to common tech and career questions.                      |
| 🧹 **PDF Text Extractor**   | Extracts and processes resume content using PyPDF2.                          |

---

## ⚙️ Tech Stack

| ⚙️ Tool/Library        | 🔧 Usage                                      |
|------------------------|-----------------------------------------------|
| 🐍 Python 3.10+         | Core programming language                     |
| 🌐 Streamlit            | Frontend web app framework                    |
| 🧠 Groq (Llama3-8B)     | Language model for Q&A and feedback           |
| 🎫 Eventbrite API       | Tech event discovery                         |
| 📄 PyPDF2               | Extracting text from resume PDFs             |
| 🧽 BeautifulSoup        | Web scraping for job listings                 |
| 🪵 Logging              | Debugging and monitoring                     |

---

## 🗂️ Folder Structure

```bash
.
├── utils/
│   ├── events_utils.py     # 📅 Fetches events from Eventbrite and GDG APIs
│   ├── resume_utils.py     # 📄 Extracts text and insights from resumes
│   └── llm_utils.py        # 🤖 Handles LLM interactions and FAQ responses
│
├── app.py                  # 🚀 Main Streamlit app
├── requirements.txt        # 📦 Python dependencies
└── README.md               # 📘 Project documentation

---

## 🔑 API Keys Required

| 🔐 Service  | 🧩 Purpose                      | 🔗 Get Key From                                |
|------------|----------------------------------|------------------------------------------------|
| Groq LLM   | AI-based resume & Q&A responses | [Groq Console](https://console.groq.com/)      |

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SimranShaikh20/Ai-Career-And-Community-Assistent.git
cd Ai-Career-And-Community-Assistent


## 🛠️ Setup Instructions (Continued)

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

### 3. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt

### 4. Add Environment Variables
Create a .env file in the project root with the following content:
 ```bash
GROQ_API_KEY=your_groq_api_key


### 5. Run the App
```bash
streamlit run app.py


### 🤝 Contribution Guide
- Contributions are welcome! 🙌
- Fork the repo, make your changes, and open a PR. Please ensure tests are updated accordingly.

### 📜 License
- Released under the MIT License – free for personal and commercial use.

### 👩‍💻 Author
- Made with 💖 by Simran Shaikh

### ⭐ If you found this helpful, star the repo and share it with others!
