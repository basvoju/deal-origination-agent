def enrichment_agent(companies):

    enriched = []

    for company in companies:

        company["industry"] = "AI"
        company["employees"] = "unknown"

        enriched.append(company)

    return enriched