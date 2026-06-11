import requests

def search_jobs_api(keyword):

    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
        "query": keyword,
        "page": "1",
        "num_pages": "1"
    }

    headers = {
        "X-RapidAPI-Key": "928f11ae6emsh1bc926864ef466fp1ec2b1jsn0c91fa441bb2",  #  replace this
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)

        data = response.json()

        jobs = []

        for item in data.get("data", []):
            jobs.append({
                "title": item.get("job_title"),
                "company": item.get("employer_name"),
                "location": item.get("job_city") or "Not specified"
            })

        return jobs

    except Exception as e:
        print("API ERROR:", e)
        return []