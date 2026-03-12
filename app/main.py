from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.schemas.cv import CVData
from app.utils.pdf import generate_pdf, render_cv_html
import os
import jinja2

app = FastAPI()

# Get the path for templates and static files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
if not os.path.exists(os.path.join(BASE_DIR, "static")):
    os.makedirs(os.path.join(BASE_DIR, "static"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate(cv_data: CVData):
    try:
        pdf_bytes = generate_pdf(cv_data.model_dump(), cv_data.template_name)
    except jinja2.exceptions.TemplateNotFound:
        raise HTTPException(status_code=400, detail=f"Template {cv_data.template_name} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={cv_data.personal_info.full_name.replace(' ', '_')}_CV.pdf"}
    )

@app.post("/preview")
async def preview(cv_data: CVData):
    try:
        html_content = render_cv_html(cv_data.model_dump(), cv_data.template_name)
    except jinja2.exceptions.TemplateNotFound:
        raise HTTPException(status_code=400, detail=f"Template {cv_data.template_name} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return Response(content=html_content, media_type="text/html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
