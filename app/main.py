from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from app.routes.cv_routes import router as cv_router
from app.models.cv_models import HealthResponse

# Create FastAPI instance
app = FastAPI(
    title="CV Portfolio API",
    description="A serverless API providing information about my professional background",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware for web access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include CV routes
app.include_router(cv_router)

# Basic health check endpoint
@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        message="CV Portfolio API is running"
    )

@app.get("/")
async def root():
    return {
        "message": "Welcome to my CV Portfolio API",
        "description": "A serverless REST API showcasing professional information",
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "profile": "/api/v1/me",
            "experience": "/api/v1/experience",
            "education": "/api/v1/education",
            "skills": "/api/v1/skills",
            "projects": "/api/v1/projects",
            "contact": "/api/v1/contact",
            "summary": "/api/v1/summary"
        },
        "features": [
            "JSON and XML response formats (use Accept header)",
            "Comprehensive API documentation",
            "Professional CV data endpoints",
            "Serverless-ready architecture"
        ]
    }

# For local development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)