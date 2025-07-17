# MCP Servers Streamable

A simple Model Context Protocol (MCP) server implementation using FastMCP with streamable HTTP transport.

## Overview

This project provides a basic MCP server that exposes mathematical operations and greeting functionality through the Model Context Protocol. It uses the FastMCP framework and operates over streamable HTTP transport, making it suitable for integration with MCP-compatible clients.

## Features

The server provides the following tools:

- **greeting**: Greet users by name
- **add**: Add two integers
- **subtract**: Subtract two integers

## Requirements

- Python 3.11 or higher
- MCP CLI package

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mcp-servers-streamable
```

2. Install dependencies using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install mcp[cli]>=1.11.0
```

## Usage

### Running the Server

Start the MCP server:

```bash
uv run server.py
```

Or alternatively:

```bash
python server.py
```

The server will start and listen for connections using the streamable HTTP transport.

### Testing the Server

You can test the streamable protocol using the MCP development tools:

```bash
mcp dev
```

This will help you verify that the server is properly running and accessible via the streamable HTTP transport.

### Available Tools

#### greeting(name: str) -> str
Greets the user by name.

**Parameters:**
- `name` (str): The name of the user to greet

**Example:**
```python
greeting("Alice")  # Returns: "Hello, Alice!"
```

#### add(a: int, b: int) -> int
Adds two integers.

**Parameters:**
- `a` (int): First integer
- `b` (int): Second integer

**Example:**
```python
add(5, 3)  # Returns: 8
```

#### subtract(a: int, b: int) -> int
Subtracts the second integer from the first.

**Parameters:**
- `a` (int): Integer to subtract from
- `b` (int): Integer to subtract

**Example:**
```python
subtract(10, 4)  # Returns: 6
```

## Development

### Project Structure

```
mcp-servers-streamable/
├── server.py          # Main MCP server implementation
├── main.py           # Entry point placeholder
├── pyproject.toml    # Project configuration
├── uv.lock          # Dependency lock file
└── README.md        # This file
```

### Adding New Tools

To add new tools to the server, define them in `server.py` using the `@mcp.tool()` decorator:

```python
@mcp.tool()
def your_tool(param: type) -> return_type:
    """
    Description of your tool
    Args:
        param: Description of parameter
    """
    # Your implementation here
    return result
```

### Running in Development

For development, you can run the server using uv:

```bash
uv run server.py
```

Or directly with Python:

```bash
python server.py
```

## MCP Integration

This server is designed to work with MCP-compatible clients. The streamable HTTP transport allows for real-time communication and is suitable for various integration scenarios.

### Using with Cursor

To use this server with Cursor, add the following configuration to your MCP settings:

```json
{
  "mcpServers": {
    "my-streamable-server": {
      "transport": "http",
      "url": "http://127.0.0.1:8000/mcp"      
    }
  }
}
```

Make sure the server is running with `uv run server.py` before connecting from Cursor.

### Using with Claude Desktop

To use this server with Claude Desktop, add the following to your Claude Desktop MCP configuration file:

```json
{
  "mcpServers": {
    "my-streamable-server": {
      "command": "uv",
      "args": ["run", "server.py"],
      "cwd": "/path/to/your/mcp-servers-streamable"
    }
  }
}
```

Replace `/path/to/your/mcp-servers-streamable` with the actual path to your project directory. Claude Desktop will automatically start and manage the server process.

#### Alternative: Using mcp-remote

If streamable HTTP transport is not supported, you can use the `mcp-remote` npm package as a bridge:

1. Install mcp-remote:
```bash
npm install -g mcp-remote
```

2. Start the server:
```bash
uv run server.py
```

3. Use mcp-remote to bridge the connection:
```bash
mcp-remote --url http://127.0.0.1:8000/mcp --allow-http
```

This provides compatibility for clients that don't directly support streamable HTTP transport.

### General MCP Client Integration

To connect other MCP clients to this server, configure them to use the streamable HTTP transport and point them to the server's endpoint at `http://127.0.0.1:8000/mcp`.

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
