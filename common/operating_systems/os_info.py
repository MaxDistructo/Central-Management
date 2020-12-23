import subprocess
import platform

class OS_Info:
    name = ""
    arch = ""
    version = ""
    def __init__(self, name, version, arch):
        self.name = name
        self.arch = arch
        self.version = version
    def execute_command(self, command):
        return subprocess.run(command)
    def update(self):
        self.execute_command("")

    def __to_json__(self) -> dict:
        return {"name":self.name, "version":self.version, "arch":self.arch}

class win_os_info(OS_Info):
    def update(self):
        self.execute_command("wuauclt.exe /detectnow /updatenow")

class mac_os_info(OS_Info):
    def update(self):
        self.execute_command("")

class debian_os_info(OS_Info):
    def update(self):
        self.execute_command("sudo apt update && sudo apt upgrade")

class arch_os_info(OS_Info):
    def update(self):
        self.execute_command("sudo pacman -Syyu")

class fedora_os_info(OS_Info):
    def update(self):
        self.execute_command("sudo dnf upgrade --refresh")

def os_info_builder() -> OS_Info:
    arch = platform.architecture()[0]
    if arch == "64bit":
        arch = "x64"
    elif arch == "32bit":
        arch = "x86"
    system = platform.system()
    if system == "Windows":
        return win_os_info(f"{platform.system()} {platform.release()}", platform.version(), arch)
    elif system == "Darwin":
        return mac_os_info(f"{platform.system()} {platform.release()}", platform.version(), arch)
    elif system == "Linux":
        apt_result = subprocess.Popen("which", "apt")
        pacman_result = subprocess.Popen("which", "pacman")
        dnf_result = subprocess.Popen("which", "dnf")
        if apt_result.returncode == 0:
            return debian_os_info(f"{platform.system()} {platform.release()}", platform.version(), arch)
        elif pacman_result == 0:
            return arch_os_info(f"{platform.system()} {platform.release()}", platform.version(), arch)
        elif dnf_result == 0:
            return fedora_os_info(f"{platform.system()} {platform.release()}", platform.version(), arch)
    else:
        return os_info(f"{platform.system()} {platform.release()}", platform.version(), arch)

