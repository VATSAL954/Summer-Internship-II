import openai

openai.api_key = 'YOUR_API_KEY'

def generate_dashboard_components(data_summary):
prompt = (
"Given the following business data summary, create a plan for a dashboard with the types "
"of charts and data segments that should be included:\n\n"
f"{data_summary}\n\nDashboard Plan:"
)
response = openai.Completion.create(
engine="text-davinci-003",
prompt=prompt,
max_tokens=150,
temperature=0.7,
top_p=1.0,
frequency_penalty=0.0,
presence_penalty=0.0,
stop=["\n\n"]
)
dashboard_plan = response.choices.text.strip()
return dashboard_plan

if name == "main":
summary = (
"In Q2 2025, total sales increased by 12% compared to Q1, with the western region "
"showing the highest growth. Top products are electronics and home appliances."
)
plan = generate_dashboard_components(summary)
print("Dashboard Plan:\n", plan)
