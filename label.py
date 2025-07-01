# 対応するラベルとコード
choices = [
    ("ゲームを始める", "pygame.init()"),
    ("ゲームの窓を作る", "pygame.display.set_mode((WIDTH, HEIGHT))"),
    ("プレイヤーの見た目の形", "pygame.Surface((50,20))"),
    ("プレイヤーの色", "GREEN"),
    ("左に動く", "self.rect.x -= self.speed"),
    ("端についたら向きを変える", "self.direction *= -1"),
    ("30%の確率で弾を撃つ", "random.random() < 0.3"),
    ("プレイヤーの弾の作る", "Bullet(player.rect.centerx, player.rect.top, -10, YELLOW)"),
    ("敵に当たったか調べる", "pygame.sprite.groupcollide(bullets, enemies, True, True)"),
    ("プレイヤーに当たったか調べる", "pygame.sprite.spritecollideany(player, enemy_bullets)"),
]
easy_choices = [
    ("ゲームを始める", "pygame.init()"),
    ("ゲームの窓を作る", "pygame.display.set_mode((WIDTH, HEIGHT))"),
    ("プレイヤーの形", "pygame.Surface((50,20))"),
    ("プレイヤーの色", "GREEN"),
    ("左に動く", "self.rect.x -= self.speed"),
    ("端に着いたら向きを変える", "self.direction *= -1"),
    ("弾をうつかどうか決める", "random.random() < 0.3"),
    ("プレイヤーの弾を作る", "Bullet(player.rect.centerx, player.rect.top, -10, YELLOW)"),
    ("敵に当たったか調べる", "pygame.sprite.groupcollide(bullets, enemies, True, True)"),
    ("プレイヤーに当たったか調べる", "pygame.sprite.spritecollideany(player, enemy_bullets)"),
]
