# Vista AI – Intelligent Content Summarization System  

## Overview  
Vista AI is a Python-based web application built using Flask and standard web technologies to automate content summarization. The system extracts and processes data from multiple sources such as YouTube videos, plain text, and uploaded documents.

It helps users quickly understand large volumes of information by generating concise summaries in structured formats, improving productivity and reducing manual effort.

---

## Objectives  
- Automate the process of content summarization  
- Reduce time required to read or watch large content  
- Support multiple input formats (video, text, documents)  
- Provide flexible output formats (points and paragraph)  
- Enable download of summarized content  

---

## Key Features  

### Multi-Source Input  
Supports input from:  
- YouTube video links  
- Manual text input  
- Document upload (PDF, DOCX, TXT)  

### Automated Text Extraction  
- Extracts transcripts from YouTube videos  
- Reads content from PDF and DOCX files  
- Processes raw text input  

### Summarization Engine  
Implements a sentence-based approach to:  
- Identify important sentences  
- Generate concise summaries  
- Maintain original meaning  

### Custom Output Options  
- Summary length selection (short, medium, detailed)  
- Output format selection (bullet points or paragraph)  

### Download Feature  
Allows users to download summarized content as a text file  

---

## Technology Stack  

**Backend:**  
- Python  
- Flask  

**Frontend:**  
- HTML5  
- CSS3  

**Libraries & Tools:**  
- YouTube Transcript API  
- PyPDF2  
- python-docx  

---

## Project Structure  

Vista-AI/
│── backend_v3/
│   │── app.py
│   │── requirements.txt
│   │
│   ├── templates/
│   │   │── login.html
│   │   │── register.html
│   │   │── dashboard.html
│   │   │── summarize.html
│   │   │── result.html
│   │
│   ├── static/
│   │   │── style.css
│
│── screenshots/
│   │── profile.png
│   │── create.png
│   │── dashboard.png
│   │── summarise.png
│   │── output.png

---

## Installation and Setup  

### Prerequisites  
- Python 3.8 or higher  
- pip  
- IDE (VS Code recommended)  

### Steps  

1. Clone the repository  
git clone https://github.com/your-username/vista-ai.git  

2. Navigate to project folder  
cd vista-ai/backend_v3  

3. Create virtual environment  
python -m venv venv  

4. Activate virtual environment  
venv\Scripts\activate  

5. Install dependencies  
pip install -r requirements.txt  

If requirements.txt not available:  
pip install flask youtube-transcript-api PyPDF2 python-docx  

6. Run the application  
python app.py  

7. Open in browser  
http://127.0.0.1:5000  

---

## Usage  

1. Register a new account  
2. Login to the system  
3. Open dashboard  
4. Provide input:  
   - YouTube link  
   - Text input  
   - Upload document  
5. Select summary length and format  
6. Click summarize  
7. View and download result  

---

## System Interface  

### Login / Profile  
User authentication to access system  

### Dashboard  
Main page to start summarization  

### Summarization Page  
Input YouTube link, text, or upload document  

### Result Page  
Displays summarized output with download option  

---

## Screenshots  

### Login Page  
![Login](screenshots/profile.png)

### Registration Page  
![Create](screenshots/create.png)

### Dashboard  
![Dashboard](screenshots/dashboard.png)

### Summarization Page  
![Summarize](screenshots/summarise.png)

### Output Result  
![Output](screenshots/output.png)

---

## Limitations  

- Requires internet for YouTube processing  
- Works only for videos with captions  
- Basic summarization technique  

---

## Future Enhancements  

- Advanced NLP-based summarization  
- Multi-language support  
- Voice input  
- Improved UI design  
- Cloud deployment  

---

## Conclusion  

Vista AI provides an efficient solution for summarizing large content from multiple sources. It demonstrates practical implementation of web technologies and text processing techniques to reduce information overload and improve productivity.




- Your Name  
- Member 2  
- Member 3
