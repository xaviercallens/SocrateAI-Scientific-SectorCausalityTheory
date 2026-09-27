"""Co-deployment check: the official Python MCP client (the same SDK this repo's server uses) talks
to rusty-SUNDIALS' `sundials-mcp` server. Skipped unless SUNDIALS_MCP_BIN points at a built binary
(`cargo build --release -p sundials-mcp` in rusty-SUNDIALS)."""
import asyncio
import json
import os

import pytest
from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

BIN = os.environ.get("SUNDIALS_MCP_BIN")
pytestmark = pytest.mark.skipif(not BIN or not os.path.exists(BIN),
                                reason="set SUNDIALS_MCP_BIN to a built rusty-SUNDIALS sundials-mcp binary")


def _payload(result):
    sc = getattr(result, "structured_content", None) or getattr(result, "structuredContent", None)
    return sc if sc else json.loads(result.content[0].text)


def _is_error(result):
    return bool(getattr(result, "is_error", None) or getattr(result, "isError", None))


async def _run():
    async with stdio_client(StdioServerParameters(command=BIN, args=[])) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = {t.name for t in (await session.list_tools()).tools}
            ok = await session.call_tool("solve", {"problem": "robertson"})
            bad = await session.call_tool("solve", {"problem": "exponential", "rtol": 1e-9, "atol": 1e-12})
            pw = await session.call_tool("pgpe_run", {"initial": "plane_wave", "n": 32, "t_end": 1.0})
            return tools, ok, bad, pw


def test_python_client_against_rust_server():
    tools, ok, bad, pw = asyncio.run(_run())
    assert {"about", "list_problems", "solve", "pgpe_run"} <= tools
    assert not _is_error(ok) and _payload(ok)["checks"]["max_mass_conservation_deviation"] < 1e-6
    assert _is_error(bad) and _payload(bad)["ran"] is True          # solver failure is an error, not a partial pass
    assert _payload(pw)["checks"]["plane_wave_max_error_vs_exact"] < 1e-9
