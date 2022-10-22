"""main module"""
import time
import questionary
from alive_progress import alive_bar

class UserSelect:
  """memo user select"""
  def __init__(self, name: str, profession: str) -> None:
    self.name = name
    self.profession = profession

with alive_bar(100, title="世界をロード中...") as bar:
  for i in range(100):
    if i == 30:
      bar.title = "少女祈祷中..."
    if i == 60:
      bar.title = "勇者を召喚中..."
    if i == 99:
      bar.title = "勇者帰来"
    time.sleep(0.01)
    bar()

questionary.print("Welcome to MagiclWorld", "bold italic fg:darkred")

playerName: str = questionary.text("勇者よ、名前を教えてください：").ask()

prof: str = questionary.select(
  "職業を選択してください: ",
  choices=[
    "剣士",
    "魔法使い",
    "戦士",
  ]
).ask()

player = UserSelect(playerName, prof)
print(player.name, player.profession)
