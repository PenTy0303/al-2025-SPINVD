import pygame
import math
import sys

# 初期設定
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2 Player Shooting")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)

# 色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# プレイヤークラス
class Player(pygame.sprite.Sprite):
    def __init__(self, is_top=False):
        super().__init__()
        self.image = pygame.Surface((50, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.speed = 6
        self.inochi = 3
        self.is_top = is_top
        if is_top:
            self.rect.centerx = WIDTH // 2
            self.rect.top = 10
        else:
            self.rect.centerx = WIDTH // 2
            self.rect.bottom = HEIGHT - 10

    def update(self, left_key, right_key, keys):
        if keys[left_key] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[right_key] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# 弾クラス
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, color):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

# プレイヤー生成
player1 = Player(is_top=False)
player2 = Player(is_top=True)
player1_group = pygame.sprite.Group(player1)
player2_group = pygame.sprite.Group(player2)
player1_bullets = pygame.sprite.Group()
player2_bullets = pygame.sprite.Group()

# ゲーム状態
game_over = False
winner = ""

# ゲームループ
while True:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        # 発射
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullet = Bullet(player1.rect.centerx, player1.rect.top, -10, YELLOW)
                player1_bullets.add(bullet)
            if event.key == pygame.K_LSHIFT and not game_over:
                bullet = Bullet(player2.rect.centerx, player2.rect.bottom, 10, BLUE)
                player2_bullets.add(bullet)

    if not game_over:
        # プレイヤー操作
        player1.update(pygame.K_LEFT, pygame.K_RIGHT, keys)
        player2.update(pygame.K_a, pygame.K_d, keys)

        # 弾の更新
        player1_bullets.update()
        player2_bullets.update()

        # 衝突判定（player2が被弾）
        hit2 = pygame.sprite.spritecollideany(player2, player1_bullets)
        if hit2:
            hit2.kill()
            player2.inochi -= 1
            if player2.inochi < 1:
                game_over = True
                winner = "Player 1"

        # 衝突判定（player1が被弾）
        hit1 = pygame.sprite.spritecollideany(player1, player2_bullets)
        if hit1:
            hit1.kill()
            player1.inochi -= 1
            if player1.inochi < 1:
                game_over = True
                winner = "Player 2"

    # 描画
    player1_group.draw(screen)
    player2_group.draw(screen)
    player1_bullets.draw(screen)
    player2_bullets.draw(screen)

    # 残機表示
    p1_text = font.render(f"P1: {player1.inochi}", True, YELLOW)
    p2_text = font.render(f"P2: {player2.inochi}", True, BLUE)
    screen.blit(p1_text, (10, HEIGHT - 40))
    screen.blit(p2_text, (10, 10))

    # 勝敗表示
    if game_over:
        result_text = font.render(f"{winner} WIN!", True, WHITE)
        screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(30)
