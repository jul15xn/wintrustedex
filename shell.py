import os
import ctypes
from datetime import datetime
import subprocess

os.system("title TrustedInstaller Shell")
os.system("cls")
print("loading shell...")
print("checking admin...")

try:
    is_admin = os.getuid() == 0
except :
    is_admin = ctypes.windll.shell32.IsUserAnAdmin()

print("is admin: " + str(is_admin))

if not is_admin:
    print("This program has to be run as administrator for it to work properly!")
    os.system("pause > nul")
    quit(1)

print("retrieving default binpath...")

bin_path = os.getcwd() + "\binpath.txt"
binpathexc = "sc.exe qc trustedinstaller | findstr 'BINARY_PATH_NAME'"

print("binpathdump command: " + binpathexc)
bin = subprocess.Popen(["powershell", binpathexc], stdout=subprocess.PIPE)
bin_out, bin_err = bin.communicate()
bin_default_path = str(bin_out, "utf-8").replace("        BINARY_PATH_NAME   : ", "")
print("bin path found! " + bin_default_path)

print("shell loaded!\n")


def ProcessInput(inputText):
    splitted = inputText.split(" ")
    if inputText.startswith("tic"):
        try:
            command = inputText[4:]
            if str.isspace(command) or command == "":
                print("Invalid command!")
                return
            print("Executing as TrustedInstaller: " + command)
            formatted_command = 'sc.exe config TrustedInstaller binpath= "cmd /c ' + command + '"; sc.exe start TrustedInstaller; sc.exe stop TrustedInstaller; sc.exe config TrustedInstaller binpath= "' + bin_default_path + '"'
            p = subprocess.Popen(["powershell", formatted_command])
            p_out, p_err = p.communicate()
            print("Command executed!")
        except:
            print("Critical error whilst trying to run command, reverting back to old binpath...")
            try:
                p = subprocess.Popen(["powershell", 'sc.exe config TrustedInstaller binpath= "' + bin_default_path + '"'])
                p_out, p_err = p.communicate()
                print("Should have fixed, checking...")
                b = subprocess.Popen(["powershell", binpathexc], stdout=subprocess.PIPE)
                bb_out, bb_err = bin.communicate()
                bbb = str(bin_out, "utf-8").replace("        BINARY_PATH_NAME   : ", "")
                if bbb == bin_default_path:
                    print("Check was successfull, and the bin has been set successfully. Make sure next time you execute your command properly!")
                else:
                    print('Check was unsuccessfull, so you would have to do it yourself. What you want to do:\n1. Open powershell as Administrator\n2. Run the following command: sc.exe config TrustedInstaller binpath= "' + bin_default_path + '"\n3. Confirm if this command was successfull by running the "tisc" command in this shell and checking if the BINARY_PATH_NAME is equal to "' + bin_default_path + '"\n\nIf the last step check is true, you have successfully reverted the bin path. But next time, try to run a command that actually works :)')
            except:
                print('Check was unsuccessfull, so you would have to do it yourself. What you want to do:\n1. Open powershell as Administrator\n2. Run the following command: sc.exe config TrustedInstaller binpath= "' + bin_default_path + '"\n3. Confirm if this command was successfull by running the "tisc" command in this shell and checking if the BINARY_PATH_NAME is equal to "' + bin_default_path + '"\n\nIf the last step check is true, you have successfully reverted the bin path. But next time, try to run a command that actually works :)')

    elif inputText.startswith("cmd"):
        command = inputText[4:]
        c = subprocess.Popen(["cmd.exe", "/c", command])
        c_out, c_err = c.communicate()
    elif splitted[0] == "tisc":
        bb = subprocess.Popen(["powershell", "sc.exe qc trustedinstaller"], stdout=subprocess.PIPE)
        bb_out, bb_err = bb.communicate()
        print(str(bb_out, "utf-8"))
    elif splitted[0] == "help":
        print("All commands:")
        print("tic {COMMAND} - Runs a cmd command as TrustedInstaller")
        print("cmd {COMMAND} - Runs a cmd command as yourself")
        print("tisc - Gets information about the TrustedInstaller service")
        print("clear - Clears the screen")
        print("exit - Exits the shell")
    elif splitted[0] == "clear":
        os.system("cls")
    elif splitted[0] == "exit":
        quit(1)
    else:
        print("Unknown command! Type 'help' for help.")

while True:
    inp = input("> ")
    ProcessInput(inp)
