import pygame
import sys
import random

"___(Pygameの初期化)___"
WIDTH, HEIGHT = 800, 600
screen = "___(画面の作成)___"
pygame.display.set_caption("Simple shooting")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)  # 敵の弾の色

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = "___(プレイヤーの見た目の作成)____"
        self.image.fill("___(プレイヤーの色)___")
        self.rect = self.image.get_rect(centerx=WIDTH//2, bottom=HEIGHT - 10)
        self.speed = 6

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            "____(左に動く)____"
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, color):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed # 上向きは負の値、下向きは正の値

    def update(self):
        self.rect.y += self.speed
        # 画面外に出たら消す
        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.shoot_timer = 0  # 弾を撃つためのカウンター

        self.speed_x = 2      # 横移動の速さ
        self.direction = 1    # 1なら右、-1なら左

    def update(self):
        # 横に動く
        self.rect.x += self.speed_x * self.direction

        # 画面端にきたら方向を変える
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            "____(端についたら向きを変える)____"
            self.rect.y += 20 # 下に少し進む（インベーダー風）

        # 弾を撃つタイマー
        self.shoot_timer += 1

    def can_shoot(self):
        if self.shoot_timer > 60:
            self.shoot_timer = 0
            return "___(30%の確率で弾を撃つ)___"
        return False

# グループを作成
player = Player()
player_group = pygame.sprite.Group(player)
bullets = pygame.sprite.Group()        # プレイヤーの弾
enemy_bullets = pygame.sprite.Group()  # 敵の弾

enemies = pygame.sprite.Group()
for i in range(8):
    enemy = Enemy(100 + i * 80, 100)
    enemies.add(enemy)

game_over = False

while True:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        # プレイヤーが弾を撃つ処理
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
            bullet = "___(プレイヤーの弾の作る)___"
            bullets.add(bullet)

    if not game_over:
        player_group.update(keys)
        bullets.update()
        enemy_bullets.update()
        enemies.update()

        # 敵が弾を撃つ判定
        for enemy in enemies:
            if enemy.can_shoot():
                enemy_bullet = Bullet(enemy.rect.centerx, enemy.rect.bottom, 7, BLUE)
                enemy_bullets.add(enemy_bullet)

        # 敵とプレイヤーの弾がぶつかったら消える
        hits = "___(敵に当たったか調べる)___"

        # 敵の弾がプレイヤーに当たったらゲームオーバー
        if "___(プレイヤーに当たったか調べる)___":
            game_over = True

        # 敵を全部倒したらゲームクリア
        if not enemies:
            game_over = True

    player_group.draw(screen)
    bullets.draw(screen)
    enemy_bullets.draw(screen)
    enemies.draw(screen)

    if game_over:
        text = "SUGEE" if not enemies else "OSHIMAI"
        clear_text = font.render(text, True, WHITE)
        screen.blit(clear_text, (WIDTH // 2 - clear_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)

