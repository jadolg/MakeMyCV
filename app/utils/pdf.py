from weasyprint import HTML
import jinja2
import os

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")

def render_cv_html(cv_data: dict, template_name: str) -> str:
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIR), autoescape=True)
    template_file = f"{template_name}.html"
    template = env.get_template(template_file)
    
    # Simple localization
    translations = {
        "en": {
            "summary": "Professional Summary",
            "experience": "Experience",
            "education": "Education",
            "skills": "Skills",
            "contact": "Contact",
            "languages": "Languages",
            "website": "Website",
            "linkedin": "LinkedIn",
            "phone": "Phone",
            "email": "Email",
            "location": "Location",
            "at": "at"
        },
        "es": {
            "summary": "Resumen Profesional",
            "experience": "Experiencia",
            "education": "Educación",
            "skills": "Habilidades",
            "contact": "Contacto",
            "languages": "Idiomas",
            "website": "Sitio Web",
            "linkedin": "LinkedIn",
            "phone": "Teléfono",
            "email": "Correo Electrónico",
            "location": "Ubicación",
            "at": "en"
        }
    }
    lang = cv_data.get("language", "en")
    t = translations.get(lang, translations["en"])
    
    return template.render(data=cv_data, t=t)

def generate_pdf(cv_data: dict, template_name: str) -> bytes:
    html_out = render_cv_html(cv_data, template_name)
    
    pdf_bytes = HTML(string=html_out, base_url=TEMPLATES_DIR).write_pdf()
    return pdf_bytes
