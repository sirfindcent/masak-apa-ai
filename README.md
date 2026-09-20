# 🍲 Masak Apa AI

Masak Apa AI is a full-stack web application that recommends Indonesian dishes based on ingredients provided by the user.

Users enter ingredients they already have, and the application generates 3–5 recipe suggestions with a short description and matched ingredients.

🌐 **Live Demo:** https://masak-apa-ai.vercel.app

## Features

- Generate Indonesian recipe recommendations from user-provided ingredients
- Return 3–5 structured recipe suggestions
- Display recipe names, descriptions, and matched ingredients
- Validate empty ingredient input
- Show loading and error states
- Use structured AI responses with Pydantic
- Run automated backend tests
- Use GitHub Actions for CI/CD
- Deploy automatically to Vercel

## Architecture

```text
User
  ↓
Next.js + TypeScript
  ↓
POST /api/suggestions
  ↓
FastAPI
  ↓
Google Gemini API
  ↓
Structured JSON
  ↓
Recipe Cards
```

The frontend and backend are deployed together on Vercel.

## Tech Stack

### Frontend

- Next.js
- TypeScript
- Tailwind CSS

### Backend

- FastAPI
- Python
- Pydantic
- REST API

### AI

- Google Gemini API
- Gemini 3.5 Flash-Lite
- Structured JSON output
- Prompt engineering for Indonesian recipe generation

### DevOps

- GitHub Actions
- Vercel
- Pytest
- Git

## API

### `POST /api/suggestions`

Generates Indonesian recipe suggestions from a list of ingredients.

### Request

```json
{
  "ingredients": [
    "chicken",
    "rice",
    "garlic",
    "egg"
  ]
}
```

### Response

```json
{
  "recipes": [
    {
      "name": "Nasi Goreng Ayam",
      "description": "Indonesian chicken fried rice with garlic and egg.",
      "matchedIngredients": [
        "chicken",
        "rice",
        "garlic",
        "egg"
      ]
    }
  ]
}
```

## Project Structure

```text
masak-apa-ai/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
│
├── api/
│   ├── __init__.py
│   ├── index.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   └── app/
│   ├── package.json
│   └── package-lock.json
│
├── specs/
│   └── 001-fullstack-mvp/
│       ├── spec.md
│       ├── plan.md
│       └── tasks.md
│
├── tests/
│   └── test_api.py
│
├── vercel.json
└── README.md
```

## Development Process

Masak Apa AI was developed using a lightweight spec-driven development workflow.

```text
Specification
     ↓
Implementation Plan
     ↓
Task Breakdown
     ↓
Development
     ↓
Testing
     ↓
Deployment
```

The project specification defines the application requirements, API contract, acceptance criteria, and scope before implementation.

## CI/CD

GitHub Actions automatically validates and deploys the application.

### Continuous Integration

On pushes and pull requests:

```text
GitHub
  ↓
Backend Tests
  ↓
Frontend Production Build
```

The CI pipeline verifies:

- FastAPI backend tests
- Input validation
- API health endpoint
- Next.js production build

### Continuous Deployment

Pushes to `main` automatically trigger:

```text
GitHub Actions
      ↓
Vercel Build
      ↓
Production Deployment
```

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/sirfindcent/masak-apa-ai.git
cd masak-apa-ai
```

### 2. Create a Python virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install backend dependencies

```bash
pip install -r api/requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the FastAPI backend

```bash
uvicorn api.index:app --reload --port 8000
```

Backend:

```text
http://localhost:8000
```

API documentation:

```text
http://localhost:8000/docs
```

### 6. Run the Next.js frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:3000
```

## Testing

Run backend tests from the project root:

```bash
source .venv/bin/activate
python -m pytest
```

Run a production frontend build:

```bash
cd frontend
npm run build
```

## Deployment

The application is deployed to Vercel through GitHub Actions.

Every push to `main` triggers the deployment workflow:

```text
Push to main
     ↓
GitHub Actions CI
     ↓
GitHub Actions Deploy
     ↓
Vercel
```

Production environment variables are configured securely in Vercel and are not committed to the repository.

## Specification

The MVP specification is located in:

```text
specs/001-fullstack-mvp/
```

It includes:

- `spec.md` — application requirements and acceptance criteria
- `plan.md` — implementation architecture and technical plan
- `tasks.md` — implementation task breakdown

## Future Improvements

- Recipe knowledge base / RAG
- Ingredient substitutions
- Recipe detail pages
- Favorites and recipe history
- Additional Indonesian regional cuisines
- Improved recipe ranking based on ingredient match quality

## Author

**Vincent Jonathan**

GitHub: https://github.com/sirfindcent