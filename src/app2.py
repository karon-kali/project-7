# src/app.py

import os
import uuid
from flask import Flask, render_template, request, jsonify
from src.agent_service import deploy_agent

# Point Flask at the root-level templates/ and static/ folders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static'),
    static_url_path='/static'
)

# In-memory storage for agents and the API key
AGENTS = {}    # maps agent_id → {"purpose": str}
API_KEY = ""   # set via the settings screen

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/set_api_key', methods=['POST'])
def set_api_key():
    global API_KEY
    data = request.get_json()
    API_KEY = data.get('apiKey', '').strip()
    return jsonify(success=True)

@app.route('/create_agent', methods=['POST'])
def create_agent():
    data = request.get_json()
    purpose = data.get('purpose', '').strip()
    if not purpose:
        return jsonify(error="Purpose cannot be empty"), 400

    agent_id = str(uuid.uuid4())
    AGENTS[agent_id] = {"purpose": purpose}
    return jsonify(agent_id=agent_id)

@app.route('/deploy_agent', methods=['POST'])
def deploy_agent_route():
    data = request.get_json()
    agent_id = data.get('agent_id')

    if not API_KEY:
        return jsonify(error="API key not set"), 400
    agent = AGENTS.get(agent_id)
    if not agent:
        return jsonify(error="Agent not found"), 404

    try:
        result = deploy_agent(agent_id, agent["purpose"], API_KEY)
        return jsonify(result)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
