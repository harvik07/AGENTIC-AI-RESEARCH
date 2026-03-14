import google.generativeai as genai

genai.configure(api_key="AIzaSyDJskp_uUePpt1Q0uCWqSXa0NZ3WA_PtxM")

def create_plan(topic):

    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
    Break this research topic into 5 tasks.

    Topic: {topic}
    """

    response = model.generate_content(prompt)

    return response.text