from flask import Flask, render_template, request, send_file
import pdfkit

app = Flask(__name__)

# Configuration of pdfkit with the wkhtmltopdf Executable Path
# To find the path to wkhtmltopdf on macOS and Linux, you can use the "which wkhtmltopdf" command.
config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate-pdf", methods=["POST"])
def generate_pdf():
    html_content = request.form.get("html_content")

    # Path to save the generated PDF
    pdf_output_path = "documents/output.pdf"

    # Generate the PDF from HTML content
    pdfkit.from_string(html_content, pdf_output_path, configuration=config)

    return send_file(pdf_output_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
