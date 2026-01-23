# MCP Server[](#mcp-server "Link to this heading")

The module also provides a simple MCP server that allows remote control of R&S instruments without the need to install any VISA library on the agent side.

Note

Please be aware that you need Python >= 3.10 to run the MCP server.

```python
RsInstrument-mcp --host localhost --port 8000 --transport streamable-http
```

Extend the built-in tools with your own using this blueprint:

```python
 1from RsInstrument import RsInstrument
 2from RsInstrument.mcp import run, safe_tool
 3
 4
 5@safe_tool  # Decorator to catch and log exceptions and return them as error messages to the agent
 6def instrument_fancy_function(resource: str, opc_timeout: int = 5000) -> str:
 7    """My fancy function for RsInstrument MCP.
 8
 9    Args:
10        resource: The VISA resource string of the instrument.
11        opc_timeout: Timeout in milliseconds for the operation complete (OPC) query.
12            Default is 5000 ms.
13
14    Returns:
15        The response from the instrument.
16    """
17    with RsInstrument(resource) as inst:
18        inst.opc_timeout = opc_timeout
19        # your logic goes here
20        return "RsInstrument is awesome."
21
22
23if __name__ == "__main__":
24    run(
25        host="localhost",
26        port=8000,
27        transport="streamable-http",
28        tools=[
29            (
30                "Instrument-Fancy-SCPI",  # Tool name
31                "This is an awesome function",  # Tool description
32                instrument_fancy_function,  # Tool function
33            )
34        ],
35    )
```

After starting the server, you can access the tools at <http://localhost:8000/mcp>.