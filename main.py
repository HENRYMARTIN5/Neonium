from cefpython3 import cefpython as cef
import platform
import sys


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
    print("Value sent from Javascript: "+value)

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