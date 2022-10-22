"""defiened all enemy types"""
from enum import Enum, unique

@unique
class EnemyType(Enum):
  """enemy types"""
  GOBLIN = "ゴブリン"
  SLIME = "スライム"

class Enemy:
  """init enemy status here"""
  def __init__(self, enemy_type: str) -> None:
    self.enemy_type = EnemyType(enemy_type)
    if self.enemy_type == EnemyType.GOBLIN:
      self.hit_point = 10
      self.acctack = 2
      self.magic_point = 0
      self.shield = 0
    elif self.enemy_type == EnemyType.SLIME:
      self.hit_point = 5
      self.acctack = 1
      self.magic_point = 5
      self.shield = 0
