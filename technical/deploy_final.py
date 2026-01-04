import os from huggingface_hub import HfApi, login, create_repo

# --- CONFIGURATION ---

# PASTE YOUR TOKEN BELOW inside the quotes

TOKEN = "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" REPO_ID =
"OstensibleParadox/recursive-lines"

# --- EXECUTION ---

print(f"--- AUTHENTICATING ---") login(token=TOKEN)

print(f"--- CREATING REPO: {REPO_ID} ---") \# This line fixes your
error. It creates the repo if it's missing. create_repo(repo_id=REPO_ID,
repo_type="dataset", exist_ok=True)

print(f"--- DEPLOYING ASSETS ---") api = HfApi()

api.upload_folder( folder_path=".", repo_id=REPO_ID,
repo_type="dataset", ignore_patterns=\[ ".git*",\
".DS_Store",\
"**pycache**",\
"*.pyc", "deploy_final.py" \] )

print(f"--- UPLOAD COMPLETE ---") print(f"Live at:
https://huggingface.co/datasets/{REPO_ID}")
