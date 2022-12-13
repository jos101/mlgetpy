from dataclasses import dataclass

from mlrgetpy.log.NoLog import NoLog
from mlrgetpy.log.NormalLog import NormalLog
from mlrgetpy.log.LogAbstract import LogAbstract


@dataclass
class ConfigLog:

    log: LogAbstract = NoLog()
