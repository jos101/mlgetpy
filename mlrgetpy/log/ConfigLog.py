from dataclasses import dataclass

from mlrgetpy.log.NoLog import NoLog
from mlrgetpy.log.NormalLog import NormalLog
from mlrgetpy.log.ILog import ILog


class ConfigLog:

    log: ILog = NoLog()
