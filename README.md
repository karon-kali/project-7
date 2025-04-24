# Project-7

A Python Flask application with agent deployment functionality.

## Prerequisites

- Python 3.7+
- pip (Python package installer)
- Git

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/karon-kali/project-7.git
cd project-7
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate.bat
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
To deactivate anytime just use the `deactivate` command inside the virtual environment

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Run as a Module (Recommended)

From the project root directory:

```bash
python -m src.app2
```

This method properly resolves Python package imports.


## Project Structure

```
project-7/
├── env/                    # Virtual environment
├── src/                    # Source code
│   ├── __init__.py
│   ├── __pycache__/
│   ├── agent_service.py
│   ├── app.py
│   └── app2.py
├── static/                 # Static assets
│   ├── style.css
│   ├── style2.css
│   └── style3.css
├── templates/              # HTML templates
│   ├── index.html
│   ├── index2.html
│   └── index3.html
├── .gitignore
├── README.md
└── requirements.txt
```

## Troubleshooting

### Import Errors

If you encounter "No module named 'src'" errors, make sure you're:
- Running the application from the project root directory
- Using the recommended command: `python -m src.app2`
- Not directly executing the script with `python src/app2.py`