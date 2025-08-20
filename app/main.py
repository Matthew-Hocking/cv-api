from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

# Basic health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "CV Portfolio API is running"}

@app.get("/")
async def root():
    return {
        "message": "Welcome to my CV Portfolio API",
        "docs": "/docs",
        "health": "/health"
    }

# For local development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)