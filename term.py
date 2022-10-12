from os import system as cmd, popen as pop

def prompt():
  print("" + pop("@echo %cd%").read().replace("\n", "") + "")
  command = input("> ")
  cmd(command)

print("Neonium Terminal")
print("Warning: 'cd' does not work. \n If it is not restricted for you, it is recommended that you run 'cmd' in the following prompt to gain access to a proper terminal.")
while True:
  try:
    prompt()
  except:
    break