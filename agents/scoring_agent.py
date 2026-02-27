import anthropic
from config import ANTHROPIC_API_KEY, CLAUDE_MODEL

client = anthropic.Anthropic(
    api_key=ANTHROPIC_API_KEY
)

def score_company(company):

    prompt = f"""
    Score this company from 1 to 10 for acquisition potential.

    Company:
    {company}

    Return only a number.
    """

    response = client.messages.create(

        model=CLAUDE_MODEL,

        max_tokens=10,

        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    score = float(
        response.content[0].text.strip()
    )

    return score


def scoring_agent(companies):

    for company in companies:

        score = score_company(company)

        company["score"] = score

    return companies