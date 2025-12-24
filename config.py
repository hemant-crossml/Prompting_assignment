"""
config.py
---------
Centralized configuration for model selection,
system instructions, and generation parameters..
"""

from prompts import System_Prompt
from google.genai import types

# Model configuration
model_name = "gemini-2.5-flash"

# Generation configuration with system instruction
generation_config = types.GenerateContentConfig(
    system_instruction= System_Prompt,
    temperature=0.2,
    top_p=0.5,
    top_k=10,
    max_output_tokens=3000
)
