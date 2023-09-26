# HTML to PDF Converter with Flask and wkhtmltopdf

This simple Flask application allows you to convert HTML content to PDF documents using wkhtmltopdf. It provides a web interface for users to input HTML content and generate PDF files.

## Prerequisites

- Python 3.9 or higher
- wkhtmltopdf installed on your system
- Virtual environment tool (e.g., `venv`)

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/A3Brothers/html-to-pdf.git
   ```

2. Navigate to the project directory:

   ```bash
   cd html-to-pdf
   ```

3. Create a Python virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows (Command Prompt):

     ```bash
     venv\Scripts\activate
     ```

   - On Windows (PowerShell):

     ```bash
     .\venv\Scripts\Activate.ps1
     ```

5. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:

   ```bash
   python app.py
   or
   flask run
   ```

2. Open your web browser and go to http://localhost:5000/

3. Enter your HTML content in the provided textarea.

4. Click the "Convert to PDF" button.

5. The generated PDF will be available for download.

## Purpose

I created this application to convert HTMLized emails to PDF format. Many free online services have limitations, and I wanted a simple and reliable tool to perform this task. I plan to continue improving this application and adding more features in the future.

Contributions from other developers are welcome through pull requests (PRs).

Feel free to use, modify, and contribute to this project as needed.

**Note**: This README is written by the project author and is intended to provide a straightforward setup guide. For any questions or assistance, please contact the project owner.