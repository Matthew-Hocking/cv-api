from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Any

from app.services.data_service import data_service

# Create router for CV endpoints
router = APIRouter(prefix="/api/v1", tags=["CV"])


def create_success_response(data: Any, message: str = "Success") -> dict:
    """Create a standardized success response format"""
    return {
        "success": True,
        "message": message,
        "data": data
    }


def create_error_response(message: str, error_code: str = "INTERNAL_ERROR") -> dict:
    """Create a standardized error response format"""
    return {
        "success": False,
        "message": message,
        "error_code": error_code,
        "data": None
    }


@router.get("/me")
async def get_profile():
    """Get basic profile information"""
    try:
        profile = data_service.get_profile()
        # Convert Pydantic model to dict for consistent JSON serialization
        profile_dict = profile.model_dump(mode='json') if hasattr(profile, 'dict') else profile
        
        response_data = create_success_response(
            data=profile_dict,
            message="Profile retrieved successfully"
        )
        return JSONResponse(content=response_data)
        
    except Exception as e:
        error_response = create_error_response(
            message=f"Failed to retrieve profile: {str(e)}",
            error_code="PROFILE_FETCH_ERROR"
        )
        return JSONResponse(content=error_response, status_code=500)


@router.get("/experience")
async def get_experience():
    """Get work experience information"""
    try:
        experiences = data_service.get_experiences()
        # Convert list of Pydantic models to list of dicts
        experiences_dict = [
            exp.model_dump(mode='json') if hasattr(exp, 'dict') else exp 
            for exp in experiences
        ]
        
        response_data = create_success_response(
            data=experiences_dict,
            message=f"Retrieved {len(experiences_dict)} work experience entries"
        )
        return JSONResponse(content=response_data)
        
    except Exception as e:
        error_response = create_error_response(
            message=f"Failed to retrieve experience: {str(e)}",
            error_code="EXPERIENCE_FETCH_ERROR"
        )
        return JSONResponse(content=error_response, status_code=500)


@router.get("/education")
async def get_education():
    """Get education information"""
    try:
        education = data_service.get_education()
        education_dict = [
            edu.model_dump(mode='json') if hasattr(edu, 'dict') else edu 
            for edu in education
        ]
        
        response_data = create_success_response(
            data=education_dict,
            message=f"Retrieved {len(education_dict)} education entries"
        )
        return JSONResponse(content=response_data)
        
    except Exception as e:
        error_response = create_error_response(
            message=f"Failed to retrieve education: {str(e)}",
            error_code="EDUCATION_FETCH_ERROR"
        )
        return JSONResponse(content=error_response, status_code=500)


@router.get("/skills")
async def get_skills():
    """Get skills information"""
    try:
        skills = data_service.get_skills()
        skills_dict = [
            skill.model_dump(mode='json') if hasattr(skill, 'dict') else skill 
            for skill in skills
        ]
        
        # Group skills by category for better organization
        skills_by_category = {}
        for skill in skills_dict:
            category = skill.get('category', 'Other')
            # Convert category to snake_case for consistency
            category_key = category.lower().replace(' ', '_').replace('&', 'and')
            if category_key not in skills_by_category:
                skills_by_category[category_key] = []
            skills_by_category[category_key].append(skill)
        
        response_data = create_success_response(
            data={
                "skills_by_category": skills_by_category,
                "total_skills": len(skills_dict),
                "categories": list(skills_by_category.keys())
            },
            message=f"Retrieved {len(skills_dict)} skills across {len(skills_by_category)} categories"
        )
        return JSONResponse(content=response_data)
        
    except Exception as e:
        error_response = create_error_response(
            message=f"Failed to retrieve skills: {str(e)}",
            error_code="SKILLS_FETCH_ERROR"
        )
        return JSONResponse(content=error_response, status_code=500)


@router.get("/projects")
async def get_projects():
    """Get projects information"""
    try:
        projects = data_service.get_projects()
        projects_dict = [
            project.model_dump(mode='json') if hasattr(project, 'dict') else project 
            for project in projects
        ]
        
        # Separate current and past projects
        current_projects = [p for p in projects_dict if p.get('current', False)]
        past_projects = [p for p in projects_dict if not p.get('current', False)]
        
        response_data = create_success_response(
            data={
                "current_projects": current_projects,
                "past_projects": past_projects,
                "total_projects": len(projects_dict)
            },
            message=f"Retrieved {len(projects_dict)} projects ({len(current_projects)} current, {len(past_projects)} past)"
        )
        return JSONResponse(content=response_data)
        
    except Exception as e:
        error_response = create_error_response(
            message=f"Failed to retrieve projects: {str(e)}",
            error_code="PROJECTS_FETCH_ERROR"
        )
        return JSONResponse(content=error_response, status_code=500)


@router.get("/contact")
async def get_contact():
    """Get contact information"""
    try:
        contact_info = data_service.get_contact_info()
        contact_dict = [
            contact.model_dump(mode='json') if hasattr(contact, 'dict') else contact 
            for contact in contact_info
        ]
        
        # Separate primary and secondary contact methods
        primary_contacts = [c for c in contact_dict if c.get('primary', False)]
        secondary_contacts = [c for c in contact_dict if not c.get('primary', False)]
        
        response_data = create_success_response(
            data={
                "primary_contacts": primary_contacts,
                "secondary_contacts": secondary_contacts,
                "all_contacts": contact_dict
            },
            message=f"Retrieved {len(contact_dict)} contact methods"
        )
        return JSONResponse(content=response_data)
        
    except Exception as e:
        error_response = create_error_response(
            message=f"Failed to retrieve contact info: {str(e)}",
            error_code="CONTACT_FETCH_ERROR"
        )
        return JSONResponse(content=error_response, status_code=500)


@router.get("/summary")
async def get_summary():
    """Get a comprehensive summary of key CV information"""
    try:
        # Fetch all data
        profile = data_service.get_profile()
        all_experiences = data_service.get_experiences()
        all_skills = data_service.get_skills()
        all_projects = data_service.get_projects()
        contact_info = data_service.get_contact_info()
        
        # Convert to dicts
        profile_dict = profile.model_dump(mode='json') if hasattr(profile, 'dict') else profile
        
        # Get recent experience (last 2 positions)
        recent_experience = [
            exp.model_dump(mode='json') if hasattr(exp, 'dict') else exp 
            for exp in all_experiences[:2]
        ]
        
        # Get top skills (advanced/expert level, max 8)
        top_skills = [
            skill.model_dump(mode='json') if hasattr(skill, 'dict') else skill
            for skill in all_skills 
            if skill.level.value in ["expert", "advanced"]
        ][:8]
        
        # Get recent projects (last 3)
        recent_projects = [
            project.model_dump(mode='json') if hasattr(project, 'dict') else project
            for project in all_projects[:3]
        ]
        
        # Get primary contact info
        primary_contact = [
            contact.model_dump() if hasattr(contact, 'dict') else contact
            for contact in contact_info
            if contact.primary
        ]
        
        summary_data = {
            "profile": profile_dict,
            "recent_experience": recent_experience,
            "top_skills": top_skills,
            "recent_projects": recent_projects,
            "primary_contact": primary_contact,
            "stats": {
                "total_experience_entries": len(all_experiences),
                "total_skills": len(all_skills),
                "total_projects": len(all_projects),
                "years_experience": profile_dict.get("years_experience", 0)
            }
        }
        
        response_data = create_success_response(
            data=summary_data,
            message="CV summary retrieved successfully"
        )
        return JSONResponse(content=response_data)
        
    except Exception as e:
        error_response = create_error_response(
            message=f"Failed to retrieve summary: {str(e)}",
            error_code="SUMMARY_FETCH_ERROR"
        )
        return JSONResponse(content=error_response, status_code=500)