"""defiened all enemy types"""
from enum import Enum, unique

@unique
class EnemyType(Enum):
  """enemy types"""
  GOBLIN = "ゴブリン"
  GOBLIN_SENIOR = "ゴブリン長老"
  SLIME = "スライム"
  ANCIENT_MACHIEN = "古代機械"

class Enemy:
  """init enemy status here"""
  def __init__(self, enemy_type: EnemyType) -> None:
    self.enemy_type = enemy_type
    if self.enemy_type == EnemyType.GOBLIN:
      self.hit_point = 10
      self.acctack = 2
      self.magic_point = 0
      self.shield = 0
      self.drop_exp = 10
    elif self.enemy_type == EnemyType.GOBLIN_SENIOR:
      self.hit_point = 100
      self.acctack = 20
      self.magic_point = 10
      self.shield = 10
      self.drop_exp = 80
    elif self.enemy_type == EnemyType.SLIME:
      self.hit_point = 5
      self.acctack = 1
      self.magic_point = 5
      self.shield = 0
      self.drop_exp = 5
    elif self.enemy_type == EnemyType.ANCIENT_MACHIEN:
      self.hit_point = 1000
      self.acctack = 100
      self.magic_point = 0
      self.shield = 100
      self.drop_exp = 1000
