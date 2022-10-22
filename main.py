"""main module"""
import time
import questionary
from alive_progress import alive_bar
from interfaces.player import Player

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
