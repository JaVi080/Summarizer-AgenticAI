
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from openai import OpenAI
client=OpenAI()


def generate(topic):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Explain {topic} in simple terms"
    )

    # Implementation for generating content based on the topic
    return response.output[0].content[0].text

def summarize(content):

    # Implementation for summarizing the generated content
     response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"summarize this {content} into 5 bullet points"
    )
     return response.output[0].content[0].text

def save(summary,topic):
    # Implementation for saving the summary
    with open("summary.txt", "a") as file:
        file.write("\n" + topic + ":\n\n")
        file.write(summary)

print("Enter a topic to generate content:")
topic =input()
content = generate(topic)
summary = summarize(content)
save(summary,topic)