from nautobot.core.apps import NautobotConfig


class DCIMConfig(NautobotConfig):
    name = "nautobot.dcim"
    verbose_name = "DCIM"
    searchable_models = [
        "cable",
        "controller",
        "device",
        "devicefamily",
        "deviceredundancygroup",
        "devicetype",
        "location",
        "powerfeed",
        "rack",
        "rackgroup",
        "softwareversion",
        "virtualchassis",
    ]

    def ready(self):
        super().ready()
        import nautobot.dcim.signals  # noqa: F401  # unused-import -- but this import installs the signals
