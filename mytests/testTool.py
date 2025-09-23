from smolagents import ToolCallingAgent, DuckDuckGoSearchTool, OpenAIServerModel

model = OpenAIServerModel(
        model_id="qwen3-30b-a3b-instruct-2507-mlx",
        api_base="http://localhost:1234/v1",  # replace with remote open-ai compatible server if necessary
        api_key="your-api-key",  # replace with API key if necessary
    )

agent = ToolCallingAgent(tools=[DuckDuckGoSearchTool()], model=model)

#agent.run("Search for the best music recommendations for a party at the Wayne's mansion")
#agent.run("Latest news about Nvidia and OpenAI")
agent.run("best price to buy RTX 6000 Pro 96GB")