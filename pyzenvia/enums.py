from enum import IntEnum, unique


@unique
class APIVersion(IntEnum):
    V1 = 1
    V2 = 2
