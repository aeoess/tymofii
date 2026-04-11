#!/usr/bin/env python3
"""Upload swarm.html to GitHub via API - reads base64 from stdin"""
import subprocess, json, sys

b64 = sys.stdin.read().strip()
payload = json.dumps({
    "message": "add: Clinical Swarm Intelligence Engine (67 autonomous agents)",
    "content": b64
})

result = subprocess.run(
    ["/Users/tima/.local/bin/gh", "api", "repos/aeoess/tymofii/contents/swarm.html",
     "--method", "PUT", "--input", "-"],
    input=payload, capture_output=True, text=True
)
print("Status:", "OK" if result.returncode == 0 else "FAIL")
if result.returncode != 0:
    print("Error:", result.stderr[:200])
else:
    data = json.loads(result.stdout)
    print("SHA:", data.get("content", {}).get("sha", "unknown")[:12])
