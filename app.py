### TODO CREATE GIT REPO
### TODO Dont say the user
### Push to repo
### Readme

import streamlit as st
import ollama

# Set up the Streamlit page
st.set_page_config(page_title="Masak Apa", page_icon="🍲", layout="wide")
st.title("🍲 Masak Apa")
st.write("Tell me what ingredients you have, and I'll suggest some Indonesian dishes you can make!")

# --- Model Selection ---
selected_model = "deepseek-r1"

# --- Ingredient Input ---
ingredients = st.text_area(
    "Enter your ingredients, separated by commas:",
    placeholder="e.g., chicken, soy sauce, garlic, ginger, rice",
    height=100
)


# --- Generate Button and Response ---
if st.button("Get Recipe Suggestions") and selected_model:
    if ingredients:
        with st.spinner(f"Asking {selected_model} for ideas..."):
            try:
                # The prompt for the Ollama model
                prompt = f"""
                You are an expert Indonesian chef. Given the following ingredients: {ingredients}.

                Please suggest 3-5 Indonesian dishes I can make with these ingredients.
                For each dish, provide:
                1. The name of the dish.
                2. A brief, one-sentence description.
                3. A list of the main ingredients required from my list.

                Max 100 words.
                Straight to the point, and avoid unnecessary detail.
                Always answer in english.
                Do not include your thought process or any conversational text before the list of dishes.
                """

                # This generator function will yield chunks of the response as they come in.
                def stream_response():
                    stream = ollama.chat(
                        model=selected_model,
                        messages=[{'role': 'user', 'content': prompt}],
                        stream=True,
                    )
                    for chunk in stream:
                        # Get the content from the chunk
                        content = chunk['message']['content']
                        # Clean the content by removing the unwanted tags
                        cleaned_content = content.replace("<think>", "").replace("</think>", "")
                        # Only yield the content if it's not empty after cleaning
                        if cleaned_content:
                            yield cleaned_content
                        

                # Use st.write_stream to display the content as it's generated.
                st.subheader("Here are some ideas for you:")
                st.write_stream(stream_response)

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some ingredients.")

# --- Instructions and Footer ---
st.markdown("---")
st.header("How to Use This App")
st.markdown("""
1.  **Make sure Ollama is running:** This app connects to a local Ollama instance. You need to have Ollama installed and running on your computer.
2.  **Pull the model:** Make sure you have the `deepseek-r1` model installed. You can get it by running `ollama pull deepseek-r1` in your terminal.
3.  **Enter your ingredients:** Type the ingredients you have into the text box, separated by commas.
4.  **Click the button:** Press the "Get Recipe Suggestions" button and wait for the AI to generate ideas!
""")

