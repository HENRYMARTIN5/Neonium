import sys
from os import system as cmd, path
import zipfile
try:
  import requests
except ImportError:
  cmd("\"" + path.realpath(sys.executable) + "\" -m ensurepip")
  cmd("\"" + path.realpath(sys.executable) + "\" -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org requests")
  import requests

link = "http://github.com/HENRYMARTIN5/Neonium/archive/refs/heads/main.zip"
file_name = "neonium.zip"

with open(file_name, "wb") as f:
  print("Downloading Neonium...")
  response = requests.get(link)
  f.write(response.content)

# now, unzip the downloaded file and put it in the user's home directory
print("Extracting %s" % file_name)
with zipfile.ZipFile(file_name, 'r') as zip_ref:
    zip_ref.extractall(path.expanduser("~"))

# remove the archive
print("Cleaning up...")
cmd("del " + file_name)

print("Creating venv...")
cmd("\"" + path.realpath(sys.executable) + "\" -m venv " + path.expanduser("~") + "/Neonium-main/venv")

print("Installing requirements...")
cmd(path.expanduser("~") + "/Neonium-main/venv/Scripts/python.exe -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r " + path.expanduser("~") + "/Neonium-main/requirements.txt")

print("Done! You can now run Neonium by running " + path.expanduser("~") + "/Neonium-main/venv/Scripts/python.exe " + path.expanduser("~") + "/Neonium-main/neonium.py")
