from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
# export GEMINI_API_KEY=AIzaSyCh_mIfQy51Kt8mYZV5A5_I7bYsH9RDycY
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)