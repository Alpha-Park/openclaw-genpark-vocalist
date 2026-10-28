# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Vocalist MCP Server
Exposes acoustic pitch detection and vocal stability tools via JSON-RPC 2.0 over STDIO.
"""

import sys
import json
from client import OpenClawGenParkVocalist

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "openclaw-genpark-vocalist", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "track_pitch_and_stability",
                        "description": "Analyzes audio signal buffer and extracts pitch (F0), jitter, and stability grade.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "duration_sec": {"type": "number", "description": "Duration of synthetic/input audio in seconds"}
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})

        if tool_name == "track_pitch_and_stability":
            voc = OpenClawGenParkVocalist()
            res = voc.track_pitch_and_stability(duration_sec=args.get("duration_sec", 1.0))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Tool '{tool_name}' not found"}}
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": f"Method '{method}' not supported"}}

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("MCP Server Discovery Test OK")
        v = OpenClawGenParkVocalist()
        test_res = v.track_pitch_and_stability()
        print(f"Test F0: {test_res['fundamental_frequency_f0_hz']} Hz")
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
