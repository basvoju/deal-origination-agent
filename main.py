from agents.orchestrator import run_pipeline

if __name__ == "__main__":

    companies = run_pipeline()

    for company in companies:

        print(company["name"])
        print(company["score"])
        print(company["report"])
        print(company["outreach"])