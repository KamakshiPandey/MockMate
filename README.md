# 🤖 MockMate AI

MockMate AI is an AI-powered interview preparation platform that generates personalized interview questions based on a user's resume.

It helps users practice interviews in a realistic environment by analyzing their resume, generating relevant questions, and providing AI-based feedback.

---

## 📌 How It Works

The system works in 4 main steps:

### 1️⃣ Resume Upload
- User uploads their resume (PDF/DOCX)
- Backend receives and processes the file

### 2️⃣ Resume Data Extraction
- Resume content is extracted and cleaned
- Important sections identified:
  - Skills
  - Projects
  - Experience
  - Education

### 3️⃣ AI Question Generation
- Extracted resume data is sent to AI APIs
- AI generates:
  - Technical questions
  - HR questions
  - Project-based questions

### 4️⃣ Interview Simulation
- User interacts via chat interface
- AI evaluates answers and provides feedback

---

## 🤖 APIs Used

### 🔹 OpenAI API / Groq API
- Used for generating interview questions and evaluating answers
- Takes resume content as input and returns structured responses

### 🔹 Hugging Face API
- Used for text processing and improving resume understanding

### 🔹 Custom Backend APIs (Node.js + Express)

- `/upload-resume` → Upload and process resume  
- `/generate-questions` → Generate AI-based questions  
- `/evaluate-answer` → Evaluate and score answers  

---

## 🛠️ Tech Stack

### Frontend
- React.js
- JavaScript

### Backend
- Node.js
- Express.js

### AI Integration
- OpenAI API / Groq API
- Hugging Face API



---

## 📂 Project Structure
