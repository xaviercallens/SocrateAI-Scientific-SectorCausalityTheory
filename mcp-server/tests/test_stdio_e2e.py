"""End-to-end: launch the real server over stdio with the official MCP client, list its tools, and call
three of them. This exercises the protocol path an agent actually uses, not only the Python functions."""
import asyncio
import json
import os
import sys
from pathlib import Path

from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

SRC = Path(__file__).resolve().parents[1] / "src"
EXPECTED_TOOLS = {"criterion", "list_cases", "get_case", "check_consistency", "search_theorems",
                  "get_theorem", "verify_theorem", "list_papers", "list_reproductions", "reproduce"}


def _payload(result):
    sc = getattr(result, "structured_content", None) or getattr(result, "structuredContent", None)
    if sc:
        return sc.get("result", sc) if isinstance(sc, dict) else sc
    return json.loads(result.content[0].text)


async def _session_run():
    params = StdioServerParameters(
        command=sys.executable, args=["-m", "sector_causality_mcp.server"],
        env={**os.environ, "PYTHONPATH": str(SRC)})
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = {t.name for t in (await session.list_tools()).tools}
            case = _payload(await session.call_tool("get_case", {"name": "montonen"}))
            repro = _payload(await session.call_tool("reproduce", {"name": "rcft_su2_level1"}))
            crit = _payload(await session.call_tool("criterion", {}))
            return tools, case, repro, crit


def test_stdio_roundtrip():
    tools, case, repro, crit = asyncio.run(_session_run())
    assert EXPECTED_TOOLS <= tools
    assert case["found"] and case["verdict"] == "not_forced"
    assert "ModularGroup.stabilizer_I" in case["mathlib_lemmas"]
    assert repro["ran"] and repro["passed"]
    assert crit["criterion"].startswith("A self-dual point pins a physical transition")
