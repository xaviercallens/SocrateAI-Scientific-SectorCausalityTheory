"""stdio MCP server exposing the Sector Causality Theory: cases, criterion, theorems, kernel checks,
papers, and bounded reproductions. Logic lives in `core.py`; this file only registers tools."""
from __future__ import annotations

from mcp.server.mcpserver import MCPServer

from . import core
from .reproductions import DESCRIPTIONS

INSTRUCTIONS = (
    "Tools for reading, checking and reproducing the Sector Causality Theory (does a self-dual point cause "
    "a transition, or only relabel sectors?). Conventions: `ran: false` means a check did not execute -- "
    "never read it as a pass. A clean Lean axiom footprint certifies a proof, not that the statement is the "
    "right physics. Case verdicts are transcribed from papers/sector_thesis.tex Table 1; `check_consistency` "
    "re-derives them from the paper itself."
)

mcp = MCPServer(name="sector-causality", instructions=INSTRUCTIONS, version="0.1.0")


@mcp.tool(description="The theory's criterion, verbatim from the foundation paper.")
def criterion() -> dict:
    return {"criterion": core.CRITERION, "source": core.CRITERION_SOURCE}


@mcp.tool(description="All sixteen candidate cases with their verdicts (4 verdict kinds, plus open question "
                      "and two kinds of exclusion). Returns id, name, verdict, one-line reason.")
def list_cases() -> dict:
    data = core.load_cases()
    return {"cases": core.list_cases(data), "verdict_vocabulary": data["verdict_vocabulary"],
            "source": data["source"]}


@mcp.tool(description="One case in full: verdict, the paper's own wording, reason, citations (DOI/arXiv), "
                      "associated Lean modules, and caveats. Accepts an id (e.g. 'potts') or a unique substring.")
def get_case(name: str) -> dict:
    c = core.get_case(name)
    if c is None:
        return {"found": False, "reason": f"no unique case matches {name!r}",
                "ids": [x["id"] for x in core.load_cases()["cases"]]}
    return {"found": True, **c}


@mcp.tool(description="Re-derive every verdict from the paper's Table 1 and report any mismatch between what "
                      "this server serves and what the paper says.")
def check_consistency() -> dict:
    return core.check_cases_against_paper()


@mcp.tool(description="Search the Lean theorems in lean/ by keywords (all must match name, module, docstring "
                      "or statement).")
def search_theorems(query: str, limit: int = 25) -> dict:
    return {"query": query, "results": core.search_theorems(query, limit=limit)}


@mcp.tool(description="A Lean theorem's full statement (up to the top-level ':='), module, line and docstring. "
                      "Accepts a fully qualified name or a unique short name.")
def get_theorem(name: str) -> dict:
    t = core.get_theorem(name)
    return {"found": True, **t} if t else {"found": False, "reason": f"no unique theorem named {name!r}"}


@mcp.tool(description="Kernel-check one Lean module with `lake env lean`: errors, sorry warnings, and the "
                      "#print axioms footprint. Returns ran=false with a reason if the toolchain or Mathlib "
                      "cache is unavailable. Can take a minute or more.")
def verify_theorem(module: str) -> dict:
    return core.verify_module(module)


@mcp.tool(description="The theory's papers in papers/, with titles, roles and DOIs.")
def list_papers() -> dict:
    return {"papers": core.PAPERS}


@mcp.tool(description="List the bounded (seconds) reproductions available to `reproduce`.")
def list_reproductions() -> dict:
    return {"reproductions": DESCRIPTIONS}


@mcp.tool(description="Run a named, bounded reproduction in a subprocess (timeout 60 s) and return ran, "
                      "expected, observed, passed, and the Lean theorems or papers it corresponds to.")
def reproduce(name: str) -> dict:
    return core.run_reproduction(name)


def main() -> None:
    mcp.run("stdio")


if __name__ == "__main__":
    main()
