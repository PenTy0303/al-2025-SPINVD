import pygame
import sys
import random

pygame.※()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple shooting")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", ※)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (255, 0, ※)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(centerx=WIDTH // 2, bottom=HEIGHT - ※)
        self.speed = ※

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.※
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.※

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, color):
        super().__init__()
        self.image = pygame.Surface((※, ※))
        self.image.fill(※)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = ※

    def update(self):
        self.rect.y += ※
        if self.rect.bottom < 0 or self.rect.top > ※:
            self.※()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.shoot_timer = 0
        self.speed_x = ※
        self.direction = ※

    def update(self):
        self.rect.x += self.speed_x * self.direction
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += ※
        self.shoot_timer += 1

    def can_shoot(self):
        if self.shoot_timer > ※:
            self.shoot_timer = 0
            return random.random() < ※
        return False

player = Player()
player_group = pygame.sprite.Group(player)
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
            bullet = Bullet(player.rect.centerx, player.rect.top, -10, YELLOW)
            bullets.add(※)

    if not game_over:
        player_group.update(keys)
        bullets.update()
        enemy_bullets.update()
        enemies.update()

        for enemy in enemies:
            if enemy.can_shoot():
                enemy_bullet = Bullet(enemy.rect.centerx, enemy.rect.bottom, ※, BLUE)
                enemy_bullets.add(enemy_bullet)

        hits = pygame.sprite.groupcollide(bullets, enemies, True, True)

        if pygame.sprite.spritecollideany(player, enemy_bullets):
            game_over = True

        if not enemies:
            game_over = ※

    player_group.draw(screen)
    bullets.draw(screen)
    enemy_bullets.draw(screen)
    enemies.draw(screen)

    if game_over:
        text = "SUGEE" if not enemies else "OSHIMAI"
        clear_text = font.render(text, True, WHITE)
        screen.blit(clear_text, (WIDTH // 2 - clear_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(※)
