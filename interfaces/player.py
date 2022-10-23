"""defiened all type of player"""
import math
from enum import Enum, unique
import questionary


@unique
class Profession(Enum):
  """enum type of player profession"""
  BLADE = "剣士"
  MAGIC_CASTER = "魔法使い"
  WARRIOR = "戦士"
  DEPRIVED = "持たざるもの"

class Player:
  """All Player Status Here"""
  def __init__(self, name: str = "名無し", profession: str = "持たざるもの") -> None:
    self.name = name
    self.level = 1
    self.exp = 0 # exp > needed_exp -> lv up
    self.needed_exp = 100 # needed_exp = 100 * level
    # デフォルトは持たざる者
    self.profession = Profession(profession)
    self.hit_point = 50
    self.max_hit_point = 50
    self.acctack = 1
    self.magic_point = 5
    self.max_magic_point = 5
    self.shield = 0
    if self.profession == Profession.BLADE:
      # 剣士はバランス的
      self.hit_point = 80
      self.max_hit_point = 80
      self.acctack = 15
      self.magic_point = 5
      self.max_magic_point = 5
      self.shield = 5
      self.print_profile()
    elif self.profession == Profession.MAGIC_CASTER:
      # 魔法使いは攻撃力が高いが、MP消耗してしまい、長期戦に長けていない
      self.hit_point = 50
      self.max_hit_point = 50
      self.acctack = 30
      self.magic_point = 10
      self.max_magic_point = 10
      self.shield = 0
      self.print_profile()
    elif self.profession == Profession.WARRIOR:
      # 戦士は防御力が高い、戦闘しながら回復する
      self.hit_point = 100
      self.max_hit_point = 100
      self.acctack = 10
      self.magic_point = 0
      self.max_magic_point = 0
      self.shield = 10
      self.print_profile()
    else:
      questionary.print("wow, you are a good boy.", "bold italic fg:#DC4518")
      self.print_profile()

  def print_profile(self):
    """print all status"""
    print(
      "---\n"+
      f"名前: {self.name} \n" +
      f"職業: {self.profession.value} \n" +
      f"レベル: {self.level} \n" +
      f"今の経験値: {self.exp} \n" +
      f"レベルアップに必要な経験値: {self.needed_exp} \n" +
      f"最大HP: {self.max_hit_point} \n" +
      f"残りHP: {self.hit_point} \n" +
      f"最大MP: {self.max_magic_point} \n" +
      f"残りMP: {self.magic_point} \n" +
      f"攻撃力: {self.acctack} \n" +
      f"防御力: {self.shield} \n" +
      "---"
    )

  def level_up(self):
    """level up function"""
    if self.level >= 9999:
      print("最大レベルに達したため、レベルアップできません")
      return
    self.level += 1
    self.exp -= self.needed_exp
    self.needed_exp = 100 * self.level
    self.max_hit_point = math.ceil(self.max_hit_point + (self.max_hit_point * 0.05))
    self.hit_point = self.max_hit_point
    self.acctack = math.ceil(self.acctack + (self.acctack * 0.01))
    self.max_magic_point = math.ceil(
      self.max_magic_point + (self.max_magic_point * 0.03)
    )
    self.magic_point = self.max_magic_point
    self.shield += 1
