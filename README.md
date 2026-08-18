````markdown
# 🤖 AI Resume Screening & Job Matching

## 🚀 Live Demo

[Try the AI Resume Screening App](https://ai-resume-screening-qdpbu5yoiaqqyr49vbhikq.streamlit.app/)

An LLM-powered resume screening system that analyzes job descriptions, extracts structured information from candidate resumes, evaluates candidate-job compatibility, ranks candidates based on their match scores, and provides an interactive Streamlit dashboard.

The project uses the **Groq API** for LLM inference, **Pydantic** for structured data validation, and **Streamlit** for the web interface.

---

## 🚀 Features

- 📄 Supports **PDF** and **DOCX** resumes
- 📤 Uploads multiple candidate resumes
- 📝 Accepts job descriptions directly through the web interface
- 🔍 Extracts structured requirements from job descriptions
- 🧠 Parses candidate resumes using an LLM
- 📋 Extracts candidate skills, education, experience, projects, and certifications
- 🎯 Compares candidates against job requirements
- 📊 Generates an overall candidate match score
- ✅ Identifies matching skills
- ❌ Identifies missing important skills
- 💼 Evaluates experience requirements
- 🧠 Generates an AI-based candidate verdict
- 🏆 Automatically ranks candidates by match score
- 📈 Displays candidate statistics and rankings
- 📥 Exports screening results as CSV
- 🌐 Deployed using Streamlit Community Cloud

---

## 🏗️ Workflow

```text
                    Job Description
                           │
                           ▼
                  ┌─────────────────┐
                  │  LLM Job Parser │
                  └────────┬────────┘
                           │
                           ▼
                  Structured Job Data
                           │
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
        ▼                                     ▼
   PDF Resume                          DOCX Resume
        │                                     │
        └──────────────────┬──────────────────┘
                           ▼
                  Resume Text Extraction
                           │
                           ▼
                  ┌─────────────────┐
                  │  LLM Resume     │
                  │     Parser      │
                  └────────┬────────┘
                           │
                           ▼
                  Structured Resume Data
                           │
                           ▼
                  ┌─────────────────┐
                  │  LLM Matching   │
                  │   & Scoring     │
                  └────────┬────────┘
                           │
                           ▼
                    Match Score
                           │
                           ▼
                  Candidate Ranking
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
              Top 2              Lowest 2
                           │
                           ▼
                     CSV Export
````

---

## 🖥️ Streamlit Interface

The application provides an interactive dashboard where users can:

1. Enter a job description
2. Upload multiple candidate resumes
3. Start AI-powered analysis
4. View candidate rankings
5. Review matching and missing skills
6. Check experience requirements
7. Read the AI-generated verdict
8. Download screening results as CSV

---

## 🛠️ Tech Stack

* **Python 3.11+**
* **Streamlit**
* **Groq API**
* **Pydantic**
* **Pandas**
* **PyPDF**
* **python-docx**
* **python-dotenv**

---

## 📁 Project Structure

```text
day5/
│
├── app.py
├── resume_parser.py
├── main.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── .gitignore
└── uv.lock
```

> Candidate resumes and `.env` are intentionally excluded from the GitHub repository for privacy and security.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd day5
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

For local development, create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

The application loads the API key using `python-dotenv`.

For the deployed Streamlit application, the API key is stored securely using **Streamlit Secrets**.

**Never commit your `.env` file or API key to GitHub.**

---

## ▶️ Run Locally

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📋 Usage

### 1. Enter Job Description

Paste the complete job description into the **Job Description** field.

### 2. Upload Resumes

Upload one or more candidate resumes.

Supported formats:

```text
.pdf
.docx
```

### 3. Analyze Candidates

Click:

```text
🚀 Analyze Resumes
```

The application processes each resume and evaluates it against the job requirements.

### 4. Review Candidate Rankings

The dashboard displays:

* Number of candidates analyzed
* Top candidate score
* Average score
* Candidate rankings

### 5. Review Candidate Details

Each candidate can be expanded to view:

* Match score
* Matching skills
* Missing important skills
* Experience requirement
* AI-generated verdict

### 6. Export Results

Click:

```text
📥 Download Results as CSV
```

The exported CSV contains:

```text
Candidate
Score
Matching Skills
Missing Skills
Experience Requirement
Verdict
```

---

## 🧠 How It Works

### 1. Job Description Parsing

The LLM analyzes the job description and extracts relevant information such as:

* Role
* Required skills
* Preferred skills
* Minimum experience
* Education requirements
* Responsibilities

The extracted information is validated using Pydantic models.

### 2. Resume Parsing

The application extracts text from uploaded resumes.

* **PDF:** parsed using `pypdf`
* **DOCX:** parsed using `python-docx`

The extracted resume text is then passed to the LLM for structured information extraction.

The system extracts:

* Candidate name
* Email
* Phone
* Experience
* Skills
* Work experience
* Education
* Projects
* Certifications

### 3. Candidate Matching

The structured job description and parsed candidate information are passed to the LLM for comparison.

The model evaluates:

* Matching skills
* Missing important skills
* Experience requirements
* Overall compatibility
* Match score
* Final verdict

### 4. Candidate Ranking

Candidates are sorted by their match score in descending order:

```python
results.sort(
    key=lambda candidate: candidate["score"],
    reverse=True
)
```

The ranked candidates are then displayed through the Streamlit dashboard.

---

## 📊 Example Output

```text
🏆 Candidate Rankings

Candidates Analyzed    3
Top Score              80.0%
Average Score          54.3%

🥇 Candidate A — 80.0%
🥈 Candidate B — 62.0%
🥉 Candidate C — 21.0%
```

Each candidate can be expanded to view:

```text
Match Score

✅ Matching Skills
• Python
• Machine Learning
• Data Structures & Algorithms

❌ Missing Skills
• SQL
• Cloud Technologies

💼 Experience Requirement
Experience requirement met

🧠 AI Verdict
Strong match on the core technical requirements.
```

> Scores shown above are illustrative examples.

---

## 📥 CSV Export

The application converts the screening results into a structured CSV file.

Example:

```text
Candidate,Score,Matching Skills,Missing Skills,Experience Requirement,Verdict

Candidate A,80.0,"Python, Machine Learning","SQL",True,"Strong overall match"

Candidate B,62.0,"Python","SQL, Cloud Technologies",False,"Moderate match"

Candidate C,21.0,"Python","Java, SQL, Cloud Technologies",False,"Low overall match"
```

---

## 📌 Data Models

Pydantic models are used to structure and validate information generated by the LLM.

The project uses structured models for:

* Job descriptions
* Candidate resumes
* Work experience
* Education
* Projects
* Matching results

This provides consistent data structures for downstream processing.

---

## 🔐 Security & Privacy

The following files are excluded from the repository:

```text
.env
.venv/
resumes/
```

The `.gitignore` file prevents API credentials, virtual environments, and candidate resumes from being committed.

The Groq API key is stored locally in `.env` during development and in **Streamlit Secrets** for the deployed application.

**Never expose your `GROQ_API_KEY` in source code, README files, screenshots, or GitHub commits.**

Candidate resumes may contain personal information and should only be processed when appropriate authorization is available.

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

```text
GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
app.py
       ↓
Live Web Application
```

### Live Application

[AI Resume Screening & Job Matching](https://ai-resume-screening-qdpbu5yoiaqqyr49vbhikq.streamlit.app/)

---

## 🔮 Future Improvements

* 📊 Add advanced score visualizations
* 🔎 Add candidate filtering and search
* 📑 Generate detailed candidate reports
* 📥 Export results to Excel/PDF
* 🗄️ Add database storage
* 🔤 Add OCR support for scanned resumes
* ⚖️ Improve scoring with deterministic weighted metrics
* 👥 Add recruiter authentication
* 📊 Add recruiter analytics dashboard
* 🧠 Improve semantic skill matching
* 📋 Support multiple job descriptions
* 🚀 Add batch processing for large candidate pools

---

## 📚 Learning Outcomes

This project demonstrates practical experience with:

* LLM API integration
* Groq API
* Prompt engineering
* Structured LLM outputs
* Pydantic data validation
* PDF and DOCX document processing
* Resume information extraction
* Candidate-job matching
* Candidate ranking
* Streamlit application development
* CSV data export
* Python dependency management
* Environment variable and secret management
* Git and GitHub
* Cloud deployment

---

## 👨‍💻 Author

**Jadi Srikanth**

**IIT Madras**

---

## ⭐ Project

An end-to-end **AI Resume Screening & Job Matching system** that combines LLM-based document understanding, structured outputs, candidate scoring, ranking, an interactive Streamlit dashboard, CSV export, and cloud deployment.

```
```
