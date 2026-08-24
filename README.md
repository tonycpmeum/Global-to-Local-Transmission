# Setup

Clone repo and install dependencies:
```bash
git clone https://github.com/tonycpmeum/Global-to-Local-Transmission.git
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

API keys are loaded from `.env` file at the project root.
If you're running this notebook for the first time:
1. `cp .env.example .env` - Duplicate `.env.example` as `.env`
2. Open `.env` and replace the placeholder with your own FRED API key
3. **Restart the kernel:** if `.env` was created or edited after starting your notebook.