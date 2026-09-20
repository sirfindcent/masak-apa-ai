"use client";

import { FormEvent, useState } from "react";

type Recipe = {
  name: string;
  description: string;
  matchedIngredients: string[];
};

export default function Home() {
  const [ingredients, setIngredients] = useState("");
  const [recipes, setRecipes] = useState<Recipe[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    setError("");
    setRecipes([]);

    const ingredientList = ingredients
      .split(",")
      .map((ingredient) => ingredient.trim())
      .filter(Boolean);

    if (ingredientList.length === 0) {
      setError("Please enter at least one ingredient.");
      return;
    }

    setLoading(true);

    try {
      const apiUrl =
        process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

      const response = await fetch(`${apiUrl}/api/suggestions`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          ingredients: ingredientList,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to generate recipes.");
      }

      const data = await response.json();

      setRecipes(data.recipes);
    } catch {
      setError("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-orange-50 px-6 py-16">
      <div className="mx-auto max-w-3xl">
        <div className="mb-10 text-center">
          <h1 className="text-5xl font-bold text-gray-900">
            🍲 Masak Apa
          </h1>

          <p className="mt-4 text-lg text-gray-600">
            Enter the ingredients you have and discover Indonesian dishes you
            can make.
          </p>
        </div>

        <form
          onSubmit={handleSubmit}
          className="rounded-2xl bg-white p-6 shadow-sm"
        >
          <label
            htmlFor="ingredients"
            className="mb-2 block font-semibold text-gray-900"
          >
            What ingredients do you have?
          </label>

          <textarea
            id="ingredients"
            value={ingredients}
            onChange={(event) => setIngredients(event.target.value)}
            placeholder="chicken, rice, garlic, egg"
            rows={4}
            className="w-full rounded-xl border border-gray-300 p-4 text-gray-900 outline-none focus:border-orange-500"
          />

          {error && (
            <p className="mt-3 text-sm font-medium text-red-600">{error}</p>
          )}

          <button
            type="submit"
            disabled={loading}
            className="mt-4 w-full rounded-xl bg-orange-600 px-5 py-3 font-semibold text-white transition hover:bg-orange-700 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? "Finding recipes..." : "Find Recipes"}
          </button>
        </form>

        {recipes.length > 0 && (
          <section className="mt-10">
            <h2 className="mb-5 text-2xl font-bold text-gray-900">
              Recipe Suggestions
            </h2>

            <div className="space-y-4">
              {recipes.map((recipe, index) => (
                <article
                  key={`${recipe.name}-${index}`}
                  className="rounded-2xl bg-white p-6 shadow-sm"
                >
                  <h3 className="text-xl font-bold text-gray-900">
                    {recipe.name}
                  </h3>

                  <p className="mt-2 text-gray-600">{recipe.description}</p>

                  <div className="mt-4">
                    <p className="text-sm font-semibold text-gray-900">
                      Uses:
                    </p>

                    <div className="mt-2 flex flex-wrap gap-2">
                      {recipe.matchedIngredients.map((ingredient) => (
                        <span
                          key={ingredient}
                          className="rounded-full bg-orange-100 px-3 py-1 text-sm text-orange-800"
                        >
                          {ingredient}
                        </span>
                      ))}
                    </div>
                  </div>
                </article>
              ))}
            </div>
          </section>
        )}
      </div>
    </main>
  );
}