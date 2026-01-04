import os
from huggingface_hub import HfApi, login, create_repo

# --- CONFIGURATION ---

TOKEN = os.environ.get("HF_TOKEN")
if not TOKEN:
    raise ValueError("HF_TOKEN environment variable not set. Export it before running.")

REPO_ID = "OstensibleParadox/recursive-lines"

# --- EXECUTION ---

print("--- AUTHENTICATING ---")
login(token=TOKEN)

print(f"--- CREATING REPO: {REPO_ID} ---")
create_repo(repo_id=REPO_ID, repo_type="dataset", exist_ok=True)

print("--- DEPLOYING ASSETS ---")
api = HfApi()

api.upload_folder(
    folder_path=".",
    repo_id=REPO_ID,
    repo_type="dataset",
    ignore_patterns=[
        ".git*",
        ".DS_Store",
        "__pycache__",
        "*.pyc",
        "deploy_final.py"
    ]
)

print("--- UPLOAD COMPLETE ---")
print(f"Live at: https://huggingface.co/datasets/{REPO_ID}")
