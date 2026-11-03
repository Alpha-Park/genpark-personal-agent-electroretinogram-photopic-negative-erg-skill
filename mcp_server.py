"""
MCP Server for Electroretinogram Photopic Negative Response (PhNR) Skill.
Exposes JSON-RPC Model Context Protocol tools for assessing retinal ganglion cell axon health and visual fatigue.
"""

import sys
import json
from typing import Dict, Any
from client import ElectroretinogramPhNRClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_phnr",
                "description": "Calculates ERG Photopic Negative Response (PhNR) amplitude, PhNR/b-wave ratio, and retinal ganglion cell integrity score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "b_wave_amplitude_uv": {
                            "type": "number",
                            "description": "Photopic ERG b-wave amplitude in microvolts (e.g. 115.0 uV)."
                        },
                        "phnr_amplitude_uv": {
                            "type": "number",
                            "description": "Photopic negative response amplitude in microvolts (e.g. 44.0 uV)."
                        },
                        "phnr_latency_ms": {
                            "type": "number",
                            "description": "Latency to PhNR trough in milliseconds (typically 65 - 85 ms).",
                            "default": 72.0
                        },
                        "a_wave_amplitude_uv": {
                            "type": "number",
                            "description": "Optional photoreceptor a-wave amplitude in microvolts."
                        }
                    },
                    "required": ["b_wave_amplitude_uv", "phnr_amplitude_uv"]
                }
            }
        ]
    }


def handle_request(client: ElectroretinogramPhNRClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_phnr":
            a_val = args.get("a_wave_amplitude_uv")
            if a_val is not None:
                a_val = float(a_val)

            res = client.evaluate_phnr(
                b_wave_amplitude_uv=float(args.get("b_wave_amplitude_uv", 110.0)),
                phnr_amplitude_uv=float(args.get("phnr_amplitude_uv", 42.0)),
                phnr_latency_ms=float(args.get("phnr_latency_ms", 72.0)),
                a_wave_amplitude_uv=a_val
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = ElectroretinogramPhNRClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
