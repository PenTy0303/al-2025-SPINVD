import pygame, sys, random


def main():
    
    GameStart()
    TaitoruKimeru("Simple Shooting")
    
    player = Player()
    player_group = Iremono(player)
    bullets = Iremono()        
    enemy_bullets = Iremono()  
    enemies = Iremono()
    
    for i in range(8):
        enemy = Enemy(100 + i * 80, 100)
        enemies.add(enemy)

    game_over = False

    while True:
        GAMEN.fill((0, 0, 0))
        keys = OsiteruBotanha()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                GameOwaru()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
                # プレイヤーの弾を撃つ
                bullet = Bullet(player.rect.centerx, player.rect.top, -10, KIRO)
                bullets.add(bullet)

        if not game_over:
            player_group.update(keys)
            bullets.update()
            enemy_bullets.update()
            enemies.update()

            # 敵が弾を撃つ判定
            for enemy in enemies:
                if enemy.can_shoot():
                    enemy_bullet = Bullet(enemy.rect.centerx, enemy.rect.bottom, 7, AO)
                    enemy_bullets.add(enemy_bullet)

            # プレイヤーの弾と敵の衝突判定
            hits = Tamaatatta(bullets, enemies)

            # 敵の弾とプレイヤーの衝突判定
            if Yarareru(player, enemy_bullets):
                game_over = True

            # 敵を全部倒したらゲームクリア
            if not enemies:
                game_over = True

        player_group.draw(GAMEN)
        bullets.draw(GAMEN)
        enemy_bullets.draw(GAMEN)
        enemies.draw(GAMEN)

        if game_over:
            text = "SUGEE" if not enemies else "OSHIMAI"
            clear_text = MOJI.render(text, True, SIRO)
            GAMEN.blit(clear_text, (YOKO // 2 - clear_text.get_width() // 2, TATE // 2))

        KOUSIN(60)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,20))
        self.image.fill(MIDORI)
        self.rect = self.image.get_rect(centerx=YOKO//2, bottom=TATE - 10)
        self.speed = 6

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < YOKO:
            self.rect.x += self.speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, color):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed  # 上向きは負の値、下向きは正の値

    def update(self):
        self.rect.y += self.speed
        # 画面外に出たら消す
        if self.rect.bottom < 0 or self.rect.top > TATE:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(AKA)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.shoot_timer = 0  # 弾を撃つためのカウンター

        self.speed_x = 2      # 横移動の速さ
        self.direction = 1    # 1なら右、-1なら左

    def update(self):
        # 横に動く
        self.rect.x += self.speed_x * self.direction

        # 画面端にきたら方向を変える
        if self.rect.right >= YOKO or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += 20  # 下に少し進む（インベーダー風）

        # 弾を撃つタイマー
        self.shoot_timer += 1

    def can_shoot(self):
        if self.shoot_timer > 60:
            self.shoot_timer = 0
            return random.random() < 0.3
        return False
    













































































# pygame intialize

def GameStart() :
    pygame.init()
YOKO = 800
TATE = 600
GAMEN = pygame.display.set_mode((YOKO, TATE))
TOKEI = pygame.time.Clock()
MOJI = pygame.font.SysFont("Arial", 36)
SIRO = (255, 255, 255)
MIDORI = (0, 255, 0)
KIRO = (255, 255, 0)
AKA = (255, 0, 0)
AO = (0, 0, 255)  # 敵の弾の色

HAYAI = 4
OSOI = 2

def TaitoruKimeru(title):
    pygame.display.set_caption(title)

def KOUSIN(fps) -> None:
    pygame.display.flip()
    TOKEI.tick(fps)
    
    return
    
def Tamaatatta( bullets : list, enemies : list) -> dict:
    """_summary_
    玉が当たったかどうかを検索する
    Args:
        bullets (pygame.spliteクラスのList): 
        enemies (pygame.spliteクラスのList): 

    Returns:
        dict: 衝突判定した結果が前から順に入る(そもそもListから消される)
    """
    return pygame.sprite.groupcollide(bullets, enemies, True, True)

def Yarareru( player : list, bullets : list) -> bool:
    """_summary_

    Args:
        player (pytame.spliteクラスのインスタンス): _description_
        bullets (pygame.spliteクラスのList): _description_

    Returns:
        dict: 衝突判定結果が入る
    """
    
    return pygame.sprite.spritecollideany(player, bullets)

def Iremono( args=None ) -> pygame.sprite.Group:
    """_summary_
    pygame.sprite.Groupクラスのインスタンスを返却する関数
    Returns:
        pygame.sprite.Group: 
    """
    
    if(args):
        return pygame.sprite.Group(args)
    else:
        return pygame.sprite.Group()

def GameOwaru():
    pygame.quit()
    sys.exit()
    
def OsiteruBotanha():
    return pygame.key.get_pressed()

main()