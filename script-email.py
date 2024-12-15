from flask import Flask, request, jsonify
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import smtplib

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route("/submit-assignment", methods=["POST"])
def send_email():
    try:
        # Fetch credentials from environment variables
        sender_email = os.getenv("EMAIL_ADDRESS")
        sender_password = os.getenv("EMAIL_PASSWORD")

        if not sender_email or not sender_password:
            return jsonify({"error": "Email credentials are not set in the .env file"}), 500

         # Email configuration
        to_email = os.getenv("TO_EMAIL")
        cc_email = os.getenv("CC_EMAIL")
    

        subject = "Python (Selenium) Assignment - Tharika Shree R"
        body = """
        Dear Team,

        Please find the attached files and links below as part of my assignment submission:

        1. Screenshot of the form filled via code (attached).
        2. Source code repository: [GitHub Link](https://github.com/tharikashree/web-scraper)
        3. Brief documentation of my approach: [GitHub Link](https://github.com/tharikashree/web-scraper/main/README.md)
        4. My resume (attached).
        5. Links to past projects/work samples:
           - Project 1: Product Price tracker(https://github.com/tharikashree/Product-Price-Tracker)
           - Project 2: IMDb web scraper(https://github.com/tharikashree/IMDb-webscraper)
           - Project 2: Internet Speed Twitter Bot(https://github.com/tharikashree/Internet-Speed-Twitter-Bot)
           - Project 2: Stock Trading System(https://github.com/tharikashree/Stock-Trading-System)

         Please find attached my assignment submission for the Python (Selenium) project. I am available to work for the required time period and can start immediately.
        I look forward to your response.

        Best regards,  
        Tharika Shree R
        """

        # Create email message
        msg = EmailMessage()
        msg["From"] = sender_email
        msg["To"] = ", ".join(to_email)
        msg["Cc"] = ", ".join(cc_email)
        msg["Subject"] = subject
        msg.set_content(body)

        # Attach the screenshot
        with open("confirmation.png", "rb") as screenshot:
            msg.add_attachment(screenshot.read(), maintype="image", subtype="png", filename="confirmation.png")

        # Attach the resume
        with open("resume.pdf", "rb") as resume:
            msg.add_attachment(resume.read(), maintype="application", subtype="pdf", filename="resume.pdf")

        # Send email via Gmail's SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)

        return jsonify({"message": "Assignment email sent successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
