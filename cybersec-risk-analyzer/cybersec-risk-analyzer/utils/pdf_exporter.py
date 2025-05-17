from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.units import inch
import os

def export_risk_report(filename, user_data, score, recommendations):
    """
    Generate a PDF report summarizing the cybersecurity risk analysis.

    Args:
        filename (str): Path to save the PDF file.
        user_data (dict): User input data dictionary.
        score (int): Calculated risk score (0-100).
        recommendations (list): List of recommendation strings.
    """

    doc = SimpleDocTemplate(filename, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=72)

    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    heading_style = styles['Heading1']
    subheading_style = styles['Heading2']
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=normal_style,
        leftIndent=20,
        bulletIndent=10,
        spaceAfter=6,
    )

    elements = []

    # Title
    elements.append(Paragraph("🔐 Cybersecurity Risk Analysis Report", heading_style))
    elements.append(Spacer(1, 12))

    # Score summary
    score_text = f"Overall Risk Score: <b>{score}/100</b>"
    elements.append(Paragraph(score_text, subheading_style))
    elements.append(Spacer(1, 12))

    # User inputs summary
    elements.append(Paragraph("User Responses:", subheading_style))
    for key, value in user_data.items():
        text = f"<b>{key.replace('_', ' ').capitalize()}:</b> {value}"
        elements.append(Paragraph(text, normal_style))
    elements.append(Spacer(1, 12))

    # Recommendations
    elements.append(Paragraph("Recommendations:", subheading_style))
    bullet_items = [Paragraph(rec, bullet_style) for rec in recommendations]
    bullet_list = ListFlowable(
        bullet_items,
        bulletType='bullet',
        start='circle',
    )
    elements.append(bullet_list)

    # Build PDF
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    doc.build(elements)
