"""
Exercise 3: Batch Processing
Process multiple items in a loop, collect results, and save to a file.

This example processes column names and suggests better naming conventions.
"""

import os
import json
from openai import OpenAI

# Sample data - column names that need to be renamed
# Format: {column_id: {"name": "current_name", "datatype": "type"}}
raw_data = {
    "column_1": {"name": "UserActive", "datatype": "boolean"},
    "column_2": {"name": "CreateDate", "datatype": "date"},
    "column_3": {"name": "LastLoginTime", "datatype": "timestamp"},
    "column_4": {"name": "EmailVerified", "datatype": "boolean"},
    "column_5": {"name": "UserCanEdit", "datatype": "boolean"},
    "column_6": {"name": "AccountCreation", "datatype": "timestamp"}
}

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("LLM_PROXY_API_KEY"),
    base_url=os.environ.get("LLM_PROXY_BASE_URL")
)

# Dictionary to store our results
results = {}

# Process each column in a loop
print(f"Processing {len(raw_data)} columns...\n")

for column_id, column_info in raw_data.items():
    print(f"Processing {column_id}: {column_info['name']}...")

    # Create a prompt asking the LLM to rename the column following best practices
    prompt = f"""You are a data engineer helping to standardize column names. Suggest a better name for this column following these rules:

RULES:
1. Use snake_case (lowercase with underscores)
2. For booleans: Start with a qualifier like "is_", "has_", "can_", "should_", or "was_"
3. For dates: End with "_date"
4. For timestamps: End with "_at"
5. Make the name clear, descriptive, and representative of the data it holds

Current column name: {column_info['name']}
Datatype: {column_info['datatype']}

Respond with ONLY the suggested column name, nothing else."""

    # Make the API call
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Store the result using the column ID as the key
    suggested_name = response.choices[0].message.content.strip()
    results[column_id] = {
        "original_name": column_info['name'],
        "datatype": column_info['datatype'],
        "suggested_name": suggested_name
    }

# Print the results in a readable format
print("\n" + "="*60)
print("COLUMN RENAMING SUGGESTIONS:")
print("="*60)
for column_id, result in results.items():
    print(f"\n{result['original_name']} ({result['datatype']})")
    print(f"  → {result['suggested_name']}")

# Also print as formatted JSON
print("\n" + "="*60)
print("FULL RESULTS (JSON):")
print("="*60)
print(json.dumps(results, indent=2))

# Write results to a file
output_file = "output.json"
with open(output_file, "w") as f:
    json.dump(results, f, indent=2)

print(f"\nResults saved to {output_file}")
