import pandas as pd
import sqlite3
from utils.scraper import ScrapperJobs

def main():
    searches = ["Python Developer", "Developer backend"]
    sites = ["indeed", "linkedIn"]
    results = 1000
    old = 120 # Ultimos 5 dias
    country = "argentina"

    scraper= ScrapperJobs()
    df = scraper.scraper_jobs(searches, sites, results, old, country)

    conn = sqlite3.connect('jobs.db')
    df.to_sql('jobs', conn, if_exists='replace', index=False)
    conn.close()

    df.to_csv('jobs.csv')

if __name__ == "__main__":
    main()