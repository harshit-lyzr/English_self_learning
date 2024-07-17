# Lyzr English Self Learning App

## Introduction

The **Lyzr English Self Learning** app leverages the power of Lyzr Automata and OpenAI to facilitate self-learning of the English language using advanced text analysis techniques.

## Features

- **Input:** Allows users to input an article link.
- **Output:** Generates self-learning activities based on the provided article.
- **Functions:**
  - Analyzes the text for vocabulary, idiomatic expressions, and complex sentence structures.
  - Provides reading comprehension questions and practice exercises.
  - Offers long-term learning strategies and recommended reading for further improvement.

## Getting Started

To run the app locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/harshit-lyzr/English_self_learning
    cd English_self_learning

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
   
3. Set up your OpenAI API Key:
- Create a file named `.env` in the root directory.
- Add your OpenAI API Key to `.env`:

  ```
  OPENAI_API_KEY=<your_openai_api_key>
  ```

4. Run the app:
    ```bash
    streamlit run app.py

markdown
Copy code

## Usage

- Enter the article link in the input field.
- Click on the **Generate** button to initiate the analysis and learning activity generation.
- View the generated learning activities and recommendations based on the article.

