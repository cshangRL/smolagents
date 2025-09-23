from smolagents import CodeAgent, tool, OpenAIServerModel

# Tool to suggest a menu based on the occasion
@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion (str): The type of occasion for the party. Allowed values are:
                        - "casual": Menu for casual party.
                        - "formal": Menu for formal party.
                        - "superhero": Menu for superhero party.
                        - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."

model = OpenAIServerModel(
        model_id="qwen3-30b-a3b-instruct-2507-mlx",
        api_base="http://localhost:1234/v1",  # replace with remote open-ai compatible server if necessary
        api_key="your-api-key",  # replace with API key if necessary
    )

# Alfred, the butler, preparing the menu for the party
agent = CodeAgent(tools=[suggest_menu], model=model)

# Preparing the menu for the party
agent.run("Prepare a formal menu for the party.")
