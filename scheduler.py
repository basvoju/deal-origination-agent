import schedule
import time
from agents.orchestrator import run_pipeline

def job():

    print("Running DOA pipeline")

    companies = run_pipeline()

    print(companies)


schedule.every().day.at("07:00").do(job)

while True:

    schedule.run_pending()

    time.sleep(60)