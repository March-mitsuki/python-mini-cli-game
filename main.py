"""main module"""
import random
import sys
import time
import questionary
from alive_progress import alive_bar
from interfaces.enemy import Enemy, EnemyType
from interfaces.player import Player


def create_player() -> Player:
  """create a new _player"""
  questionary.print(
    "\n -- Welcome to MagiclWorld -- \n",
    "bold italic fg:#9EC545"
  )

  player_name: str = questionary.text("勇者よ、名前を教えてくれないか: ").ask()

  prof: str = questionary.select(
    "勇者よ、あなたに合った職業を選択しよう: ",
    choices=[
      "剣士",
      "魔法使い",
      "戦士",
    ]
  ).ask()

  # with alive_bar(100, title="世界をロード中...") as a_bar:
  #   for i in range(100):
  #     if i == 30:
  #       a_bar.title = "少女祈祷中..."
  #     if i == 60:
  #       a_bar.title = "勇者を召喚中..."
  #     if i == 99:
  #       a_bar.title = "勇者帰来"
  #     time.sleep(0.05)
  #     a_bar()

  if player_name and prof:
    _player = Player(player_name, prof)
  elif player_name:
    _player = Player(name=player_name)
  elif prof:
    _player = Player(profession=prof)
  else:
    _player = Player()

  questionary.print(
    f"よくぞ来てくれた! {_player.name}様! さぁ、旅を続けよう!",
    "bold italic fg:#F5D300"
  )

  # print("あなたは勇者としてこの世界に召喚された")
  # with alive_bar(100, dual_line=True, length=30, title="", receipt=False) as a_bar:
  #   for _ in range(100):
  #     time.sleep(0.03)
  #     a_bar()

  # print("どうやらこの世界が危機に陥ったようだ")
  # with alive_bar(100, dual_line=True, title="", receipt=False) as a_bar:
  #   for _ in range(100):
  #     time.sleep(0.03)
  #     a_bar()

  # print("あなたはやりたくないと思いながらも、やらないといけないという使命感に襲われた")
  # with alive_bar(100, dual_line=True, title="", receipt=False) as a_bar:
  #   for _ in range(100):
  #     time.sleep(0.03)
  #     a_bar()

  # print("あなたが目を醒めて、国王の言う通り世界を脅かす「魔王」を倒す旅に出た")
  # with alive_bar(100, dual_line=True, title="", receipt=False) as a_bar:
  #   for _ in range(100):
  #     time.sleep(0.03)
  #     a_bar()

  # print("これが、劇の始まりのであった...")
  # with alive_bar(100, dual_line=True, title="", receipt=False) as a_bar:
  #   for _ in range(100):
  #     time.sleep(0.03)
  #     a_bar()

  return _player


def create_random_enemy() -> Enemy:
  """test create random enemy"""
  num = random.randint(0, len(EnemyType)-1)
  # print(EnemyType(EnemyNameList[num]))
  return Enemy(EnemyType(EnemyNameList[num]), PLAYER.level)


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
      time.sleep(0.03)
      a_bar()
  PLAYER.hit_point = PLAYER.max_hit_point
  PLAYER.magic_point = PLAYER.max_magic_point
  questionary.print(
    f"よくぞ来てくれた! {PLAYER.name}様! さぁ、旅を続けよう!",
    "bold italic fg:#F5D300"
  )


def handle_ctrl_c():
  """when ctrl c pressed, print player profile"""
  print("--- \nゲームを終了します")
  if PLAYER:
    print("今回の最終ステータス:")
    PLAYER.print_profile()
  sys.exit(0)


if __name__ == "__main__":
  try:
    EnemyNameList = []
    for enemy in EnemyType:
      # 初始化EnemyNameList
      EnemyNameList.append(enemy.value)

    PLAYER = create_player()
    random_enemy = create_random_enemy()
    while True:
      if battle(PLAYER, random_enemy):
        questionary.print(
          "勝利しました",
          "bold fg:#9EC545"
        )
        PLAYER.exp += random_enemy.drop_exp
        while PLAYER.exp >= PLAYER.needed_exp:
          PLAYER.level_up()
          questionary.print(
            "レベルアップしました: ",
            "bold blink fg:#9EC545"
          )
          time.sleep(0.2)
        PLAYER.print_profile()
        random_enemy = create_random_enemy()
      else:
        questionary.print(
          "誠に残念ながらあなたは無惨に敗北してしまいました",
          "bold underline fg:#CB291A"
        )
        when_defeat()
  except KeyboardInterrupt:
    handle_ctrl_c()
