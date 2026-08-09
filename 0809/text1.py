from google import genai

# client = genai.Client(api_key="AQ.Ab8RN6IYgL4wQF0dPwb_MC7P7GxOnurjx-d1e0l2LahZ2fPA_w")
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)