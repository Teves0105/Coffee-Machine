import pygame

class Block:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)  # Nạp hình ảnh từ file
        self.image = pygame.transform.scale(self.image, (80, 50))  # Thay đổi kích thước
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)