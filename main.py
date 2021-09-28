from cefpython3 import cefpython as cef
import platform, sys, json, os, subprocess
import urllib.request
import threading

def downloadworker(value):
    if value == "installGeforceNow":
        print('Warning: If this file is blocked, ask for an update.')
        url = 'https://download.nvidia.com/gfnpc/GeForceNOW-release.exe'
        urllib.request.urlretrieve(url, 'GeForceNOWinstaller.exe')
        subprocess.call("GeForceNOWinstaller.exe")

g_htmlcode = open("neonium.html", "r").read()

with open("apps.json", "r") as f:
    apps = json.load(f)
    f.close()

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
    print("[NEONIUM CORE] CEF Python {ver}".format(ver=ver["version"]))
    print("[NEONIUM CORE] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[NEONIUM CORE] CEF {ver}".format(ver=ver["cef_version"]))
    print("[NEONIUM CORE] Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))

if __name__ == '__main__':
    main()