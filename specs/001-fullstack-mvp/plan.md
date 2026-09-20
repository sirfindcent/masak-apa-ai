# Masak Apa Full-Stack MVP — Implementation Plan

## Architecture

The application will use a simple full-stack architecture:

```text
User
  ↓
Next.js + TypeScript frontend
  ↓
POST /api/suggestions
  ↓
FastAPI backend
  ↓
Hosted LLM API
  ↓
Structured JSON response
  ↓
Recipe cards
```

## Frontend

Technology:

- Next.js
- TypeScript
- Tailwind CSS

Responsibilities:

- Accept comma-separated ingredients
- Validate empty input
- Send ingredients to the backend
- Show loading state
- Show error state
- Display returned recipes as cards

## Backend

Technology:

- FastAPI
- Python
- Pydantic

Endpoint:

`POST /api/suggestions`

Responsibilities:

- Receive ingredient list
- Validate request data
- Build the recipe-generation prompt
- Call the LLM provider
- Return structured recipe JSON
- Handle provider errors safely

## AI Integration

Production will use a hosted LLM API.

The API key will:

- exist only on the server
- be stored in an environment variable
- never be exposed to frontend code

The existing Ollama implementation will not be required for production.

## Deployment

The application will be deployed publicly.

Target:

- Vercel

Environment variables will be configured through the deployment platform.

## Project Structure

```text
masak-apa-ai/
│
├── frontend/
│   └── Next.js application
│
├── api/
│   └── FastAPI backend
│
├── specs/
│   └── 001-fullstack-mvp/
│       ├── spec.md
│       ├── plan.md
│       └── tasks.md
│
├── app.py
├── README.md
└── soto_ayam.md
```

The existing Streamlit application will remain temporarily during the migration.

## Testing

The MVP must verify:

1. Valid ingredients return recipe suggestions.
2. Empty ingredient input is rejected.
3. Loading state appears during generation.
4. Backend errors are shown to the user.
5. Backend returns structured recipe data.
6. Production API credentials are not exposed to the browser.

## Migration Strategy

1. Preserve the existing Streamlit application.
2. Build the new frontend separately.
3. Build the FastAPI backend.
4. Connect frontend to backend.
5. Replace local Ollama dependency with hosted LLM API.
6. Test the complete flow.
7. Deploy publicly.
8. Verify the implementation against `spec.md`.