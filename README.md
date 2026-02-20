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
```json
{
  "message": "Welcome to Task API"
}
```

#### GET /health
Health check endpoint
```json
{
  "status": "healthy"
}
```

#### GET /name
Returns my name
```json
{
  "Name": "Trent"
}
```

#### POST /greeting
Accepts a name and returns a personalized greeting
```json
{
  "message": "Hello, {name}"
}
```

## 🗄️ Part 2 - Database Integration (Complete)

### What I Built
- PostgreSQL database configuration with SQLAlchemy
- User model with authentication fields
- Task model with relationships
- Database initialization script

### Database Models

#### User Model
- Email-based authentication
- Password hashing support
- Role-based access control (user/admin roles)
- One-to-many relationship with tasks
- Automatic timestamp tracking

**Fields:**
- `id` - Primary key
- `email` - Unique, indexed
- `hashed_password` - Secure password storage
- `full_name` - User's full name
- `role` - User role (default: "user")
- `is_active` - Account status
- `created_at` - Account creation timestamp

#### Task Model
- Title, description, status, priority fields
- Foreign key relationship to users
- Automatic timestamps (created_at, updated_at)
- Cascade delete with user

**Fields:**
- `id` - Primary key
- `title` - Task title (indexed)
- `description` - Optional detailed description
- `status` - pending/in_progress/completed (indexed)
- `priority` - low/medium/high
- `owner_id` - Foreign key to users (indexed)
- `created_at` - Task creation timestamp
- `updated_at` - Last update timestamp

### Database Setup

1. **Created PostgreSQL database:**
   ```bash
   psql -U postgres
   CREATE DATABASE task_api_db;
   ```

2. **Configured SQLAlchemy connection** in `app/database.py`

3. **Defined models** with proper relationships:
   - User → Tasks (one-to-many)
   - Task → User (many-to-one)

4. **Created tables:**
   ```bash
   python create_db.py
   ```

### File Structure
```
enterprise-task-api/
├── main.py
├── create_db.py
└── app/
    ├── database.py
    └── models/
        ├── user.py
        └── task.py
```

## 🚀 Running the Application

1. Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

2. Run the server:
```bash
uvicorn main:app --reload
```

3. Access the API:
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs

## 📖 Learning Progress

### Tutorial Parts Completed
- [x] Part 1: Hello World API
- [x] Part 2: Add Database
- [ ] Part 3: Authentication
- [ ] Part 4: Protected Routes
- [ ] Part 5: Task CRUD
- [ ] Part 6: Testing
- [ ] Part 7: Docker
- [ ] Part 8: Documentation

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Language:** Python 3.11+
- **Server:** Uvicorn
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Database Driver:** psycopg2-binary

## 📝 Notes

Following the step-by-step tutorial to build a production-ready enterprise task management API with authentication, database integration, and comprehensive testing.

### Key Learnings (Part 2)
- Database design with proper relationships
- SQLAlchemy ORM configuration
- Model definitions with constraints and indexes
- Foreign key relationships and cascade behavior
- Database initialization and table creation
