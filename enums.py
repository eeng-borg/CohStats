from enum import Enum


class DatabaseType(Enum):
    matches = "matches"
    profiles = "profiles"

class Factions(Enum):
    OST = 0
    Soviet = 1
    OKW = 2
    USF = 3
    UKF = 4

