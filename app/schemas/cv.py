from pydantic import BaseModel, EmailStr
from typing import List, Optional

class PersonalInfo(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None
    location: str
    website: Optional[str] = None
    linkedin: Optional[str] = None
    profile_picture: Optional[str] = None
    summary: str

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
    description: List[str]

class Skill(BaseModel):
    name: str

class CVData(BaseModel):
    personal_info: PersonalInfo
    education: List[Education]
    experience: List[Experience]
    skills: List[Skill]
    languages: Optional[List[str]] = []
    template_name: str = "template1"
    language: str = "en"

    class Config:
        extra = "ignore"
