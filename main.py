"""main module"""
from enum import Enum, unique
import time
import questionary
from alive_progress import alive_bar

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
    # デフォルトは持たざる者
    self.profession = Profession(profession)
    self.hit_point = 50
    self.acctack = 1
    self.magic_point = 5
    self.shield = 0
    if self.profession == Profession.BLADE:
      # 剣士はバランス的
      self.hit_point = 80
      self.acctack = 15
      self.magic_point = 0
      self.shield = 5
      self.get_profile()
    elif self.profession == Profession.MAGIC_CASTER:
      # 魔法使いは攻撃力が高いが、MP消耗してしまい、長期戦に長けていない
      self.hit_point = 50
      self.acctack = 30
      self.magic_point = 10
      self.shield = 0
      self.get_profile()
    elif self.profession == Profession.WARRIOR:
      # 戦士は防御力が高い、戦闘しながら回復する
      self.hit_point = 100
      self.acctack = 10
      self.magic_point = 5
      self.shield = 10
      self.get_profile()
    else:
      questionary.print("wow, you are a good boy.", "bold italic fg:#DC4518")
      self.get_profile()

  def get_profile(self):
    """print all status"""
    print(
      f"名前: {self.name} \n" +
      f"職業: {self.profession.value} \n" +
      f"HP: {self.hit_point} \n" +
      f"攻撃力: {self.acctack} \n" +
      f"防御力: {self.shield} \n"
    )

def create_player() -> Player:
  """create a new player"""
  with alive_bar(100, title="世界をロード中...") as a_bar:
    for i in range(100):
      if i == 30:
        a_bar.title = "少女祈祷中..."
      if i == 60:
        a_bar.title = "勇者を召喚中..."
      if i == 99:
        a_bar.title = "勇者帰来"
      time.sleep(0.01)
      a_bar()

  questionary.print("Welcome to MagiclWorld", "bold italic fg:#9EC545")

  player_name: str = questionary.text("勇者よ、名前を教えてください：").ask()

  prof: str = questionary.select(
    "職業を選択してください: ",
    choices=[
      "剣士",
      "魔法使い",
      "戦士",
    ]
  ).ask()

  if player_name and prof:
    player = Player(player_name, prof)
  elif player_name:
    player = Player(name=player_name)
  elif prof:
    player = Player(profession=prof)
  else:
    player = Player()

  return player

if __name__ == "__main__":
  create_player()
