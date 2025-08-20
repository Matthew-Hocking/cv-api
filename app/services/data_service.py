from datetime import date
from typing import List
from app.models.cv_models import (
    Profile, Experience, Education, Skill, Project, ContactInfo,
    SkillLevel, ContactMethod
)


class DataService:
    """Mock data service for CV information - will be replaced with DynamoDB later"""
    
    def __init__(self):
        self._initialize_mock_data()
    
    def _initialize_mock_data(self):
        """Initialize mock CV data - replace with your actual information"""
        
        # Profile Data
        self.profile = Profile(
            name="Matthew Hocking",
            title="Full Stack Developer",
            summary="Passionate full stack developer with 4+ years of experience building scalable web applications using modern technologies.",
            location="Edinburgh, United Kingdom",
            years_experience=4,
            specialties=["TypeScript", "React", "Next.js", "Web Development"]
        )
        
        # Experience Data
        self.experiences = [
            Experience(
                id="exp1",
                company="Haunt Digital",
                title="Developer",
                location="Wellington, New Zealand",
                start_date=date(2022, 8, 1),
                end_date=date(2024, 10, 1),
                current=False,
                description="Developed and maintained 10+ full-stack applications for clients ranging from small businesses to government organisations and international companies.",
                achievements=[
                    "Built applications for large-scale, multi-agency projects across diverse industries",
                    "Delivered technical solutions that enhanced UX and SEO performance",
                    "Worked in Agile teams contributing to sprint planning and cross-functional communication",
                    "Liaised directly with clients to scope technical requirements and define project featuresDeveloped",
                    "Led a full stack re-platforming project, improving UX, SEO performance, and page loading speeds by 60%"
                ],
                technologies=["Next.js", "TypeScript", "Tailwind CSS", "GraphQL", "Algolia", "Silverstripe", "Docker", "Vercel"]
            ),
        ]
        
        # Education Data
        self.education = [
            Education(
                id="edu1",
                institution="Dev Academy Aotearoa",
                degree="Web Development Training Scheme",
                location="Wellington, New Zealand",
                start_date=date(2022, 6, 1),
                end_date=date(2022, 10, 1),
                current=False,
                credits="72",
                achievements=[
                    "Built web servers from scratch using Node.js and Express",
                    "Developed RESTful APIs and integrated third-party APIs",
                    "Implemented authentication systems including JWT and social login",
                    "Practiced test-driven development and conducted code reviews",
                    "Managed project workflows using Git, stand-ups, and sprint planningCoded",
                ]
            )
        ]
        
        # Skills Data
        self.skills = [
            # Programming Languages
            Skill(name="JavaScript", level=SkillLevel.ADVANCED, years_experience=4, category="Programming Languages"),
            Skill(name="TypeScript", level=SkillLevel.ADVANCED, years_experience=3, category="Programming Languages"),
            Skill(name="PHP", level=SkillLevel.BEGINNER, years_experience=2, category="Programming Languages"),
            Skill(name="Python", level=SkillLevel.BEGINNER, years_experience=0, category="Programming Languages"),
            
            # Frameworks & Libraries
            Skill(name="FastAPI", level=SkillLevel.BEGINNER, years_experience=0, category="Frameworks"),
            Skill(name="React", level=SkillLevel.ADVANCED, years_experience=4, category="Frameworks"),
            Skill(name="Node.js", level=SkillLevel.ADVANCED, years_experience=4, category="Frameworks"),
            Skill(name="Next.js", level=SkillLevel.ADVANCED, years_experience=2, category="Frameworks"),
            Skill(name="Vue.js", level=SkillLevel.INTERMEDIATE, years_experience=2, category="Frameworks"),
            Skill(name="Storybook", level=SkillLevel.BEGINNER, years_experience=2, category="Frameworks"),
            Skill(name="Express", level=SkillLevel.INTERMEDIATE, years_experience=2, category="Frameworks"),

            # API Design
            Skill(name="REST APIs", level=SkillLevel.ADVANCED, years_experience=4, category="APIs"),
            Skill(name="GraphQL", level=SkillLevel.ADVANCED, years_experience=2, category="APIs"),
            
            # Cloud & DevOps
            Skill(name="AWS", level=SkillLevel.BEGINNER, years_experience=0, category="Cloud & DevOps"),
            Skill(name="Docker", level=SkillLevel.INTERMEDIATE, years_experience=2, category="Cloud & DevOps"),
            Skill(name="Vercel", level=SkillLevel.ADVANCED, years_experience=2, category="Cloud & DevOps"),
            Skill(name="Google Cloud", level=SkillLevel.BEGINNER, years_experience=2, category="Cloud & DevOps"),
            
            # Databases
            Skill(name="PostgreSQL", level=SkillLevel.ADVANCED, years_experience=4, category="Databases"),
            Skill(name="Prisma", level=SkillLevel.INTERMEDIATE, years_experience=2, category="Databases"),
            Skill(name="Algolia", level=SkillLevel.ADVANCED, years_experience=2, category="Databases"),
            Skill(name="Supabase", level=SkillLevel.INTERMEDIATE, years_experience=1, category="Databases"),

            # Content Management Systems
            Skill(name="DatoCMS", level=SkillLevel.ADVANCED, years_experience=2, category="CMS"),
            Skill(name="Silverstripe", level=SkillLevel.INTERMEDIATE, years_experience=2, category="CMS"),
            Skill(name="StoryBlok", level=SkillLevel.BEGINNER, years_experience=1, category="CMS"),
            
            # Tools & Other
            Skill(name="Git", level=SkillLevel.ADVANCED, years_experience=4, category="Tools"),
            Skill(name="Docker", level=SkillLevel.INTERMEDIATE, years_experience=2, category="Tools"),
            Skill(name="Postman", level=SkillLevel.INTERMEDIATE, years_experience=3, category="Tools"),
        ]
        
        # Projects Data
        self.projects = [
            Project(
                id="proj1",
                name="CV Portfolio API",
                description="Serverless REST API built with FastAPI and AWS Lambda for showcasing professional information. Demonstrates modern cloud architecture and development practices.",
                technologies=["Python", "FastAPI", "AWS Lambda", "DynamoDB", "API Gateway", "GitHub Actions"],
                start_date=date(2025, 8, 1),
                end_date=None,
                current=True,
                url="https://api.placeholder.com",  # Replace with URL
                github_url="https://github.com/Matthew-Hocking/cv-api",
                highlights=[
                    "Built with 100% AWS Free Tier services",
                    "Automated CI/CD pipeline with GitHub Actions",
                    "Comprehensive test coverage with pytest",
                    "Auto-generated API documentation"
                ]
            ),
            Project(
                id="proj2",
                name="Skadi",
                description="Job tracking app with multiple list management and Kanban status tracking with detailed application entries.",
                technologies=["TypeScript", "React", "Supabase", "Vite", "Vercel"],
                start_date=date(2023, 8, 1),
                end_date=None,
                current=True,
                url="https://skadi-job-hunt.vercel.app/",
                github_url="https://github.com/Matthew-Hocking/skadi",
                highlights=[
                    "Multiple job tracking lists",
                    "Kanban status tracking",
                    "Drag-and-drop job organization",
                    "Google and Github auth providers",
                ]
            ),
        ]
        
        # Contact Data
        self.contact_info = [
            ContactInfo(
                method=ContactMethod.EMAIL,
                value="matthewhocking.dev@gmail.com",
                label="Email",
                primary=True
            ),
            ContactInfo(
                method=ContactMethod.LINKEDIN,
                value="https://www.linkedin.com/in/matthew-rsc-hocking/",
                label="LinkedIn",
                primary=False
            ),
            ContactInfo(
                method=ContactMethod.GITHUB,
                value="https://github.com/Matthew-Hocking",
                label="GitHub",
                primary=False
            ),
            ContactInfo(
                method=ContactMethod.WEBSITE,
                value="https://matthocking.vercel.app/",
                label="Portfolio Website",
                primary=False
            )
        ]
    
    # Service methods
    def get_profile(self) -> Profile:
        """Get profile information"""
        return self.profile
    
    def get_experiences(self) -> List[Experience]:
        """Get work experience"""
        return self.experiences
    
    def get_education(self) -> List[Education]:
        """Get education information"""
        return self.education
    
    def get_skills(self) -> List[Skill]:
        """Get skills information"""
        return self.skills
    
    def get_projects(self) -> List[Project]:
        """Get projects information"""
        return self.projects
    
    def get_contact_info(self) -> List[ContactInfo]:
        """Get contact information"""
        return self.contact_info


# Create singleton instance
data_service = DataService()