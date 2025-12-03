"""
Exercise 2: Dynamic Prompt Construction - MADLIBS EDITION!
Learn to build prompts dynamically using variables and f-strings.

This is a collaborative madlibs activity - have each person contribute one variable!
"""

import os
from openai import OpenAI

# MADLIBS TIME! Each person contributes one variable
# Feel free to make these as silly or creative as you want!

person_1_character_name = "bob"
person_2_place = "the moon"
person_3_object = "a moon rock"
person_4_adjective = "shiny"
person_5_profession = "astronaut"
person_6_animal = "a cat"
person_7_verb = "jumped"

# Construct a creative prompt using all 7 variables!
prompt = f"""Write a short, entertaining story (3-4 paragraphs) that includes ALL of these elements:
- A character named {person_1_character_name}
- The location: {person_2_place}
- An important object: {person_3_object}
- Something described as {person_4_adjective}
- A {person_5_profession}
- A {person_6_animal}
- Someone or something {person_7_verb}

Make it creative and fun!"""

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("LLM_PROXY_API_KEY"),
    base_url=os.environ.get("LLM_PROXY_BASE_URL")
)

# Show everyone what we're sending
print("=" * 60)
print("MADLIBS STORY GENERATOR")
print("=" * 60)
print(f"\nYour ingredients:")
print(f"  Character: {person_1_character_name}")
print(f"  Place: {person_2_place}")
print(f"  Object: {person_3_object}")
print(f"  Adjective: {person_4_adjective}")
print(f"  Profession: {person_5_profession}")
print(f"  Animal: {person_6_animal}")
print(f"  Verb: {person_7_verb}")
print(f"\nGenerating your story...\n")

# Make the API call with our madlibs prompt
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Extract and print the story
story = response.choices[0].message.content
print("=" * 60)
print("YOUR STORY:")
print("=" * 60)
print(story)
print("\n" + "=" * 60)
