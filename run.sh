#!/usr/bin/env bash
set -euo pipefail

# Optional: initialize pyenv if available
if command -v pyenv >/dev/null 2>&1; then
  eval "$(pyenv init -)" || true
  eval "$(pyenv virtualenv-init -)" || true
fi

# Install requirements (no-op if file is comments)
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Run the script
python run.py
