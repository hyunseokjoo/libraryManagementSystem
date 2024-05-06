from enum import Enum


class LMSEnum(str, Enum):
    def __str__(self) -> str:
        return str.__str__(self)
