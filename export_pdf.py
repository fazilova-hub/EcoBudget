from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet

def export_to_pdf(data, metrics, recommendations, filename):
    """Экспортирует результаты в PDF."""
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Отчёт EcoBudget", styles['Title']))
    story.append(Paragraph(f"Общий запланированный бюджет: {metrics['total_planned']}", styles['Normal']))
    story.append(Paragraph(f"Фактический бюджет: {metrics['total_actual']}", styles['Normal']))
    story.append(Paragraph(f"Коэффициент выполнения: {metrics['execution_rate']:.2f}%", styles['Normal']))


    for rec in recommendations:
        story.append(Paragraph(rec, styles['Normal
