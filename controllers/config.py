#!/usr/bin/env python3

import json


class Config():
    """
    Configuration class for controllers.
    Reads a json configuration file if supplied and updates configuration object
    accordingly, else uses default configuration.

    class variable self.ConfigVersion is checked and if the initialised values are
    newer, the passed configuration file will be overwritten with new defaults.
    """

    def __init__(self, configFile):
        """
        Class initialisation.
        """

        # Configuration filename.
        self.cf = configFile

        # Version of configuration.
        self.ConfigVersion = 1

        # Custom controller details.
        self.ControllerName = "Controller"
        self.IPaddress = "127.0.0.1"

        # Logger configuration values.
        self.DebugLevel = 10
        self.LogFileSize = 100000
        self.LogBackups = 3

        # Timers.
        self.Timers = {
            "MainSleep" : 1,
            "WatchDog" : 1.5
        }

        # gRPC settings.
        self.GRPC = {
            "ListenPort" : 50051
        }

        # Machine control settings.
        self.MCtrl = {
            "MaxMachines" : 4,
            "LoopTime" : 1,
            "WatchdogRetries" : 3
        }

        # Read / update configuration from file.
        self.readConfig()

    def readConfig(self):
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
                try:
                    paramSaved = self.ControllerName
                    self.ControllerName = config["ControllerName"]
                except Exception:
                    self.ControllerName = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.IPaddress
                    self.IPaddress = config["IPaddress"]
                except Exception:
                    self.IPaddress = paramSaved
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
                    paramSaved = self.Timers["WatchDog"]
                    self.Timers["WatchDog"] = config["Timers"]["WatchDog"]
                except Exception:
                    self.Timers["WatchDog"] = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.GRPC["ListenPort"]
                    self.GRPC["ListenPort"] = config["GRPC"]["ListenPort"]
                except Exception:
                    self.GRPC["ListenPort"] = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.MCtrl["MaxMachines"]
                    self.MCtrl["MaxMachines"] = config["MCtrl"]["MaxMachines"]
                except Exception:
                    self.MCtrl["MaxMachines"] = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.MCtrl["LoopTime"]
                    self.MCtrl["LoopTime"] = config["MCtrl"]["LoopTime"]
                except Exception:
                    self.MCtrl["LoopTime"] = paramSaved
                    updateConfig = True
                try:
                    paramSaved = self.MCtrl["WatchdogRetries"]
                    self.MCtrl["WatchdogRetries"] = config["MCtrl"]["WatchdogRetries"]
                except Exception:
                    self.MCtrl["WatchdogRetries"] = paramSaved
                    updateConfig = True

                # If required, i.e. couldn't update all data from user configuration, then save default.
                if updateConfig:
                    print("Saving configuration file due to user changed parameter.")
                    self.saveConfig()

        except Exception:
            # Create default configuration file.
            print("Saving default configuration data.")
            self.saveConfig()
        
    def saveConfig(self):
        """
        Export and save the configuration class object to a json file.
        A default configuration file will be created if one doesn't exist,
        or the current configuration file will be overwritten if it does.
        """

        # Format configuration data.
        cfgDict = {
            "ConfigVersion" : self.ConfigVersion,
            "ControllerName" : self.ControllerName,
            "IPaddress" : self.IPaddress,
            "DebugLevel" : self.DebugLevel,
            "LogFileSize" : self.LogFileSize,
            "LogBackups" : self.LogBackups,
            "Timers" : self.Timers,
            "GRPC" : self.GRPC,
            "MCtrl" : self.MCtrl
        }

        # Open file for writing.
        try:
            outfile = open(self.cf, "w")
            outfile.write(json.dumps(cfgDict, sort_keys=False, indent=4, ensure_ascii=False))
            outfile.close()
        except Exception:
            print("Failed to create default configuration file : {0:s}".format(self.cf))
