from smolagents import CodeAgent, OpenAIServerModel
import numpy as np
import time
import datetime

model = OpenAIServerModel(
        model_id="qwen3-30b-a3b-instruct-2507-mlx",
        api_base="http://localhost:1234/v1",  # replace with remote open-ai compatible server if necessary
        api_key="your-api-key",  # replace with API key if necessary
    )

agent = CodeAgent(tools=[], model=model, additional_authorized_imports=['datetime'])

agent.run(
    """
    Alfred needs to prepare for the party. Here are the tasks:
    1. Prepare the drinks - 30 minutes
    2. Decorate the mansion - 60 minutes
    3. Set up the menu - 45 minutes
    4. Prepare the music and playlist - 45 minutes

    If we start right now, at what time will the party be ready?
    """
)