"""AI-helper/ai_engine/LLMclient.py"""
import logging
from openai import OpenAI
from typing import Optional, List, Dict, Any
#logger conf
logger = logging.getLogger(__name__)
#main class
class AIClient:
    def __init__(self, api_key: str, base_url: str, model: str):
        """Initialize an AIClient object.User need enter api_key and base_url, model for creating object"""
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            timeout=60,
        )
        logger.info(f"AI Client initialized. Model: {self.model}")
    def ask(self,
            prompt: Optional[str] = None,
            system_prompt: Optional[str] = None,
            messages: Optional[List[Dict[str, Any]]] = None,
            max_tokens: int = 1000,
            tools: Optional[List[Dict[str,Any]]] = None,
            **kwargs)->Any:
        """
                A universal method for making requests to an AI.
                :param prompt: The request text (can be empty if only a system_prompt is used)
                :param system_prompt: A system instruction (can be empty)
                :param max_tokens: Token limit (defaults to 1000)
                :param tools: A list of tools (functions) for the agent
                :param kwargs: Any other parameters (temperature, top_p, response_format, etc.)
                :return: The AI response object (message)
                """
        if not messages:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            if prompt:
                messages.append({"role": "user", "content": prompt})
            # Empty response for tests
            if not messages:
                messages.append({"role": "user", "content": ""})
        try:
            request_args ={
                "model":self.model,
                "messages":messages,
                "max_tokens":max_tokens,
                **kwargs
            }
            if tools:
                request_args["tools"] = tools
            response = self.client.chat.completions.create(**request_args)
            #return all responses
            return response.choices[0].message
        except Exception as e:
            logger.exception(f"AI API error: {e}")
            return None





