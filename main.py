"""main module"""
import sys
import time
import questionary
from alive_progress import alive_bar
from interfaces.enemy import Enemy, EnemyType
from interfaces.player import Player

def create_player() -> Player:
  """create a new _player"""
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

  questionary.print("\n -- Welcome to MagiclWorld -- \n", "bold italic fg:#9EC545")

  player_name: str = questionary.text("勇者よ、名前を教えてくれないか: ").ask()

  prof: str = questionary.select(
    "勇者よ、あなたに合った職業を選択しよう: ",
    choices=[
      "剣士",
      "魔法使い",
      "戦士",
    ]
  ).ask()

  if player_name and prof:
    _player = Player(player_name, prof)
  elif player_name:
    _player = Player(name=player_name)
  elif prof:
    _player = Player(profession=prof)
  else:
    _player = Player()

  return _player

def create_random_enemy():
  """test create random enemy"""
  print(len(EnemyType))

def battle(_player: Player, _enemy: Enemy) -> bool:
  """battle _player with enemy"""
  print(f"{_enemy.enemy_type.value}と戦闘中...")
  while True:
    _enemy.hit_point -= _player.acctack
    with alive_bar(100, dual_line=True, title="", receipt=False) as a_bar:
      a_bar.text = f"{_player.name} が攻撃している..."
      for _ in range(100):
        time.sleep(0.01)
        a_bar()
    print(f"{_enemy.enemy_type.value} に対して {_player.acctack} ダメージを与えた")
    print(
      f"-- {_player.name}のHP: {_player.hit_point} - " +
      f"{_enemy.enemy_type.value}のHP: {_enemy.hit_point} --"
    )
    if _enemy.hit_point <= 0:
      return True
    elif _player.hit_point <= 0:
      return False

    _player.hit_point -= _enemy.acctack
    with alive_bar(100, dual_line=True, title="", receipt=False) as a_bar:
      a_bar.text = f"{_enemy.enemy_type.value} が攻撃している..."
      for _ in range(100):
        time.sleep(0.01)
        a_bar()
    print(f"{_player.name} が {_enemy.acctack} ダメージを受けた")
    print(
      f"-- {_player.name}のHP: {_player.hit_point} - " +
      f"{_enemy.enemy_type.value}のHP: {_enemy.hit_point} --"
    )
    if _enemy.hit_point <= 0:
      return True
    elif _player.hit_point <= 0:
      return False

def when_defeat():
  """restart life"""
  with alive_bar(100, title="世界をロード中...") as a_bar:
    for i in range(100):
      if i == 30:
        a_bar.title = "少女祈祷中..."
      if i == 60:
        a_bar.title = "勇者召喚中..."
      if i == 99:
        a_bar.title = "勇者帰来"
      time.sleep(0.01)
      a_bar()
  questionary.print(f"ようこそ来てくれた! {PLAYER.name}様! ", "bold italic fg:#9EC545")

def handle_ctrl_c():
  """when ctrl c pressed, print player profile"""
  print("--- \nゲームを終了します")
  print("今回の最終ステータス:")
  PLAYER.get_profile()
  sys.exit(0)

if __name__ == "__main__":
  try:
    PLAYER = create_player()
    goblin = Enemy(EnemyType.GOBLIN_SENIOR)
    if battle(PLAYER, goblin):
      print("勝利しました")
      PLAYER.exp += goblin.drop_exp
      if PLAYER.exp >= 100:
        PLAYER.level_up()
    else:
      questionary.print(
        "誠に残念ながらあなたは無惨に敗北してしまいました",
        "bold underline fg:#CB291A"
      )
  except KeyboardInterrupt:
    handle_ctrl_c()
