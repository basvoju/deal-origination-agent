import anthropic
from config import ANTHROPIC_API_KEY, CLAUDE_MODEL

client = anthropic.Anthropic(
    api_key=ANTHROPIC_API_KEY
)

def generate_report(company):

    prompt = f"""
    Create investment summary:

    Company:
    {company}

    Include:
    overview
    investment thesis
    risks
    """

    response = client.messages.create(

        model=CLAUDE_MODEL,

        max_tokens=500,

        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text


def report_agent(companies):

    for company in companies:

        report = generate_report(company)

        company["report"] = report

    return companies