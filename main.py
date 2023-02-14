from subprocess import call

#call(["ping", "www.google.com"])
#call(["ping", "www.google.com"])

print("Package initializing...")
call(["sudo", "apt-get", "upgrade", "-y"])
call(["sudo", "apt-get", "install", "-y"])
call(["sudo", "apt", "install", "aircrack-ng", "-y"])
print("Package update complete")

print("Check processes")
call(["sudo", "airmon-ng"])
call(["sudo", "airmon-ng", "check"])
call(["sudo", "airmon-ng", "check", "kill"])
print("Interfering processes killed...")


call(["sudo", "airmon-ng", "start", "wlan0"])
call(["sudo", "iwconfig"])



