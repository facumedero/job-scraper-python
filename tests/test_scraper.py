import pandas as pd
from unittest.mock import patch
from utils.scraper import ScrapperJobs

@patch("utils.scraper.scrape_jobs")
def test_scraper_deduplicates_by_id(mock_scrape):
    mock_scrape.return_value = pd.DataFrame([
        {"id": "1", "title": "Python Dev"},
        {"id": "1", "title": "Python Dev"},  # duplicado
        {"id": "2", "title": "Backend Dev"},
    ])

    scraper = ScrapperJobs()
    df = scraper.scraper_jobs(["Python Developer"], ["indeed"], 10, 24, "USA")

    assert len(df) == 2
    assert set(df["id"]) == {"1", "2"}
