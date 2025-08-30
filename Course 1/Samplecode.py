import openai

openai.api_key = 'YOUR_API_KEY'

def generate_business_insights(text):
prompt = f"Extract three key business insights from the following data: {text}"
response = openai.Completion.create(
engine="text-davinci-003",
prompt=prompt,
max_tokens=100,
temperature=0.6
)
return response.choices.text.strip()

data_summary = "Sales increased by 15% in Q2 2025 with highest growth in the western region."
print(generate_business_insights(data_summary))
