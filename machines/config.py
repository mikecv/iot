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

    def __init__(self, configFile):
        """
        Class initialisation.
        """

        # Configuration filename.
        self.cf = configFile

        # Version of configuration.
        self.ConfigVersion = 1

        # Logger configuration values
        self.DebugLevel = 10
        self.LogFileSize = 100000
        self.LogBackups = 3

        # Timers
        self.Timers = {
            "MainSleep" : 1
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
                paramSaved = ""
                try:
                    self.DebugLevel = config["DebugLevel"]
                except Exception:
                    updateConfig = True
                try:
                    self.LogFileSize = config["LogFileSize"]
                except Exception:
                    updateConfig = True
                try:
                    self.LogBackups = config["LogBackups"]
                except Exception:
                    updateConfig = True
                try:
                    paramSaved = self.Timers["MainSleep"]
                    self.Timers["PicCodedBgCol"] = config["Timers"]["MainSleep"]
                except Exception:
                    self.Timers["MainSleep"] = paramSaved
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
            "DebugLevel" : self.DebugLevel,
            "LogFileSize" : self.LogFileSize,
            "LogBackups" : self.LogBackups,
            "Timers" : self.Timers,
        }

        # Open file for writing.
        try:
            outfile = open(self.cf, "w")
            outfile.write(json.dumps(cfgDict, sort_keys=False, indent=4, ensure_ascii=False))
            outfile.close()
        except Exception:
            print("Failed to create default configuration file : {0:s}".format(self.cf))
