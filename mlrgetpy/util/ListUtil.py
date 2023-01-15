from typing import List


class ListUtil:

    def has_duplicated(list: List) -> bool:
        """Check if the list has duplicated items

        Args:
            list (List): the list with values

        Returns:
            bool: True is the list has duplicated itmes, false if every item is unique
        """
        return len(list) != len(set(list))
