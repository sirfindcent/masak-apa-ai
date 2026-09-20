import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
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

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="LLM service is not configured.",
        )

    client = OpenAI(api_key=api_key)

    try:
        response = client.responses.parse(
            model="gpt-5.6-luna",
            input=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert Indonesian cooking assistant. "
                        "Suggest 3 to 5 Indonesian dishes that make practical "
                        "use of the user's available ingredients. "
                        "Keep each description to one sentence. "
                        "matchedIngredients must contain only ingredients "
                        "from the user's provided list. "
                        "Prefer recipes requiring minimal additional ingredients."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        "Available ingredients: "
                        + ", ".join(ingredients)
                    ),
                },
            ],
            text_format=RecipeResponse,
        )

        result = response.output_parsed

        if result is None:
            raise ValueError("Model did not return structured recipe data.")

        return result

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Recipe generation failed. Please try again.",
        )