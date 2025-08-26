from datetime import date, datetime, timezone
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, HttpUrl, Field
from enum import Enum


class SkillLevel(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class ContactMethod(str, Enum):
    EMAIL = "email"
    PHONE = "phone"
    LINKEDIN = "linkedin"
    GITHUB = "github"
    WEBSITE = "website"


# Profile/Personal Information
class Profile(BaseModel):
    name: str = Field(..., description="Full name")
    title: str = Field(..., description="Current job title or professional title")
    summary: str = Field(..., description="Professional summary or bio")
    location: str = Field(..., description="Current location")
    years_experience: int = Field(..., description="Total years of professional experience")
    specialties: List[str] = Field(default=[], description="Key areas of expertise")


# Experience/Work History
class Experience(BaseModel):
    id: str = Field(..., description="Unique identifier for this role")
    company: str = Field(..., description="Company name")
    title: str = Field(..., description="Job title")
    location: str = Field(..., description="Job location")
    start_date: date = Field(..., description="Start date")
    end_date: Optional[date] = Field(None, description="End date (null if current)")
    current: bool = Field(default=False, description="Whether this is current role")
    description: str = Field(..., description="Role description")
    achievements: List[str] = Field(default=[], description="Key achievements in this role")
    technologies: List[str] = Field(default=[], description="Technologies used")


# Education
class Education(BaseModel):
    id: str = Field(..., description="Unique identifier")
    institution: str = Field(..., description="School/University name")
    degree: str = Field(..., description="Degree type and field")
    location: str = Field(..., description="Institution location")
    start_date: date = Field(..., description="Start date")
    end_date: Optional[date] = Field(None, description="End date (null if ongoing)")
    current: bool = Field(default=False, description="Whether currently enrolled")
    credits: Optional[str] = Field(None, description="Credits if relevant")
    achievements: List[str] = Field(default=[], description="Academic achievements, honors")


# Skills
class Skill(BaseModel):
    name: str = Field(..., description="Skill name")
    level: SkillLevel = Field(..., description="Proficiency level")
    years_experience: int = Field(..., description="Years of experience with this skill")
    category: str = Field(..., description="Skill category (e.g., 'Programming', 'Cloud')")


# Projects
class Project(BaseModel):
    id: str = Field(..., description="Unique identifier")
    name: str = Field(..., description="Project name")
    description: str = Field(..., description="Project description")
    technologies: List[str] = Field(default=[], description="Technologies used")
    start_date: date = Field(..., description="Project start date")
    end_date: Optional[date] = Field(None, description="Project end date (null if ongoing)")
    current: bool = Field(default=False, description="Whether project is ongoing")
    url: Optional[HttpUrl] = Field(None, description="Project URL if available")
    github_url: Optional[HttpUrl] = Field(None, description="GitHub repository URL")
    highlights: List[str] = Field(default=[], description="Key project highlights")


# Contact Information
class ContactInfo(BaseModel):
    method: ContactMethod = Field(..., description="Contact method type")
    value: str = Field(..., description="Contact value (email, phone number, URL)")
    label: str = Field(..., description="Display label for this contact method")
    primary: bool = Field(default=False, description="Whether this is a primary contact method")


# Health Check Response
class HealthResponse(BaseModel):
    status: str
    message: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    version: str = "1.0.0"


# Admin Models (for later)
class AdminUpdateRequest(BaseModel):
    section: str = Field(..., description="Section to update (profile, experience, etc.)")
    data: Dict[str, Any] = Field(..., description="Data to update")