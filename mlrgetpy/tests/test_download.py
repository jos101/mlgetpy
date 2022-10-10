from mlrgetpy.Filter import Filter
from mlrgetpy.Repository import Repository
import unittest
import pandas as pd
from mlrgetpy.enums.Area import Area

from mlrgetpy.enums.AttributeType import FilterAttributeType


class Test_Download(unittest.TestCase):

    def test_download(self):
        rep = Repository()
        #rep.addByIDs(IDs=[480, 296, 540, 307, 314])
        #rep.addByIDs(IDs=[296, 540, 307, 314])

        # uses folders in old_url (432, 442)
        # rep.addByIDs(IDs=[432])
        # rep.addByIDs(IDs=[442])
        # uses folders in old_url (516)
        # rep.addByIDs(IDs=[516])
        #rep.addByIDs(IDs=[516, 296, 540, 307, 314])

        # 713 uses new url https://archive-beta.ics.uci.edu/api/static/ml/datasets/713
        # and subfolder
        # 480 uses old url https://archive.ics.uci.edu/ml/machine-learning-databases/00480/
        # 692 uses new url https://archive-beta.ics.uci.edu/api/static/ml/datasets/692

        # ┌────┬───────────┬────────┬───────────┐
        # │    │   old url │ new url│ subfolders│
        # ├────┼───────────┼────────┼───────────┤
        # │ 713│           │     x  │     x     │
        # ├────┼───────────┼────────┼───────────┤
        # │ 299│     x     │        │           │
        # ├────┼───────────┼────────┼───────────┤
        # │ 692│     x     │        │           │
        # └────┴───────────┴────────┴───────────┘
        # TODO: test with old url with subfolders
        rep.addByIDs(IDs=[713, 299, 692])

        # rep.addByIDs(IDs=[713])

        rep.download()