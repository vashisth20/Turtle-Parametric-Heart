# Turtle-Parametric-Heart

This repository contains a small Turtle graphics script that draws a colorful parametric pattern.

Files
- run.py    : The script to run (uses Python's turtle and tkinter)
- requirements.txt : Notes on runtime requirements (no pip packages)
- README.md : This file with step-by-step instructions
- run.sh    : Helper shell script to install requirements and run (macOS/Linux)
- run.ps1   : Helper PowerShell script to install requirements and run (Windows)

Getting started (very explicit, for beginners)

macOS (recommended for devs)

1) Open Terminal (Cmd+Space, type Terminal, Enter).
2) Install Homebrew (if not installed):
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
3) Install pyenv and Tcl/Tk:
   brew update
   brew install pyenv tcl-tk pyenv-virtualenv
4) Configure shell for pyenv (run and restart Terminal):
   export PATH="$(brew --prefix pyenv)/bin:$PATH"
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"
5) Prepare build flags for Tcl/Tk (run before pyenv install):
   export LDFLAGS="-L$(brew --prefix tcl-tk)/lib"
   export CPPFLAGS="-I$(brew --prefix tcl-tk)/include"
   export PKG_CONFIG_PATH="$(brew --prefix tcl-tk)/lib/pkgconfig"
6) Install Python and create a venv (example 3.14.6):
   PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.14.6
   pyenv virtualenv 3.14.6 turtle-env
   pyenv local turtle-env
7) Install requirements and run:
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   python run.py

Windows (PowerShell)

1) Download and install Python from https://www.python.org/downloads/windows/ (check "Add Python to PATH").
2) Open PowerShell (Win, type PowerShell, Enter).
3) Run these commands (replace path as appropriate):
   cd C:\\path\\to\\Turtle-Parametric-Heart
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   python run.py

Linux (Debian/Ubuntu example)

1) Open a terminal and run:
   sudo apt update
   sudo apt install -y python3 python3-venv python3-pip python3-tk
2) Create and activate venv (optional):
   python3 -m venv .venv
   source .venv/bin/activate
3) Install requirements and run:
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   python run.py

Headless servers
- The script needs a display. Use xvfb on Linux:
  sudo apt install -y xvfb
  xvfb-run -s "-screen 0 1024x768x24" python run.py

Helper scripts
- make run.sh executable: chmod +x run.sh && ./run.sh
- run PowerShell on Windows: .\\run.ps1

If anything fails, copy-paste the exact error and someone can help.
