from pydantic import BaseModel, EmailStr, field_validator, ValidationInfo
from typing import List, Optional, Literal

class PersonalInfo(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    location: str
    website: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    profile_picture: Optional[str] = None
    summary: str

    @field_validator('profile_picture')
    @classmethod
    def validate_profile_picture(cls, v: Optional[str], info: ValidationInfo) -> Optional[str]:
        if v is not None:
            # Prevent Server-Side Request Forgery (SSRF) and Local File Read
            if v.startswith('file://'):
                raise ValueError("file:// URLs are not allowed for security reasons.")
            if not (v.startswith('http://') or v.startswith('https://') or v.startswith('data:image/')):
                raise ValueError("Profile picture must be a valid HTTP/HTTPS URL or a base64 data URI.")
        return v

class Education(BaseModel):
    institution: str
    degree: str
    start_date: str
    end_date: str
    description: Optional[str] = None
    location: Optional[str] = None

class Experience(BaseModel):
    company: str
    position: str
    start_date: str
    end_date: str
    location: Optional[str] = None
    summary: Optional[str] = None
    description: List[str]

class Skill(BaseModel):
    name: str

class CVData(BaseModel):
    personal_info: PersonalInfo
    education: List[Education]
    experience: List[Experience]
    skills: List[Skill]
    languages: Optional[List[str]] = []
    template_name: Literal["template1", "template2", "template3"] = "template1"
    language: str = "en"

    class Config:
        extra = "ignore"
