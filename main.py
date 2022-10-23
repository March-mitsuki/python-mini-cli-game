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
    "\n -- Welcome to use MagiclStone -- \n",
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
  # print(EnemyType(enemy_name_list[num]))
  return Enemy(EnemyType(enemy_name_list[num]), PLAYER.level)


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
  if death_times > 100 and PLAYER.level > 20:
    questionary.print(
      "あなたは体の異様な痛みを覚えながらも、再び冒険を始まった",
      "bold italic fg:#EEB0AC"
    )
    with alive_bar(100, dual_line=True, title="", receipt=False) as bar:
      for _ in range(100):
        time.sleep(0.03)
        bar()


def unnomal_death_event():
  """unnomal deeat event"""
  with alive_bar(100, title="世界をロード中...", manual=True) as a_bar:
    for i in range(100):
      if i == 10:
        a_bar.title = "勇者■◆■■■◆に..."
        for _ in range(5):
          a_bar(random.random())
          time.sleep(0.05)
        a_bar.title="世界をロード中..."
      if i == 20:
        a_bar.title = "■■◆◆■◆■■◆???"
        for _ in range(5):
          a_bar(random.random())
          time.sleep(0.05)
        a_bar.title = "少女祈祷中..."
      if i == 50:
        a_bar.title = "■◆■■復活■◆..."
        for _ in range(5):
          a_bar(random.random())
          time.sleep(0.05)
        a_bar.title = "少女祈祷中..."
      if i == 69:
        a_bar.title = "■◆■■ため■◆に..."
        for _ in range(5):
          a_bar(random.random())
          time.sleep(0.05)
        a_bar.title = "勇者召喚中..."
      if i == 75:
        a_bar.title = "■戦争■◆◆■◆■■◆"
        for _ in range(5):
          a_bar(random.random())
          time.sleep(0.05)
        a_bar.title = "勇者召喚中..."
      if i == 30:
        a_bar.title = "少女祈祷中..."
      if i == 60:
        a_bar.title = "勇者召喚中..."
      if i == 99:
        a_bar.title = "勇者帰来"
      time.sleep(0.03)
      a_bar((i+1) / 100)
  PLAYER.hit_point = PLAYER.max_hit_point
  PLAYER.magic_point = PLAYER.max_magic_point
  questionary.print(
    f"よくぞ来てくれた! {PLAYER.name}様! さぁ、旅を続けよう!",
    "bold italic fg:#F5D300"
  )
  if death_times > 100 and PLAYER.level > 20:
    questionary.print(
      "あなたは体の異様な痛みを覚えながらも、再び冒険を始まった",
      "bold italic fg:#EEB0AC"
    )
    with alive_bar(100, dual_line=True, title="", receipt=False) as bar:
      for _ in range(100):
        time.sleep(0.03)
        bar()


def end_of_the_strory():
  """when the end of strory"""
  questionary.print(
    "幾たびの戦えと経て、あなたは気づいた",
    "bold italic fg:#9EC545"
  )
  with alive_bar(100, dual_line=True, title="", receipt=False) as a_bar:
    for _ in range(100):
      time.sleep(0.03)
      a_bar()

  questionary.print(
    "この世界に危機なんて存在しなかった",
    "bold italic fg:#9EC545"
  )
  with alive_bar(100, dual_line=True, title="", receipt=False) as a_bar:
    for _ in range(100):
      time.sleep(0.03)
      a_bar()

  questionary.print(
    "ただ統治者たちが、わざと人々に恐怖と救済を与えるためにわざとしているものだった",
    "bold italic fg:#9EC545"
  )
  with alive_bar(100, dual_line=True, title="", receipt=False) as a_bar:
    for _ in range(100):
      time.sleep(0.03)
      a_bar()

  questionary.print(
    "つまり、飴と鞭、戦争をするための戦争だ",
    "bold italic fg:#9EC545"
  )
  with alive_bar(100, dual_line=True, title="", receipt=False) as a_bar:
    for _ in range(100):
      time.sleep(0.03)
      a_bar()

  questionary.print(
    "これに気づいたあなたは、MagicStoneを壊し、自ら命をたち、永遠の眠りについた...",
    "bold italic fg:#9EC545"
  )
  with alive_bar(100, dual_line=True, title="", receipt=False) as a_bar:
    for _ in range(100):
      time.sleep(0.03)
      a_bar()

  questionary.print(
    "...",
    "bold italic fg:#9EC545"
  )
  with alive_bar(100, dual_line=True, title="", receipt=False) as a_bar:
    for _ in range(100):
      time.sleep(0.03)
      a_bar()

  questionary.print(
    "......",
    "bold italic fg:#9EC545"
  )
  with alive_bar(100, dual_line=True, title="", receipt=False) as a_bar:
    for _ in range(100):
      time.sleep(0.03)
      a_bar()

  questionary.print(
    f"\nこの「冒険」の中で、あなたは合計 {death_times} 回死亡した \n" +
    f"そして、第 {battle_times} 回の戦闘を終えた時に真相に気づいた \n" +
    "あなたの最終ステータスは: ",
    "bold italic fg:#EEB0AC"
  )
  PLAYER.print_profile()


def handle_ctrl_c():
  """when ctrl c pressed, print player profile"""
  print("--- \nゲームを終了します")
  if PLAYER:
    print("今回の最終ステータス:")
    PLAYER.print_profile()
  sys.exit(0)


if __name__ == "__main__":
  try:
    enemy_name_list = []
    death_times = 0
    battle_times = 0
    for enemy in EnemyType:
      # 初始化enemy_name_list
      enemy_name_list.append(enemy.value)

    PLAYER = create_player()

    # PLAYER.acctack = 200
    # PLAYER.level = 19
    # death_times = 99

    random_enemy = create_random_enemy()
    while True:
      if battle(PLAYER, random_enemy):
        questionary.print(
          "勝利しました",
          "bold fg:#9EC545"
        )
        battle_times += 1
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

        if PLAYER.level > 100:
          # 当lv > 100时则有10%的概率可触发结局
          break_num = random.randint(0, 100)
          if break_num in (1,11,22,33,44,55,66,77,88,99):
            end_of_the_strory()
            break
      else:
        questionary.print(
          "誠に残念ながらあなたは無惨に敗北してしまいました",
          "bold underline fg:#CB291A"
        )
        death_times += 1
        if PLAYER.level > 50:
          # 当lv > 50时有20%几率触发活动
          event_num = random.randint(0, 100)
          if event_num in (1,11,22,33,44,55,66,77,88,99,7,17,27,37,47,57,67,77,87,97):
            unnomal_death_event()
          else:
            when_defeat()
        else:
          when_defeat()
  except KeyboardInterrupt:
    handle_ctrl_c()
