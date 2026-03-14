from google import genai

# create client with API key
client = genai.Client(api_key="AIzaSyAWhwctMZcnTRs7IhnNCDyzBepHA0EZqTk")

topic = input("Enter research topic: ")

prompt = f"""
Write a short research report about {topic}.
Include:
- market overview
- key companies
- future trends
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)