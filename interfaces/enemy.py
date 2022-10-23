"""defiened all enemy types"""
import math
from enum import Enum, unique

@unique
class EnemyType(Enum):
  """enemy types"""
  GOBLIN = "ゴブリン"
  GOBLIN_SENIOR = "ゴブリン長老"
  SLIME = "スライム"
  METAL_SLIME = "メタルスライム"
  ANCIENT_MACHIEN = "古代機械"

class Enemy:
  """init enemy status here"""
  def __init__(self, enemy_type: EnemyType, player_level: int) -> None:
    self.enemy_type = enemy_type
    if self.enemy_type == EnemyType.GOBLIN:
      self.hit_point = math.ceil(10 + ( 10 * (player_level/10)))
      self.acctack = 2 * player_level
      self.magic_point = 0 * player_level
      self.shield = 0 * player_level
      self.drop_exp = math.ceil(10 + ( 10 * (player_level/100)))
    elif self.enemy_type == EnemyType.GOBLIN_SENIOR:
      self.hit_point = math.ceil(100 + ( 100 * (player_level/10)))
      self.acctack = math.ceil(20 + ( 20 * player_level/100))
      self.magic_point = 10 * player_level
      self.shield = 10 * player_level
      self.drop_exp = math.ceil(80 + ( 80 * (player_level/100)))
    elif self.enemy_type == EnemyType.SLIME:
      self.hit_point = math.ceil(5 + ( 5 * (player_level/10)))
      self.acctack = 1 * player_level
      self.magic_point = 5 * player_level
      self.shield = 0 * player_level
      self.drop_exp = math.ceil(5 + ( 5 * (player_level/100)))
    elif self.enemy_type == EnemyType.METAL_SLIME:
      self.hit_point = math.ceil(10 + ( 10 * (player_level/10)))
      self.acctack = 1 * player_level
      self.magic_point = 5 * player_level
      self.shield = 50 * player_level
      self.drop_exp = math.ceil(100 + ( 100 * (player_level/100)))
    elif self.enemy_type == EnemyType.ANCIENT_MACHIEN:
      self.hit_point = math.ceil(100 + ( 100 * (player_level/10)))
      self.acctack = 200 + ( 200 * player_level/100)
      self.magic_point = 0 * player_level
      self.shield = 100 * player_level
      self.drop_exp = math.ceil(1000 + ( 1000 * (player_level/100)))
