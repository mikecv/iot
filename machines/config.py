#!/usr/bin/env python3

import json


class Config():
    """
    Configuration class for machines.
    Reads a json configuration file if supplied and updates configuration object
    accordingly, else uses default configuration.

    class variable self.ConfigVersion is checked and if the initialised values are
    newer, the passed configuration file will be overwritten with new defaults.
    """

    def __init__(self, configFile: str) -> None:
        """
        Class initialisation.
        Parameters:
            configFile : Configuration file name.
        """

        # Configuration filename.
        self.cf = configFile

        # Version of configuration.
        self.ConfigVersion = 1

        # Custom machine details.
        self.MachineName = "Machine"
        self.IPaddress = "127.0.0.1"
        self.IPport = 50061

        # Logger configuration values
        self.DebugLevel = 10
        self.LogFileSize = 100000
        self.LogBackups = 3

        # Timers
        self.Timers = {
            "MainSleep" : 1
        }

        # gRPC settings.
        self.GRPC = {
            "ServerIP" : "127.0.0.1",
            "ServerPort" : 50051
        }

        # Machine settings.
        self.Machine = {
            "RegRetries" : 3,
            "RegDelay" : 5,
            "ControlAwayTime" : 5
        }

        # Read / update configuration from file.
        self.readConfig()

    def readConfig(self) -> None:
        """
        Attempt to read configuration file, and create default if it doesn't.
        If it exists then update this configuration class object with differences.
        """
        try:
            with open(self.cf) as config_file:
                config = json.load(config_file)

                # Check configuration version.
                # If version not a match then update completely.
                if config["ConfigVersion"] != self.ConfigVersion:
                    print("Upgrading configuration file.")
                    # Save configuration to file.
                    self.saveConfig()

                # Update configuration values if possible.
                # If not, just update with default + whatever values read.
                updateConfig = False
                paramSaved = ""
                try:
                    paramSaved = self.MachineName
                    self.MachineName = config["MachineName"]
                except Exception:
                    self.MachineName = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.IPaddress
                    self.IPaddress = config["IPaddress"]
                except Exception:
                    self.IPaddress = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.IPport
                    self.IPport = config["IPport"]
                except Exception:
                    self.IPport = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.DebugLevel
                    self.DebugLevel = config["DebugLevel"]
                except Exception:
                    self.DebugLevel = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.LogFileSize
                    self.LogFileSize = config["LogFileSize"]
                except Exception:
                    self.LogFileSize = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.LogBackups
                    self.LogBackups = config["LogBackups"]
                except Exception:
                    self.LogBackups = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.Timers["MainSleep"]
                    self.Timers["MainSleep"] = config["Timers"]["MainSleep"]
                except Exception:
                    self.Timers["MainSleep"] = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.GRPC["ServerIP"]
                    self.GRPC["ServerIP"] = config["GRPC"]["ServerIP"]
                except Exception:
                    self.GRPC["ServerIP"] = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.GRPC["ServerPort"]
                    self.GRPC["ServerPort"] = config["GRPC"]["ServerPort"]
                except Exception:
                    self.GRPC["ServerPort"] = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.Machine["RegRetries"]
                    self.Machine["RegRetries"] = config["Machine"]["RegRetries"]
                except Exception:
                    self.Machine["RegRetries"] = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.Machine["RegDelay"]
                    self.Machine["RegDelay"] = config["Machine"]["RegDelay"]
                except Exception:
                    self.Machine["RegDelay"] = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.Machine["ControlAwayTime"]
                    self.Machine["ControlAwayTime"] = config["Machine"]["ControlAwayTime"]
                except Exception:
                    self.Machine["ControlAwayTime"] = paramSaved
                    updateConfig = True

                # If required, i.e. couldn't update all data from user configuration, then save default.
                if updateConfig:
                    print("Saving configuration file due to user changed parameter.")
                    self.saveConfig()

        except Exception:
            # Create default configuration file.
            print("Saving default configuration data.")
            self.saveConfig()
        
    def saveConfig(self) -> None:
        """
        Export and save the configuration class object to a json file.
        A default configuration file will be created if one doesn't exist,
        or the current configuration file will be overwritten if it does.
        """

        # Format configuration data.
        cfgDict = {
            "ConfigVersion" : self.ConfigVersion,
            "MachineName" : self.MachineName,
            "IPaddress" : self.IPaddress,
            "IPport" : self.IPport,
            "DebugLevel" : self.DebugLevel,
            "LogFileSize" : self.LogFileSize,
            "LogBackups" : self.LogBackups,
            "Timers" : self.Timers,
            "GRPC" : self.GRPC,
            "Machine" : self.Machine
        }

        # Open file for writing.
        try:
            outfile = open(self.cf, "w")
            outfile.write(json.dumps(cfgDict, sort_keys=False, indent=4, ensure_ascii=False))
            outfile.close()
        except Exception:
            print("Failed to create default configuration file : {0:s}".format(self.cf))
