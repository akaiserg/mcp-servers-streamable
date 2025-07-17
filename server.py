from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="server", version="1.0.0")

@mcp.tool()
def greeting(name: str) -> str:
    """
    Greet the user by name
    Args:
        name: The name of the user to greet    
    """
    return f"Hello, {name}!"


@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b

if __name__ == "__main__":
    mcp.run(transport="streamable-http")