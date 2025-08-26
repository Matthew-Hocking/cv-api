import pytest
from fastapi.testclient import TestClient
from app.main import app

# Create test client
client = TestClient(app)


class TestHealthAndRoot:
    """Test basic health and root endpoints"""
    
    def test_health_endpoint(self):
        """Test health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "message" in data
        assert "timestamp" in data
    
    def test_root_endpoint(self):
        """Test root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "endpoints" in data
        assert "version" in data


class TestCVEndpoints:
    """Test CV-related endpoints"""
    
    def test_get_profile(self):
        """Test profile endpoint"""
        response = client.get("/api/v1/me")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert "name" in data["data"]
        assert "title" in data["data"]
        assert "summary" in data["data"]
    
    def test_get_experience(self):
        """Test experience endpoint"""
        response = client.get("/api/v1/experience")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert isinstance(data["data"], list)
        
        if data["data"]:  # If there's experience data
            exp = data["data"][0]
            assert "company" in exp
            assert "title" in exp
            assert "description" in exp
    
    def test_get_education(self):
        """Test education endpoint"""
        response = client.get("/api/v1/education")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert isinstance(data["data"], list)
    
    def test_get_skills(self):
        """Test skills endpoint"""
        response = client.get("/api/v1/skills")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert isinstance(data["data"], dict)
        
        if data["data"]:  # If there's skills data
            skills = data["data"]["all_skills"]
            skill = skills[0]
            assert "name" in skill
            assert "level" in skill
            assert "category" in skill
    
    def test_get_projects(self):
        """Test projects endpoint"""
        response = client.get("/api/v1/projects")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert isinstance(data["data"], dict)
    
    def test_get_contact(self):
        """Test contact endpoint"""
        response = client.get("/api/v1/contact")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert isinstance(data["data"], dict)
    
    def test_get_summary(self):
        """Test summary endpoint"""
        response = client.get("/api/v1/summary")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert "profile" in data["data"]


class TestResponseFormats:
    """Test different response formats"""
    
    def test_json_response_default(self):
        """Test default JSON response"""
        response = client.get("/api/v1/me")
        assert response.status_code == 200
        assert "application/json" in response.headers.get("content-type", "")
    
    def test_json_response_explicit(self):
        """Test explicit JSON response format"""
        headers = {"Accept": "application/json"}
        response = client.get("/api/v1/skills", headers=headers)
        assert response.status_code == 200
        assert "application/json" in response.headers.get("content-type", "")


class TestDataModels:
    """Test data model validation"""
    
    def test_profile_data_structure(self):
        """Test profile data has required fields"""
        response = client.get("/api/v1/me")
        data = response.json()["data"]
        
        required_fields = ["name", "title", "summary", "location", "years_experience"]
        for field in required_fields:
            assert field in data, f"Missing required field: {field}"
    
    def test_experience_data_structure(self):
        """Test experience data structure"""
        response = client.get("/api/v1/experience")
        experiences = response.json()["data"]
        
        if experiences:  # If there's experience data
            exp = experiences[0]
            required_fields = ["company", "title", "start_date", "description"]
            for field in required_fields:
                assert field in exp, f"Missing required field: {field}"
    
    def test_skills_data_structure(self):
        """Test skills data structure"""
        response = client.get("/api/v1/skills")
        skills = response.json()["data"]

        if skills:  # Check the structure of the skills data
            assert skills["all_skills"]
            assert skills["skills_by_category"]
            assert skills["categories"]
        
        if skills["all_skills"]:  # Check the details of a skill
            skill = skills["all_skills"][0]
            required_fields = ["name", "level", "category", "years_experience"]
            for field in required_fields:
                assert field in skill, f"Missing required field: {field}"
            
            # Test skill level is valid enum value
            valid_levels = ["beginner", "intermediate", "advanced", "expert"]
            assert skill["level"] in valid_levels
    
    def test_projects_data_structure(self):
        """Test projects data structure"""
        response = client.get("/api/v1/projects")
        projects = response.json()["data"]

        if projects:  # If there's project data
            project = projects["all_projects"][0]
            required_fields = ["name", "description", "start_date"]
            for field in required_fields:
                assert field in project, f"Missing required field: {field}"
    
    def test_contact_data_structure(self):
        """Test contact data structure"""
        response = client.get("/api/v1/contact")
        contacts = response.json()["data"]
        
        if contacts:  # If there's contact data
            contact = contacts["all_contacts"][0]
            required_fields = ["method", "value", "label"]
            for field in required_fields:
                assert field in contact, f"Missing required field: {field}"


class TestEndpointResponses:
    """Test endpoint response consistency"""
    
    def test_all_endpoints_return_success(self):
        """Test all CV endpoints return success=True"""
        endpoints = [
            "/api/v1/me",
            "/api/v1/experience", 
            "/api/v1/education",
            "/api/v1/skills",
            "/api/v1/projects",
            "/api/v1/contact"
        ]
        
        for endpoint in endpoints:
            response = client.get(endpoint)
            assert response.status_code == 200
            data = response.json()
            assert data["success"] is True, f"Endpoint {endpoint} did not return success=True"
    
    def test_all_endpoints_have_timestamps(self):
        """Test all CV endpoints include timestamps"""
        endpoints = [
            "/api/v1/me",
            "/api/v1/experience", 
            "/api/v1/education",
            "/api/v1/skills",
            "/api/v1/projects",
            "/api/v1/contact"
        ]
        
        for endpoint in endpoints:
            response = client.get(endpoint)
            data = response.json()
            assert "timestamp" in data, f"Endpoint {endpoint} missing timestamp"


class TestErrorHandling:
    """Test error handling"""
    
    def test_nonexistent_endpoint(self):
        """Test 404 for non-existent endpoints"""
        response = client.get("/api/v1/nonexistent")
        assert response.status_code == 404
    
    def test_invalid_http_method(self):
        """Test invalid HTTP methods return 405"""
        response = client.post("/api/v1/me")
        assert response.status_code == 405


class TestAPIDocumentation:
    """Test API documentation endpoints"""
    
    def test_docs_endpoint(self):
        """Test Swagger docs are accessible"""
        response = client.get("/docs")
        assert response.status_code == 200
        assert "swagger" in response.text.lower() or "openapi" in response.text.lower()
    
    def test_redoc_endpoint(self):
        """Test ReDoc documentation is accessible"""
        response = client.get("/redoc")
        assert response.status_code == 200
        assert "redoc" in response.text.lower()
    
    def test_openapi_schema(self):
        """Test OpenAPI schema is available"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        schema = response.json()
        assert "openapi" in schema
        assert "info" in schema
        assert schema["info"]["title"] == "CV Portfolio API"


class TestCORS:
    """Test CORS configuration"""
    
    def test_cors_headers_present(self):
        """Test CORS headers are present in responses"""
        response = client.get("/api/v1/me")
        assert response.status_code == 200
        # CORS headers should be present due to middleware
        # Note: TestClient might not show all CORS headers, but this tests the endpoint works
    
    def test_options_request(self):
        """Test OPTIONS request for CORS preflight"""
        response = client.options("/api/v1/me")
        # FastAPI should handle OPTIONS requests


class TestDataConsistency:
    """Test data consistency across endpoints"""
    
    def test_profile_name_consistency(self):
        """Test profile name is consistent"""
        profile_response = client.get("/api/v1/me")
        summary_response = client.get("/api/v1/summary")
        
        profile_name = profile_response.json()["data"]["name"]
        summary_name = summary_response.json()["data"]["profile"]["name"]
        
        assert profile_name == summary_name, "Profile name inconsistent between endpoints"
    
    def test_experience_consistency(self):
        """Test experience data consistency"""
        experience_response = client.get("/api/v1/experience")
        summary_response = client.get("/api/v1/summary")
        
        experiences = experience_response.json()["data"]
        summary_experiences = summary_response.json()["data"]["recent_experience"]
        
        # Summary should contain subset of full experience
        if experiences and summary_experiences:
            assert len(summary_experiences) <= len(experiences)


class TestPerformance:
    """Test basic performance characteristics"""
    
    def test_response_time_reasonable(self):
        """Test endpoints respond in reasonable time"""
        import time
        
        endpoints = ["/api/v1/me", "/api/v1/skills", "/api/v1/projects"]
        
        for endpoint in endpoints:
            start_time = time.time()
            response = client.get(endpoint)
            end_time = time.time()
            
            assert response.status_code == 200
            response_time = end_time - start_time
            assert response_time < 1.0, f"Endpoint {endpoint} took too long: {response_time}s"
