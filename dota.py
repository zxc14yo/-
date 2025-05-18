import pygame
import random

# Ініціалізація
pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Dota 2 Clone")

clock = pygame.time.Clock()

# Кольори
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Гравець
player = pygame.Rect(100, 300, 40, 40)
enemy = pygame.Rect(600, 300, 40, 40)
player_health = 100
enemy_health = 100
speed = 5

# Шрифт
font = pygame.font.SysFont("arial", 24)

# Атака
def attack(attacker, target):
    if attacker.colliderect(target):
        return 10  # Шкода
    return 0

# Основний цикл 
run = True
while run:
    clock.tick(60)
    win.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Управління гравцем
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= speed
    if keys[pygame.K_RIGHT]: player.x += speed
    if keys[pygame.K_UP]: player.y -= speed
    if keys[pygame.K_DOWN]: player.y += speed

    # Простий бот
    if enemy.x > player.x: enemy.x -= 2
    if enemy.x < player.x: enemy.x += 2
    if enemy.y > player.y: enemy.y -= 2
    if enemy.y < player.y: enemy.y += 2

    # Атака
    if keys[pygame.K_SPACE]:
        enemy_health -= attack(player, enemy)
    player_health -= attack(enemy, player)

    # Здоров’я
    pygame.draw.rect(win, RED, (player.x, player.y - 10, 40, 5))
    pygame.draw.rect(win, BLUE, (enemy.x, enemy.y - 10, 40, 5))

    # Персонажі
    pygame.draw.rect(win, RED, player)
    pygame.draw.rect(win, BLUE, enemy)

    # Текст
    health_text = font.render(f"Player HP: {player_health}  Enemy HP: {enemy_health}", True, (0, 0, 0))
    win.blit(health_text, (20, 20))

    pygame.display.update()

    # Перевірка перемоги
    if player_health <= 0:
        print("Game Over: You Lost!")
        run = False
    if enemy_health <= 0:
        print("Victory: Enemy Defeated!")
        run = False

pygame.quit()