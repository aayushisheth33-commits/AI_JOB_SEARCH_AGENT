import requests
from bs4 import BeautifulSoup

def search_jobs(keyword):
    url = f"https://www.indeed.com/jobs?q={keyword}&l="
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for job in soup.find_all("h2"):
        title = job.text.strip()
        jobs.append({"title": title})

    return jobs[:10]