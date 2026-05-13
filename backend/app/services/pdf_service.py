from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_analysis_pdf(analysis, output_path):
    doc = SimpleDocTemplate(output_path)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Resume Analysis", styles["Title"]))

    for i, q in enumerate(analysis.get("suggested_interview_questions", [])):
        content.append(Paragraph(f"Q{i+1}: {q}", styles["Normal"]))

    if analysis.get("summary"):
        content.append(Paragraph("<br/>Summary:", styles["Heading2"]))
        content.append(Paragraph(analysis["summary"], styles["Normal"]))

    doc.build(content)

    return output_path