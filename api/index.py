import sys
import os

# Robust path handling for Vercel
# Ensure the parent directory is in sys.path so we can find the 'backend' package
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Import the FastAPI app from the backend package
from backend.app.main import app
