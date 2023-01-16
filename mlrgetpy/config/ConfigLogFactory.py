from mlrgetpy.log.ConfigLog import ConfigLog
from mlrgetpy.log.NoLog import NoLog
from mlrgetpy.log.NormalLog import NormalLog


class ConfigLogfactory:
    def create(log):
        if log == "No_log":
            ConfigLog.log = NoLog()
        elif log == "Normal":
            ConfigLog.log = NormalLog()
