from typing import Dict, Protocol


class TestOutputParser(Protocol):
    """Protocol for all test output parsers."""

    def parse(self) -> Dict:
        """Prunes the given code node.

        Returns:
            a dictionary of parsed results.
        """
        ...
