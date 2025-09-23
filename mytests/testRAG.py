from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel

model = OpenAIServerModel(
        model_id="qwen3-30b-a3b-instruct-2507-mlx",
        api_base="http://localhost:1234/v1",  # replace with remote open-ai compatible server if necessary
        api_key="your-api-key",  # replace with API key if necessary
    )

# Initialize the search tool
search_tool = DuckDuckGoSearchTool()

agent = CodeAgent(
    model=model,
    tools=[search_tool],
)

# Example usage
agent.run(
    "Search for luxury superhero-themed party ideas, including decorations, entertainment, and catering."
)