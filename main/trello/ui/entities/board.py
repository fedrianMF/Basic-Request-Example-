""" module to Board entity"""
from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class Board:  # pylint: disable=R0902
    """Board entity Class
    """
    name: Any = ""
    privacy: Any = "Team Visible"  # can be Private, Public or Team
    team: Any = "ATBOOTCAMP02"
