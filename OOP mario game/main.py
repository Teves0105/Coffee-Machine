import pygame
from mario import Mario
from enemy import Enemy
from block import Block

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mario Game")

# Màu sắc
WHITE = (255, 255, 255)
background = pygame.image.load("assets/background.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Thay đổi kích thước nền
# Tạo đối tượng
mario = Mario(100, 430, "assets/mario.png")  # Thêm đường dẫn hình ảnh Mario
enemy = Enemy(400, 240, "assets/enemy.png")  # Hình ảnh Enemy
block = Block(200, 450, "assets/block.png")  # Hình ảnh Block # Block ở vị trí x=200, y=450

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)  # Làm sạch màn hình với màu trắng

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cập nhật đối tượng
    mario.update()
    enemy.update()

    # Hiển thị hình nền
    screen.blit(background, (0, 0))
    # Vẽ đối tượng
    mario.draw(screen)
    enemy.draw(screen)
    block.draw(screen)

    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(60)  # Giới hạn FPS ở 60

pygame.quit()