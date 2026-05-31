import os
import requests

def analyze_repo(repo):

    url = f"https://api.github.com/repos/{repo}"

    headers = {
    "User-Agent": "GitHub-Repository-Analyzer",
    "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"
    }

    response = requests.get(url, headers=headers)

    print("Status Code:", response.status_code)
    print("Response:", response.text[:200])

    if response.status_code != 200:
        return None

    data = response.json()

    score = 0

    if data["stargazers_count"] > 10000:
        score += 40
    elif data["stargazers_count"] > 1000:
        score += 25
    else:
        score += 10

    if data["forks_count"] > 1000:
        score += 25
    elif data["forks_count"] > 100:
        score += 15
    else:
        score += 5

    if data["open_issues_count"] < 100:
        score += 20
    elif data["open_issues_count"] < 1000:
        score += 10
    else:
        score += 5

    if data["description"]:
        score += 15

    # Top Contributors
    contributors_url = data["contributors_url"]

    contributors = requests.get(
        contributors_url,
        headers=headers
    ).json()

    top_contributors = []

    for contributor in contributors[:5]:
        top_contributors.append({
            "name": contributor["login"],
            "contributions": contributor["contributions"]
        })

    # Languages
    languages_url = data["languages_url"]

    languages = requests.get(languages_url, headers=headers).json()

    language_data = []

    total = sum(languages.values())

    sorted_languages = sorted(
    languages.items(),
    key=lambda x: x[1],
    reverse=True
    )

    for language, bytes_count in sorted_languages:

        percentage = round(
            (bytes_count / total) * 100,
            2
        )

        if percentage < 0.1:
            continue

        language_data.append({
            "language": language,
            "percentage": percentage
        })

    created_at = data["created_at"][:10]
    updated_at = data["updated_at"][:10]

    topics = data.get("topics", [])

    html_url = data["html_url"]

    return {
        "name": data["name"],
        "owner": data["owner"]["login"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "language": data["language"],
        "description": data["description"],
        "health_score": score,
        "contributors": top_contributors,
        "languages": language_data,
        "created_at": created_at,
        "updated_at": updated_at,
        "topics": topics,
        "html_url": html_url
    }