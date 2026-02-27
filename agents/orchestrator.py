from agents.source_agent import source_agent
from agents.enrichment_agent import enrichment_agent
from agents.scoring_agent import scoring_agent
from agents.report_agent import report_agent
from agents.outreach_agent import outreach_agent
from tools.crm_tool import save_to_crm


def run_pipeline():

    print("Fetching companies...")

    companies = source_agent()

    companies = enrichment_agent(companies)

    companies = scoring_agent(companies)

    companies.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    top_companies = companies[:5]

    top_companies = report_agent(top_companies)

    for company in top_companies:

        email = outreach_agent(company)

        company["outreach"] = email

        save_to_crm(company)

    return top_companies