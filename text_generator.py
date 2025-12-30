from typing import Optional, Union

from google.genai import types

from utils import *


def generate_text(client, model_name: str, system_prompt: str, user_prompt: str,
                 config: Optional[dict] = None,
                 use_self_consistency: bool = True)->str:
    """
    summary:
        Generate text from an LLM given a system prompt and user prompt, optionally including an image.
        Supports two modes: self-consistency (multiple samples + majority vote) or single-pass generation.

    args:
        client: LLM client instance used to call `client.models.generate_content(...)`.
        model_name (str): Model identifier/name to use for generation.
        system_prompt (str): High-level instruction that sets the assistant behavior (used in single-pass config).
        user_prompt (str): User input/question/task description to generate a response.
        config (Optional[dict]): Optional generation configuration passed to self-consistency generation.
        use_self_consistency (bool): If True, uses multi-sample generation and voting; if False, uses one call.

    return:
        str: Model output text (either the consensus result in self-consistency mode, or the single-pass response),
             or an error message when generation fails.
    """
    if use_self_consistency:
        output = self_consistent_generate(client, model_name, [user_prompt], config)
    else:
        # FIXED SINGLE-PASS: Initialize response before try
        response = None
        try:
            response = client.models.generate_content(model=model_name, contents=[user_prompt], config=config)
            output = response.text if response and response.text else "No response"
        except Exception as e:
            output = f"Single pass failed: {str(e)}"
    print_output(system_prompt, user_prompt, output)
    return output