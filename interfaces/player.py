"""defiened all type of player"""
from enum import Enum, unique

@unique
class Profession(Enum):
  """enum type of player profession"""
  BLADE = "剣士"
  MAGIC_CASTER = "魔法使い"
  WARRIOR = "戦士"
  DEPRIVED = "持たざるもの"
