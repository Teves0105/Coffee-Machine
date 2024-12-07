import pygame

class Enemy:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)  # Nạp hình ảnh từ file
        self.image = pygame.transform.scale(self.image, (250, 200))  # Thay đổi kích thước
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = 1  # Hướng di chuyển
        self.velocity = 2  # Tốc độ di chuyển

    def update(self):
        # Enemy di chuyển qua lại
        self.rect.x += self.direction * self.velocity
        if self.rect.left < 0 or self.rect.right > 800:  # Thay đổi hướng khi chạm biên
            self.direction *= -1

    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.image, True, False)  # Lật hình ảnh theo chiều ngang
        surface.blit(flipped_image, self.rect)