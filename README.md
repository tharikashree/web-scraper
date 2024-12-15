# Web Scrape Assignment - Selenium with Flask Email Submission

This project demonstrates how to automate the process of filling out a Google Form using Selenium and Flask. The project also includes functionality for sending an email with the form submission results via Flask.

## Project Structure

    
    web-scrape-assignment/
    │
    ├── script-email.py   # Flask app for sending email with form data
    ├── main.py          # Script to automate filling the Google Form using Selenium
    ├── requirements.txt        
    ├── .gitignore              
    └── README.md               


## Features

- **Automated Google Form Filling**: Uses Selenium to automate filling out the Google Form.
- **Email Submission**: Once the form is filled, the results are sent via email using Flask.

## Prerequisites

Ensure you have the following installed:

- **Python 3.x**: Install from the official website: [Python.org](https://www.python.org/downloads/)
- **Selenium**: Python library for automating browsers.
- **Flask**: Python framework to build web applications.
- **Webdriver**: Web browser driver (e.g., ChromeDriver for Chrome).
- **Other dependencies**: Listed in the `requirements.txt`.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/web-scrape-assignment.git
   cd web-scrape-assignment

2. **Install the dependencies**:

   Create and activate a virtual environment:
   
          python -m venv venv
          # On Windows
          venv\Scripts\activate
          # On macOS/Linux
          source venv/bin/activate
   Install the required libraries:

        pip install -r requirements.txt
3. **Set up WebDriver**:

  Download the appropriate WebDriver for your browser (e.g., ChromeDriver) and ensure it's accessible from your system’s PATH.

## Usage

1. Fill the Google Form:
In the form_filler.py script, update the XPaths and selectors for the form fields to match the Google Form you want to automate.
Run the script:
        
        python form_filler.py
This will automatically fill out the form and take a screenshot once it's complete.

2. Send Email:
After filling the form, the data is passed to the Flask app in email.py, where the results are emailed.

Run the Flask application to handle the email:

    python email.py
This will send an email with the form submission results.

## Requirements
Selenium: To control the browser and automate the form filling process.
Flask: To handle the email sending after the form is filled.
WebDriver: ChromeDriver or another WebDriver to run the browser.
Install the requirements:

    pip install -r requirements.txt
## Testing
Ensure that your environment is correctly set up, and all dependencies are installed. Run the following tests to ensure that the script is correctly interacting with the form and sending the email.

    python main.py
    python script-email.py
