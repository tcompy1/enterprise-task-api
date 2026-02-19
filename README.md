# Enterprise Task API

A FastAPI-based REST API for task management, built as part of an 8-week learning curriculum.

## 📚 Day 1 - Introduction to REST APIs

### What I Built
- Basic FastAPI application with multiple endpoints
- Health check endpoint
- Greeting endpoint with POST method

### Endpoints

#### GET /
Returns a welcome message
\`\`\`json
{
  "message": "Welcome to Task API"
}
\`\`\`

#### GET /health
Health check endpoint
\`\`\`json
{
  "status": "healthy"
}
\`\`\`

#### GET /name
Returns my name
\`\`\`json
{
  "Name": "Trent"
}
\`\`\`

#### POST /greeting
Accepts a name and returns a personalized greeting
\`\`\`json
{
  "message": "Hello, {name}"
}
\`\`\`

## 🚀 Running the Application

1. Install dependencies:
\`\`\`bash
pip install fastapi uvicorn
\`\`\`

2. Run the server:
\`\`\`bash
uvicorn main:app --reload
\`\`\`

3. Access the API:
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs

## 📖 Learning Progress

- [x] Day 1: Introduction to REST APIs
- [ ] Day 2: FastAPI Deep Dive
- [ ] Day 3: Testing with Pytest
- [ ] Week 2: Database Design
- [ ] Week 3: Authentication
- [ ] Week 4: Authorization & CRUD
- [ ] Week 5: Testing
- [ ] Week 6: Advanced Features
- [ ] Week 7: Deployment
- [ ] Week 8: Documentation & Polish

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Language:** Python 3.x
- **Server:** Uvicorn

## 📝 Notes

This is Day 1 of an 8-week curriculum to build a production-ready enterprise task management API.
