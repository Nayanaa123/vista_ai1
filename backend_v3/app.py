from flask import Flask, render_template, request, redirect, url_for, session
from youtube_transcript_api import YouTubeTranscriptApi
import re
import PyPDF2
import docx

app = Flask(__name__)
app.secret_key = "vista_ai_secret"

# Temporary users database
users = {"admin": "1234"}

# ---------------- HOME ----------------
@app.route("/")
def home():
    return redirect(url_for("login"))

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users:
            return "User already exists!"

        users[username] = password
        return redirect(url_for("login"))

    return render_template("register.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("dashboard"))

        return "Invalid credentials"

    return render_template("login.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


# ---------------- SUMMARIZE ----------------
@app.route("/summarize", methods=["GET", "POST"])
def summarize():

    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        youtube_url = request.form.get("youtube_url", "").strip()
        text_input = request.form.get("text_input", "").strip()
        uploaded_file = request.files.get("doc_file")

        length = int(request.form.get("length", 5))
        fmt = request.form.get("format", "paragraph")

        raw_text = ""

        # ---------- YOUTUBE ----------
        if youtube_url:
            try:
                video_id = None

                if "v=" in youtube_url:
                    video_id = youtube_url.split("v=")[1].split("&")[0]

                elif "youtu.be/" in youtube_url:
                    video_id = youtube_url.split("youtu.be/")[1].split("?")[0]

                if video_id:
                    api = YouTubeTranscriptApi()
                    transcript = api.fetch(video_id)

                    raw_text = " ".join([item.text for item in transcript])

                else:
                    raw_text = "Error: Invalid YouTube link."

            except Exception as e:
                raw_text = f"YouTube Error: {str(e)}"


        # ---------- DOCUMENT ----------
        elif uploaded_file and uploaded_file.filename != "":

            ext = uploaded_file.filename.split(".")[-1].lower()

            try:

                if ext == "txt":
                    raw_text = uploaded_file.read().decode("utf-8")

                elif ext == "pdf":
                    reader = PyPDF2.PdfReader(uploaded_file)

                    raw_text = " ".join(
                        [page.extract_text() for page in reader.pages if page.extract_text()]
                    )

                elif ext == "docx":
                    document = docx.Document(uploaded_file)

                    raw_text = " ".join([p.text for p in document.paragraphs])

                else:
                    raw_text = "Unsupported file format."

            except Exception as e:
                raw_text = f"File Error: {str(e)}"


        # ---------- TEXT ----------
        elif text_input:
            raw_text = text_input


        # ---------- SUMMARIZER ----------
        if not raw_text or "Error" in raw_text:

            session["summary"] = [raw_text if raw_text else "No content found."]
            session["is_points"] = False

        else:

            sentences = re.split(r'(?<=[.!?]) +', raw_text)

            if len(sentences) <= 1:
                words = raw_text.split()

                sentences = [
                    " ".join(words[i:i+15]) for i in range(0, len(words), 15)
                ]

            summary_sentences = sentences[:length]

            session["summary"] = summary_sentences
            session["is_points"] = (fmt == "points")

        return redirect(url_for("result"))

    return render_template("summarize.html")


# ---------------- RESULT ----------------
@app.route("/result")
def result():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "result.html",
        summary=session.get("summary", []),
        is_points=session.get("is_points", False)
    )


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)