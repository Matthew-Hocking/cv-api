# CV Portfolio API

A serverless REST API built with FastAPI and AWS that provides information about my professional background, skills, and projects.

## 🏗️ Architecture

- **API Framework**: FastAPI
- **Database**: AWS DynamoDB
- **Deployment**: AWS Lambda + API Gateway
- **Authentication**: AWS Cognito
- **CI/CD**: GitHub Actions
- **Cost**: Free (AWS Free Tier)

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Git
- AWS Account (for deployment)

### Local Development Setup

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/cv-portfolio-api.git
cd cv-portfolio-api
```

2. **Create and activate virtual environment:**
```bash
python -m venv cv-api-env
source cv-api-env/bin/activate  # On Windows: cv-api-env\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Run the development server:**
```bash
uvicorn app.main:app --reload
```

6. **Visit the API:**
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## 📚 API Documentation

### Available Endpoints

**Public Endpoints:**
- `GET /` - API information
- `GET /health` - Health check
- `GET /me` - Basic profile information
- `GET /experience` - Work experience
- `GET /education` - Education background
- `GET /skills` - Technical and soft skills
- `GET /projects` - Portfolio projects
- `GET /contact` - Contact information

**Admin Endpoints:** *(Coming Soon)*
- `POST /admin/auth` - Admin authentication
- `PUT /admin/{section}` - Update CV sections

## 🧪 Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=app

# Run tests in watch mode
pytest-watch
```

## 🚀 Deployment

*Deployment instructions will be added as we progress through the development phases.*

## 📁 Project Structure

```
cv-portfolio-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── models/              # Pydantic models
│   ├── routes/              # API route handlers
│   ├── services/            # Business logic
│   └── utils/               # Utility functions
├── tests/                   # Test files
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # Project documentation
```

## 🛠️ Development Status

- [x] Project setup and structure
- [x] Basic FastAPI application
- [x] CV data models
- [x] API endpoints implementation
- [ ] Database integration
- [ ] Authentication system
- [ ] AWS deployment
- [ ] CI/CD pipeline

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact

For questions about this API or to discuss opportunities, please use the contact endpoints or visit my profile.

---

*This project is built as a learning exercise to demonstrate modern serverless development practices with AWS.*