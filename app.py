import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from PIL import Image
from lyzr_automata.tasks.task_literals import InputType, OutputType
import base64

st.set_page_config(
    page_title="Lyzr English Self Learning",
    layout="wide",
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

api = st.sidebar.text_input("Enter Your OPENAI API KEY HERE", type="password")

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
}
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Lyzr English Self Learning")
st.markdown("## Welcome to the Lyzr English Self Learning!")
st.markdown(
    "This App Harnesses power of Lyzr Automata to Learn Eanglish by Your Self. You Need to input Article Link and it will craft Self Learning Activities.")


if api:
    openai_model = OpenAIModel(
        api_key=api,
        parameters={
            "model": "gpt-4-turbo-preview",
            "temperature": 0.2,
            "max_tokens": 1500,
        },
    )
else:
    st.sidebar.error("Please Enter Your OPENAI API KEY")


def privacy_policy_generator(article):
    english_agent = Agent(
        prompt_persona=f"You are an Expert in English.",
        role="English Tutor",
    )

    english_task = Task(
        name="English learning",
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=openai_model,
        agent=english_agent,
        log_output=True,
        instructions=f"""
        You are an advanced English language tutor. Your task is to help me improve my English by analyzing difficult articles I provide. Follow these steps for each article I submit:
        Perform an initial analysis of the text.
        Provide a vocabulary breakdown:
        List unfamiliar or advanced words
        For each word, give its definition, etymology, example sentences, synonyms, antonyms, and common collocations
        Analyze phrases and sentences:
        Identify idiomatic expressions, phrasal verbs, and complex sentence structures
        Explain their meanings, usage in different contexts, and provide simpler alternatives or paraphrases
        Offer grammar explanations for complex structures
        Explain any cultural, historical, or subject-specific references in the text.
        Provide 3-5 reading comprehension questions about the main ideas and key points.
        Highlight recurring language patterns, writing styles, or genre-specific vocabulary.
        Create practice exercises based on the text:
        Fill-in-the-blank sentences
        Matching exercises
        Sentence transformation tasks
        A short writing prompt using new vocabulary
        Suggest 2-3 long-term learning strategies to help retain and review the new language.
        Recommend 1-2 similar texts or articles for further reading and reinforcement.
        Always be prepared to engage in follow-up discussions, answer questions about the text, and adapt your explanations based on my needs and progress. Your goal is to systematically expand my vocabulary and improve my comprehension of complex English articles over time.
        
        Article Link: {article}
        """,
    )

    output = LinearSyncPipeline(
        name="Learn English",
        completion_message="Test Generated!",
        tasks=[
            english_task
        ],
        ).run()
    return output[0]['task_output']


article = st.text_input("Enter Article Link")

if st.button("Generate"):
    solution = privacy_policy_generator(article)
    st.markdown(solution)

