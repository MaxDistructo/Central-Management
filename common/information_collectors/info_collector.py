from common.operating_systems.os_info import OS_Info


class InformationCollector():
    oi: OS_Info = None

    def __init__(self, oi: OS_Info):
        self.oi = oi

    def get_program_list(self) -> list:
        print("unimplemented")

    def get_users(self) -> list:
        print("unimplemented")

    def get_drives(self) -> list:
        print("unimplemented")

    def get_nerd_stats(self) -> dict:
        print("unimplemented")


class WindowsInformation(InformationCollector):

    def __init__(self, oi: OS_Info):
        super().__init__(self, oi)

    def get_program_list(self) -> list:
        return self.oi.execute_command("wmic product get name").split("\n")

    def get_users(self) -> list:
        return self.oi.execute_command("wmic UserAccount get Name").split("\n")

    def get_drives(self) -> list:
        return self.oi.execute_command("wmic diskdrive list brief").split("\n")

    def get_nerd_stats(self) -> dict:
        # Collects a whole bunch of information from wmic that is useful to have but not critical
        os_info = self.oi.execute_command("wmic OS get Caption,CSDVersion,OSArchitecture,Version")
        bios = self.oi.execute_command("wmic BIOS get Manufacturer,Name,SMBIOSBIOSVersion,Version")
        cpu = self.oi.execute_command("wmic CPU get Name,NumberOfCores,NumberOfLogicalProcessors")
        ram = self.oi.execute_command("wmic MEMPHYSICAL get MaxCapacity")
        ram_detailed = self.oi.execute_command("wmic MEMORYCHIP get Capacity,DeviceLocator,PartNumber,Tag")
        nics = self.oi.execute_command("wmic NIC get Description,MACAddress,NetEnabled,Speed")
        audio = self.oi.execute_command("wmic sounddev get Name,Description,DeviceID,Manufacturer")
        domain = self.oi.execute_command("wmic COMPUTERSYSTEM get Domain")

        return {"os": os_info, "bios": bios, "cpu": cpu, "ram": ram, "ram_detailed": ram_detailed, "nics": nics,
                "audio": audio, "domain": domain}
