from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna", "os", "pypdf"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "hw-merge",
    options = options,
    version = "1.0",
    description = 'merges numerical PDFs into one PDF',
    executables = executables
)