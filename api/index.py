import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from google.genai import types
from pydantic import BaseModel


load_dotenv()

app = FastAPI(title="Masak Apa API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RecipeRequest(BaseModel):
    ingredients: list[str]


class Recipe(BaseModel):
    name: str
    description: str
    matchedIngredients: list[str]


class RecipeResponse(BaseModel):
    recipes: list[Recipe]


@app.get("/")
def health_check():
    return {"message": "Masak Apa API is running"}


@app.post("/api/suggestions", response_model=RecipeResponse)
def get_recipe_suggestions(request: RecipeRequest):
    ingredients = [
        ingredient.strip()
        for ingredient in request.ingredients
        if ingredient.strip()
    ]

    if not ingredients:
        raise HTTPException(
            status_code=400,
            detail="At least one ingredient is required.",
        )

    if not os.getenv("GEMINI_API_KEY"):
        raise HTTPException(
            status_code=500,
            detail="AI service is not configured.",
        )

    try:
        client = genai.Client()

        prompt = f"""
You are an expert Indonesian cooking assistant.

Available ingredients:
{", ".join(ingredients)}

Suggest 3 to 5 Indonesian dishes.

Requirements:
- Keep each description to one sentence.
- matchedIngredients must contain only ingredients supplied by the user.
- Prefer dishes requiring minimal additional ingredients.
- Always respond in English.
"""

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=RecipeResponse,
            ),
        )

        if not response.text:
            raise ValueError("Gemini returned an empty response.")

        return RecipeResponse.model_validate_json(response.text)

    except Exception as e:
        print("GEMINI ERROR:", repr(e))

        raise HTTPException(
            status_code=502,
            detail="Recipe generation failed. Please try again.",
        )