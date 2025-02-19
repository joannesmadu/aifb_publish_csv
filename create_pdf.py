# Replace problematic characters with safe equivalents
def sanitize_text(text):
    replacements = {
        "’": "'",  # Curly apostrophe to straight apostrophe
        "“": '"',  # Open curly quote to straight quote
        "”": '"',  # Close curly quote to straight quote
        "–": "-",  # En dash to hyphen
        "—": "--"  # Em dash to double hyphen
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# Regenerate PDF with sanitized text
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='', size=12)

# Add title
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, report_title, ln=True, align='C')
pdf.ln(10)

# Add sections to PDF
pdf.set_font("Arial", size=12)
for title, content in sections:
    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(0, 10, sanitize_text(title), ln=True)
    pdf.set_font("Arial", size=12)
    for paragraph in content:
        pdf.multi_cell(0, 7, sanitize_text(paragraph))
        pdf.ln(2)
    pdf.ln(5)

# Save and provide new PDF
pdf_filename = "/mnt/data/Beauty_Industry_Report.pdf"
pdf.output(pdf_filename)

pdf_filename
