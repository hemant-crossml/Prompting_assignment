"""
Creates a reusable Gemini client instance using the
Google GenAI SDK and an API key loaded from environment
variables via the cred module.

This client is used across the application to send
requests to Gemini models for text generation.
"""

from google import genai
from cred import GEMINI_API_KEY

# Initialize Gemini client with secure API key
Client= genai.Client(api_key=GEMINI_API_KEY)