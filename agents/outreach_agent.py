import anthropic
from config import ANTHROPIC_API_KEY, CLAUDE_MODEL

client = anthropic.Anthropic(
    api_key=ANTHROPIC_API_KEY
)

def outreach_agent(company):

    prompt = f"""
    Write outreach email to:

    {company["name"]}

    Tone: professional
    """

    response = client.messages.create(

        model=CLAUDE_MODEL,

        max_tokens=300,

        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text