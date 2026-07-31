# PowerShell helper to install requirements and run the turtle script
Set-StrictMode -Version Latest

# Change to script directory if invoked from elsewhere
# Run from this folder: .\run.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run.py
