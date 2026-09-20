# Masak Apa Full-Stack MVP

## Goal

Migrate Masak Apa from a local Streamlit application into a publicly accessible full-stack web application.

## User Story

As a user, I want to enter ingredients I already have and receive Indonesian recipe suggestions so I can decide what to cook.

## Requirements

1. The user can enter ingredients separated by commas.
2. Empty input must not be accepted.
3. The user can request recipe suggestions.
4. The system returns 3-5 Indonesian dishes.
5. Each suggestion contains:
   - dish name
   - short description
   - matched ingredients from the user's input
6. The interface shows a loading state while waiting.
7. The interface shows a friendly error if generation fails.
8. The deployed application must not require the user to install Ollama.
9. LLM credentials must remain on the server.

## API Contract

### Request

`POST /api/suggestions`

```json
{
  "ingredients": [
    "chicken",
    "rice",
    "garlic"
  ]
}
```

### Response

```json
{
  "recipes": [
    {
      "name": "Nasi Goreng Ayam",
      "description": "Indonesian chicken fried rice.",
      "matchedIngredients": [
        "chicken",
        "rice",
        "garlic"
      ]
    }
  ]
}
```

## Acceptance Criteria

- Valid ingredients return 3-5 Indonesian recipe suggestions.
- Empty input does not call the backend.
- A loading state appears while recipe suggestions are being generated.
- API errors are displayed clearly to the user.
- The frontend successfully communicates with the backend.
- Each recipe contains a name, short description, and matched ingredients.
- The application works from a public URL.
- The application does not require Ollama to be installed on the user's computer.
- No LLM API secret is exposed in frontend code.

## Out of Scope

The following features are not part of this MVP:

- Authentication
- User accounts
- Database
- Favorites
- Recipe history
- Image generation
- RAG
- Multiple pages
- Recipe ratings
- Social sharing