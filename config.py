import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

DB_URL = "postgresql://user:password@localhost:5432/doa"

EMBEDDING_MODEL = "text-embedding-3-small"
CLAUDE_MODEL = "claude-3-5-sonnet-20241022"