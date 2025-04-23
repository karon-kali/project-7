# agent_service.py

import requests

def deploy_agent(agent_id: str, purpose: str, api_key: str):
    """
    Calls your external AI/API to run the agent.
    Returns whatever the API returns (or raises on error).
    """
    url = "https://api.your-llm.com/run"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "agent_id": agent_id,
        "purpose": purpose
    }
    resp = requests.post(url, json=payload, headers=headers)
    resp.raise_for_status()
    return resp.json()
