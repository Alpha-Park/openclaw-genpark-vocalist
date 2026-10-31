---
name: openclaw-genpark-vocalist
description: OpenClaw GenPark Vocalist - Pure standard library acoustic time-domain autocorrelation pitch tracker and vocal stability estimator.
category: Service
version: 1.0.0
license: MIT
tools:
  - execute_vocalist
---

# Openclaw Genpark Vocalist

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Openclaw Genpark Vocalist**.
Your primary directive is to execute: OpenClaw GenPark Vocalist - Pure standard library acoustic time-domain autocorrelation pitch tracker and vocal stability estimator.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `execute_vocalist`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `execute_vocalist`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
