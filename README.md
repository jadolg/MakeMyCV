# MakeMyCV - CV/Resume PDF Generator

MakeMyCV is a lightweight FastAPI-based web application that allows you to generate professional-looking CVs/Resumes in PDF format using Jinja2 templates and WeasyPrint.

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) (recommended)
- OR Python 3.14+ with WeasyPrint dependencies installed (see [WeasyPrint installation guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation))

### Running with Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd MakeMyCV
   ```

2. Build and run the application:
   ```bash
   docker-compose up --build
   ```

3. Access the application at `http://localhost:8000`.

### Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: Ensure system dependencies for WeasyPrint (like Pango, Cairo, and GdkPixbuf) are installed.*

2. Run the application:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

## API Usage

The application provides a simple API for generating and previewing CVs.

### Endpoints

- **GET `/`**: Serves the index page.
- **POST `/generate`**: Generates and downloads a CV as a PDF file.
- **POST `/preview`**: Generates a CV and returns the PDF bytes for previewing.

### Example Request Body (`CVData`)

```json
{
  "personal_info": {
    "full_name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "+1 234 567 890",
    "location": "New York, USA",
    "website": "https://johndoe.me",
    "linkedin": "https://linkedin.com/in/johndoe",
    "github": "https://github.com/johndoe",
    "profile_picture": "https://example.com/photo.jpg",
    "summary": "Experienced software engineer with a passion for building scalable web applications."
  },
  "education": [
    {
      "institution": "University of Technology",
      "degree": "B.Sc. in Computer Science",
      "start_date": "2015-09-01",
      "end_date": "2019-06-30",
      "location": "Boston, USA"
    }
  ],
  "experience": [
    {
      "company": "Tech Solutions Inc.",
      "position": "Senior Developer",
      "start_date": "2019-07-01",
      "end_date": "Present",
      "location": "New York, USA",
      "description": [
        "Led a team of 5 developers to build a cloud-native platform.",
        "Improved system performance by 30% through code optimization."
      ]
    }
  ],
  "skills": [
    { "name": "Python" },
    { "name": "FastAPI" },
    { "name": "Docker" }
  ],
  "languages": ["English", "Spanish"],
  "template_name": "template1",
  "language": "en"
}
```

### Example CURL Command

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "personal_info": {
      "full_name": "John Doe",
      "email": "john.doe@example.com",
      "phone": "+1 234 567 890",
      "location": "New York, USA",
      "summary": "Experienced software engineer."
    },
    "education": [],
    "experience": [],
    "skills": [
       { "name": "Python" }
    ],
    "languages": ["English"],
    "template_name": "template2",
    "language": "en"
  }' \
  --output my_cv.pdf
```
