from google.genai import types

generation_config = types.GenerateContentConfig(
    temperature=0.2,
    top_p=0.5,
    top_k=10,
    max_output_tokens=3000
)
