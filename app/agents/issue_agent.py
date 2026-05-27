import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from app.agents.prompt_templates import ISSUE_ANALYZER_PROMPT
from app.core.config import GROQ_API_KEY, GROQ_MODEL


llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=GROQ_MODEL
)

prompt = ChatPromptTemplate.from_template(
    ISSUE_ANALYZER_PROMPT
)


async def analyze_issue_with_ai(title: str, body: str,similar_issues: str):

    chain = prompt | llm

    response = await chain.ainvoke({
        "title": title,
        "body": body or "No issue body provided",
        "similar_issues": similar_issues
        
    })

    cleaned_response = (
        response.content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned_response)