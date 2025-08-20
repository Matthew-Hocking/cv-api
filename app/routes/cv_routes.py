from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import Response
from typing import Union
import json
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

from app.models.cv_models import (
    ProfileResponse, ExperienceResponse, EducationResponse,
    SkillsResponse, ProjectsResponse, ContactResponse, ErrorResponse
)
from app.services.data_service import data_service

# Create router for CV endpoints
router = APIRouter(prefix="/api/v1", tags=["CV"])


def format_response_data(data: Union[dict, list], format_type: str = "json") -> Response:
    """Format response data as JSON or XML"""
    
    if format_type.lower() == "xml":
        # Convert to XML
        root = Element("response")
        
        def dict_to_xml(parent, data, item_name="item"):
            if isinstance(data, dict):
                for key, value in data.items():
                    child = SubElement(parent, str(key))
                    if isinstance(value, (dict, list)):
                        dict_to_xml(child, value)
                    else:
                        child.text = str(value)
            elif isinstance(data, list):
                for item in data:
                    child = SubElement(parent, item_name)
                    dict_to_xml(child, item)
            else:
                parent.text = str(data)
        
        # Convert the response data
        if hasattr(data, 'dict'):
            data_dict = data.dict()
        else:
            data_dict = data
            
        dict_to_xml(root, data_dict)
        
        # Pretty print XML
        xml_str = minidom.parseString(tostring(root)).toprettyxml(indent="  ")
        return Response(content=xml_str, media_type="application/xml")
    
    else:
        # Default JSON response
        if hasattr(data, 'dict'):
            json_data = data.dict()
        else:
            json_data = data
        return Response(
            content=json.dumps(json_data, default=str, indent=2),
            media_type="application/json"
        )


def get_response_format(request: Request) -> str:
    """Determine response format from Accept header"""
    accept_header = request.headers.get("accept", "application/json")
    if "application/xml" in accept_header or "text/xml" in accept_header:
        return "xml"
    return "json"


@router.get("/me", response_model=ProfileResponse)
async def get_profile(request: Request):
    """Get basic profile information"""
    try:
        profile = data_service.get_profile()
        response_data = ProfileResponse(data=profile)
        format_type = get_response_format(request)
        return format_response_data(response_data, format_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve profile: {str(e)}")


@router.get("/experience", response_model=ExperienceResponse)
async def get_experience(request: Request):
    """Get work experience information"""
    try:
        experiences = data_service.get_experiences()
        response_data = ExperienceResponse(data=experiences)
        format_type = get_response_format(request)
        return format_response_data(response_data, format_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve experience: {str(e)}")


@router.get("/education", response_model=EducationResponse)
async def get_education(request: Request):
    """Get education information"""
    try:
        education = data_service.get_education()
        response_data = EducationResponse(data=education)
        format_type = get_response_format(request)
        return format_response_data(response_data, format_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve education: {str(e)}")


@router.get("/skills", response_model=SkillsResponse)
async def get_skills(request: Request):
    """Get skills information"""
    try:
        skills = data_service.get_skills()
        response_data = SkillsResponse(data=skills)
        format_type = get_response_format(request)
        return format_response_data(response_data, format_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve skills: {str(e)}")


@router.get("/projects", response_model=ProjectsResponse)
async def get_projects(request: Request):
    """Get projects information"""
    try:
        projects = data_service.get_projects()
        response_data = ProjectsResponse(data=projects)
        format_type = get_response_format(request)
        return format_response_data(response_data, format_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve projects: {str(e)}")


@router.get("/contact", response_model=ContactResponse)
async def get_contact(request: Request):
    """Get contact information"""
    try:
        contact_info = data_service.get_contact_info()
        response_data = ContactResponse(data=contact_info)
        format_type = get_response_format(request)
        return format_response_data(response_data, format_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve contact info: {str(e)}")


# Summary endpoint that combines key information
@router.get("/summary")
async def get_summary(request: Request):
    """Get a summary of key CV information"""
    try:
        profile = data_service.get_profile()
        recent_experience = data_service.get_experiences()[:2]
        top_skills = [skill for skill in data_service.get_skills() if skill.level.value in ["expert", "advanced"]][:8]
        recent_projects = data_service.get_projects()[:3]
        
        summary_data = {
            "success": True,
            "data": {
                "profile": profile,
                "recent_experience": recent_experience,
                "top_skills": top_skills,
                "recent_projects": recent_projects
            }
        }
        
        format_type = get_response_format(request)
        return format_response_data(summary_data, format_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve summary: {str(e)}")