# How to run with uv:
#   uv run structured_output_tool.py
#
# Modify the smolagents dependency to point to the local smolagents repo or
# remove `@ file:///<path-to-smolagents>`
#
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "smolagents[mcp,litellm] @ file:///<path-to-smolagents>",
#   "pydantic",
# ]
# ///

from textwrap import dedent

from mcp import StdioServerParameters

from smolagents import CodeAgent, InferenceClientModel, LiteLLMModel, MCPClient  # noqa: F401
from smolagents import OpenAIServerModel

model = OpenAIServerModel(
        model_id="qwen3-30b-a3b-instruct-2507-mlx",
        api_base="http://localhost:1234/v1",  # replace with remote open-ai compatible server if necessary
        api_key="your-api-key",  # replace with API key if necessary
    )

def weather_server_script() -> str:
    """Return an inline MCP server script that exposes a weather tool."""
    return dedent(
        '''
        from pydantic import BaseModel, Field
        from mcp.server.fastmcp import FastMCP

        mcp = FastMCP("Weather Service")

        class WeatherInfo(BaseModel):
            location: str = Field(description="The location name")
            temperature: float = Field(description="Temperature in Celsius")
            conditions: str = Field(description="Weather conditions")
            humidity: int = Field(description="Humidity percentage", ge=0, le=100)

        @mcp.tool(
            name="get_weather_info",
            description="Get weather information for a location as structured data.",
        )
        def get_weather_info(city: str) -> WeatherInfo:
            """Get weather information for a city."""
            return WeatherInfo(
                location=city,
                temperature=22.5,
                conditions="partly cloudy",
                humidity=65
            )

        mcp.run()
        '''
    )


def main() -> None:
    # Configure your inference model
    # model = InferenceClientModel()

    # Start the Weather MCP server from an inline script in this same file
    serverparams = StdioServerParameters(command="python", args=["-c", weather_server_script()])

    # Bridge MCP tools into SmolAgents with structured outputs enabled
    with MCPClient(
        serverparams,
        structured_output=True,
    ) as tools:
        agent = CodeAgent(tools=tools, model=model)
        # Example query that encourages tool use and unit conversion
        agent.run("What is the temperature in Tokyo in Fahrenheit?")


if __name__ == "__main__":
    main()
