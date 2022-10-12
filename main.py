from cefpython3 import cefpython as cef
import platform, sys, json, os, subprocess
import urllib.request
import threading
import zipfile

def downloadworker(value):
    if value == "installGeforceNow":
        print('Warning: If this file is blocked, ask for an update.')
        url = 'https://download.nvidia.com/gfnpc/GeForceNOW-release.exe'
        urllib.request.urlretrieve(url, './apps/GeForceNOWinstaller.exe')
        subprocess.call("./apps/GeForceNOWinstaller.exe")
    if value == "installVsCode":
        print('Installing VScode...')
        url = 'https://az764295.vo.msecnd.net/stable/7f6ab5485bbc008386c4386d08766667e155244e/VSCode-win32-ia32-1.60.2.zip'
        urllib.request.urlretrieve(url, 'VSCode.zip')
        
        with zipfile.ZipFile("VSCode.zip", 'r') as zip_ref:
            zip_ref.extractall("/apps/vscode")
        subprocess.call("/apps/vscode/Code.exe")
    if value == "cmd":
        subprocess.call('start /wait python term.py', shell=True)

g_htmlcode = open("neonium.html", "r").read()

def main():
    check_versions()
    cef.Initialize()
    browser = cef.CreateBrowserSync(url=cef.GetDataUrl(g_htmlcode),
                                    window_title="Neonium")
    bindings = cef.JavascriptBindings()
    bindings.SetFunction("sendData", recieveData)
    browser.SetJavascriptBindings(bindings)
    cef.MessageLoop()
    del browser
    cef.Shutdown()

def recieveData(value):
    t = threading.Thread(target=downloadworker, args=[value])
    t.start()
        


def check_versions():
    ver = cef.GetVersion()
    print("[Neonium] CEFPython {ver}".format(ver=ver["version"]))
    print("[Neonium] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[Neonium] CEF {ver}".format(ver=ver["cef_version"]))
    print("[Neonium] Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))

if __name__ == '__main__':
    main()