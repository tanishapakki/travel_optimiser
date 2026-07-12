

import logging
from typing import Any

from certifi import contents
from groq import APIConnectionError, APITimeoutError, Groq
from tenacity import before_sleep_log, retry, retry_if_exception_type, stop_after_attempt, wait_exponential


from app.core.llmconfig import get_llm_settings


logger = logging .getLogger(__name__)

settings =get_llm_settings()

client =Groq(api_key=settings.GROQ_API_KEY, timeout=settings.LLM_TIMEOUT_SECONDS, max_retries=0)

@retry(
    retry=retry_if_exception_type((APIConnectionError, APITimeoutError)),
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier =3,
                          min=1,
                          max=4),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)

def generate(messages:str | list[dict[str,Any]], 
             max_tokens:int = 1000, 
             system:str = None) -> str:
    """
    Generate a response from the LLM using the provided messages and parameters.

    Args:
        messages (str | list[dict[str, Any]]): The input messages for the LLM.
        max_tokens (int): Maximum number of tokens in the response.
        system (str): Optional system message to provide context for the LLM.
    Returns:
        str: The generated response from the LLM.
    """
    formatted_messages = list[dict[str, Any]]()
    if system:
        formatted_messages.append({"role": "system", "content": system})
    if isinstance(messages, str):
        formatted_messages.append({"role": "user", "content": messages})

    else:
        formatted_messages.extend(messages)
    
    response = client.chat.completions.create(
        model= settings.GROQ_MODEL,
        messages=formatted_messages,
        max_tokens= max_tokens
    )

    content = response.choices[0].message.content

    if content is None:
        raise ValueError("LLM returned empty content")
    
    return content