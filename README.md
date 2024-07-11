## Getting Started

### Prerequisites
Before you begin, make sure you have the following installed on your machine:

- Python 3.11
- Git

### Clone the Repository
```bash
git clone https://github.com/Tojonirina33/help-me-back.git
```

### Set Up Virtual Environment
Navigate to the project directory and create a virtual environment.

```bash
cd backend
python3 -m venv env # Mac OS / Linux
python -m venv env # Windows
```

### Activate the Virtual Environment
```bash
source env/bin/activate # Mac OS / Linux
.\env\Scripts\activate # Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Environment Variables
Rename the env.example file to .env. This file contains environment variables used by the project. You may need to customize these variables based on your local configuration.

```bash
cd help_me
mv env.example .env  # Mac OS / Linux
ren env.example .env  # Windows
```

### Running the Project
```bash
python manage.py runserver
```

The project will be accessible at http://localhost:8000.