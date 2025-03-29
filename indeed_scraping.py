import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

# ScraperAPI Key
API_KEY = "4316fc6257316b8086e8295fe87d3ecf"

# Function to construct the Indeed URL for each page
def get_url(position, location, page):
    base_url = "https://in.indeed.com/jobs?q={}&l={}&start={}"
    position = position.replace(" ", "+")
    location = location.replace(" ", "+")
    return base_url.format(position, location, page * 10)

# Function to scrape job details
def scrape_jobs(position, location, pages=50):
    all_jobs = []
    
    for page in range(pages):
        print(f"Scraping page {page + 1}...")

        # Request data using ScraperAPI
        url = get_url(position, location, page)
        response = requests.get(f"https://api.scraperapi.com/?api_key={API_KEY}&url={url}")

        if response.status_code != 200:
            print(f"Failed to fetch page {page + 1}. Status Code:", response.status_code)
            continue

        soup = bs(response.text, "html.parser")

        # Extract job cards
        job_cards = soup.find_all("div", class_="job_seen_beacon")

        if not job_cards:
            print(f"No jobs found on page {page + 1}. Stopping...")
            break  # Stop if no more jobs are found

        for job_card in job_cards:
            try:
                # Extract Job Title & Link
                title_tag = job_card.find("h2", class_="jobTitle")
                title = title_tag.text.strip() if title_tag else "N/A"
                job_link = "https://in.indeed.com" + title_tag.a["href"] if title_tag and title_tag.a else "N/A"

                # Extract Company Name
                company_tag = job_card.find("span", class_="css-1h7lukg")
                company = company_tag.text.strip() if company_tag else "N/A"

                # Extract Location
                location_tag = job_card.find("div", class_="companyLocation")
                job_location = location_tag.text.strip() if location_tag else location  # Default to user-input location

                # Extract Salary (Some jobs may not have salary details)
                salary_tag = job_card.find("div", class_="metadata salary-snippet-container")
                salary = salary_tag.text.strip() if salary_tag else "Not Disclosed"

                # Extract Rating (Some jobs may not have ratings)
                rating_tag = job_card.find("span", {"data-testid": "holistic-rating"})
                rating = rating_tag.get("aria-label").split()[0] if rating_tag else "Not Rated"

                # Store job details
                all_jobs.append([title, job_link, company, job_location, salary, rating])

            except Exception as e:
                print(f"Error extracting job: {e}")

        # Wait before the next request (Avoid detection)
        time.sleep(3)

    # Save data to CSV
    df = pd.DataFrame(all_jobs, columns=["Job Title", "Job Link", "Company", "Location", "Salary", "Rating"])
    df.to_csv("indeed_jobs.csv", index=False)
    
    print("Scraping Completed!")
    print(df.head())  # Print first 5 jobs

# Input job title and location
position = input("Enter the position you are looking for: ")
location = input("Enter the location you are looking for: ")
scrape_jobs(position, location, pages=70)  # Scrape 70 pages
