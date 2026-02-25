from pathlib import Path
import os
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

INPUT_PATH = Path(os.getenv("INPUT_PATH", "/app/data/input"))
OUTPUT_PATH = Path(os.getenv("OUTPUT_PATH", "/app/data/output"))
MODEL_NAME = "llama-3.3-70b-versatile"
EMBEDDING = 'all-mpnet-base-v2'
INDEX_FILE = OUTPUT_PATH / "vector_storage.index"
CHUNKS_FILE = "data/all_chunks.pkl"