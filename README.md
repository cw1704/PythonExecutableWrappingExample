# PythonExecutableWrappingExample

# Setup

1. Make directory
	- `mkdir <projet_name>`
	
1. Environment setup
	
	For Window:
	1. Create a virtual environment
		- `python3 -m venv .venv`
	1. Activate the environment 
		- `.venv\Scripts\activate` (use standard terminal instead of powershell)
	
	For Linux:
	1. Create virtual environment
		- `python -m venv your-enc-name`
	1. Activate the environment
		- `source your-env-name/bin/activate`

1. Install pyinstaller
	- `pip install pyinstaller`


# Usage
- Build EXE in one file
	- `pyinstaller --clean --onefile <target_script> -n <exe_name>`
- See the exe in `./dist`
- Execute to create a `file.txt` if not exists