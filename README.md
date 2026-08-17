# Setup

Clone repo and install dependencies:
```bash
git clone https://github.com/tonycpmeum/Global-to-Local-Transmission.git
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

API keys are loaded from `.env` file at the project root and are gitignored.

If you're running this notebook for the first time:
1. Create `.env` at project root
2. Copy `.env.example` to `.env`
3. Open `.env` and replace the placeholder with your own FRED API key
4. Restart the kernel if `.env` was created or edited after the kernel started