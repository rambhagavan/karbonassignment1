from model import probe_model_5l_profit
import json

# Load financial data from data.json
with open("data.json", "r") as file:
    content = file.read()
    data = json.loads(content)

# Analyze financial data and get flags
result = probe_model_5l_profit(data["data"])

# Print the result
print(result)
