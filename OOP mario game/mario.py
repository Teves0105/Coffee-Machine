import pygame

class Mario:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)  # Nạp hình ảnh từ file
        self.image = pygame.transform.scale(self.image, (100, 190))  # Thay đổi kích thước
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Tốc độ di chuyển và trọng lực
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5  # Tốc độ di chuyển ngang
        self.gravity = 0.5  # Lực hút xuống
        self.jump_strength = -10  # Lực khi nhảy

        # Trạng thái trên mặt đất
        self.on_ground = False

    def update(self):
        # Điều khiển di chuyển ngang
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed
        else:
            self.velocity_x = 0

        # Nhảy
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False

        # Áp dụng trọng lực
        self.velocity_y += self.gravity

        # Cập nhật vị trí
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # Giới hạn Mario trong màn hình
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800

        # Giới hạn ở đáy màn hình (giả sử mặt đất là y = 500)
        if self.rect.bottom >= 430:
            self.rect.bottom = 430
            self.velocity_y = 0
            self.on_ground = True

    def draw(self, surface):
        surface.blit(self.image, self.rect)