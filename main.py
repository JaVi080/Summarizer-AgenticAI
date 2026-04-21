
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from openai import OpenAI
client=OpenAI()
import os
import requests
import urllib.parse

api_key=os.getenv("SERPAPI_KEY")

# serpapi ---could not get for now 
def search_web(topic):
    url = f"https://serpapi.com/search.json?q={topic}&api_key={api_key}&engine=google"
    data = requests.get(url).json()

# as data is in this form --
# {
#   "organic_results": [
#     {
#       "title": "What is AI",
#       "link": "...",
#       "snippet": "Artificial Intelligence is..."
#     }
#   ]
# }
# so thats why ---hehehhehehe

    results = []
    for item in data.get("organic_results", [])[:5]:
      results.append(item["snippet"])
    return results

#for wikipedia
HEADERS = {
    "User-Agent": "WikiSummaryPrj/1.0 (javairialateef627@gmail.com)"  # ← Required by Wikipedia
}

def search_wikipedia(topic):

    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": topic,
        "format": "json"
    }

    data = requests.get(url, params=params, headers=HEADERS) 
    if data.status_code != 200:
        return f"Error fetching search results: HTTP {data.status_code}"
       
    response=data.json()

    if response["query"]["search"]:
        return response["query"]["search"][0]["title"]
    else:
      return None
     

# now fetching data from wikipedia
def fetch_content(page_title):
    page_title = page_title.replace(" ", "_")
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{page_title}"

    data = requests.get(url, headers=HEADERS)
    if data.status_code != 200:
        return f"Error fetching content: HTTP {data.status_code}"
       
    response=data.json()
    return response.get("extract", "No summary found")

#generating the content (General Mode)
def generate(topic):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Explain {topic} in simple terms"
    )

    # Implementation for generating content based on the topic
    return response.output[0].content[0].text

#summarizing the content
def summarize(content):

    # Implementation for summarizing the generated content
     response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"summarize this {content} into 5 bullet points"
    )
     return response.output[0].content[0].text

def save(summary,topic):
    # Implementation for saving the summary
    print(" Data found Now Saving the summary into file...")
    with open("summary.txt", "a") as file:
        file.write("\n\n" + topic + ":\n\n")
        file.write(summary)


# main data flow

print("Enter a topic fro summarization in file:")
topic =input()
switch = input("General Mode or Search Mode? (1/2): ")

if switch == "2":
    print("Searching the web for content...")
    page = search_wikipedia(topic)
    if not page:
        print("No relevant Wikipedia page found. Generating content instead...")
        content = generate(topic)
    else:
        content = fetch_content(page)

elif switch == "1":
    print("Generating content...")
    content=generate(topic)
else:
    print("Invalid input. Please enter 1 or 2.")
summary = summarize(content)
save(summary,topic)