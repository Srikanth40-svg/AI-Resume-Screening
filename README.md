# 🤖 AI Resume Screening & Job Matching 
## 🚀 Live Demo

[Try the AI Resume Screening App](https://ai-resume-screening-qdpbu5yoiaqqyr49vbhikq.streamlit.app/)

An LLM-powered resume screening system that analyzes job descriptions, extracts structured information from candidate resumes, evaluates candidate-job compatibility, and ranks candidates based on their match scores.

The project uses the **Groq API** for LLM inference and **Pydantic** for structured data validation.

## 🚀 Features

* 📄 Supports **PDF** and **DOCX** resumes
* 🔍 Extracts structured requirements from job descriptions
* 🧠 Parses candidate resumes using an LLM
* 📋 Extracts candidate skills, education, experience, projects, and certifications
* 🎯 Compares resumes against job requirements
* 📊 Generates a candidate match score
* ✅ Identifies matching skills
* ❌ Identifies missing important skills
* 🏆 Ranks candidates based on their scores
* 📈 Displays the top 2 and lowest 2 candidates

## 🏗️ Workflow


Job Description
       │
       ▼
LLM Job Parser
       │
       ▼
Structured Job Data
       │
       │
Resumes ──► PDF/DOCX Parser
       │
       ▼
LLM Resume Parser
       │
       ▼
Structured Resume Data
       │
       ▼
LLM Matching & Scoring
       │
       ▼
Candidate Match Score
       │
       ▼
Candidate Ranking
       │
       ├──► Top 2
       └──► Lowest 2


## 🛠️ Tech Stack

* **Python 3.11+**
* **Groq API**
* **Pydantic**
* **PyPDF**
* **python-docx**
* **python-dotenv**

## 📁 Project Structure


day5/
│
├── resumes/
│   ├── resume1.pdf
│   ├── resume2.pdf
│   └── resume3.docx
│
├── main.py
├── pyproject.toml
├── README.md
└── .gitignore


> Create a `.env` file locally for your API key. It should not be committed to the repository.

## ⚙️ Installation

### 1. Clone the repository


git clone <your-repository-url>
cd day5


### 2. Create a virtual environment


python -m venv .venv


Activate it on Windows:


.venv\Scripts\activate


On Linux/macOS:


source .venv/bin/activate


### 3. Install dependencies


pip install -e .


Or install the dependencies directly:


pip install groq pydantic pypdf python-docx python-dotenv


## 🔑 Environment Variables

Create a `.env` file in the project root:


GROQ_API_KEY=your_groq_api_key

The application loads the API key using `python-dotenv` and initializes the Groq client with it.

**Never commit your `.env` file or API key to GitHub.**

## ▶️ Usage

Place candidate resumes inside the `resumes/` directory.

Supported formats:


.pdf
.docx


Run the application:


python resume_parser.py


The application processes each resume, extracts structured candidate information, compares it against the job description, and generates a match score.

## 🧠 How It Works

### 1. Job Description Parsing

The LLM analyzes the job description and extracts:

* Role
* Required skills
* Preferred skills
* Minimum experience
* Education requirements
* Responsibilities

The extracted information is validated using a Pydantic model.

### 2. Resume Parsing

The application extracts text from the candidate's resume.

* **PDF:** parsed using `pypdf`
* **DOCX:** parsed using `python-docx`

The extracted text is then passed to the LLM.

The resume parser extracts:

* Name
* Email
* Phone
* Total experience
* Skills
* Work experience
* Education
* Projects
* Certifications

### 3. Candidate Matching

The structured job description and parsed resume are passed to an LLM for comparison.

The model evaluates:

* Matching skills
* Missing important skills
* Experience requirements
* Overall compatibility
* Match score
* Final verdict

### 4. Candidate Ranking

After all resumes are processed, candidates are sorted by their match score in descending order.

all_results.sort(
    key=lambda candidate: candidate["score"],
    reverse=True
)


The application then displays the highest- and lowest-scoring candidates.

## 📊 Example Output

Example output:


Processing: candidate1.pdf
Score: 82.5

Processing: candidate2.pdf
Score: 71.0

Processing: candidate3.docx
Score: 91.0

TOP 2 CANDIDATES

Candidate 3 - 91.0%
Candidate 1 - 82.5%

LOWEST 2 CANDIDATES

Candidate 2 - 71.0%
Candidate 4 - 65.5%


> Scores shown above are illustrative examples.

## 📌 Data Models

Pydantic models are used to structure and validate the information produced by the LLM.

The project defines models for:

* Job descriptions
* Candidate resumes
* Work experience
* Education
* Projects
* Matching results

This provides a consistent structure for downstream processing.

## 🔐 Security

Add `.env` to `.gitignore`:

```gitignore
# Python-generated files
__pycache__/
*.py[oc]

# Build files
build/
dist/
wheels/
*.egg-info/

# Virtual environment
.venv/

# Environment variables
.env
```

Never expose your `GROQ_API_KEY` in source code, README files, screenshots, or GitHub commits.

## 🔮 Future Improvements

* Add a **Streamlit web interface**
* Add candidate filtering and search
* Export results to **CSV/Excel**
* Generate detailed candidate reports
* Add database storage
* Support batch processing at scale
* Add OCR support for scanned resumes
* Improve scoring with deterministic weighted metrics
* Add recruiter dashboard
* Support multiple job descriptions

## 📚 Learning Outcomes

This project demonstrates practical experience with:

* LLM API integration
* Prompt engineering
* Structured LLM responses
* Pydantic data validation
* PDF and DOCX document processing
* Resume information extraction
* Candidate-job matching
* Automated candidate ranking
* Python dependency management

## 👨‍💻 Author

Jadi Srikanth
IIT Madras
