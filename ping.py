from pygame import *

font.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.size_x = size_x
        self.size_y = size_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

class Ball(GameSprite):
    speedx = 3
    speedy = 3
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y >= 400:
            self.speedy *= -1
        if self.rect.y <= 5:
            self.speedy *= -1
        if sprite.collide_rect(rocket1, ball):
            self.speedx = 3
        if sprite.collide_rect(rocket2, ball):
            self.speedx = -3

window = display.set_mode((700, 500))
display.set_caption("Пинг-понг")
run = True
clock = time.Clock()
FPS = 60

font = font.Font(None, 70)
rocket1 = Player('rocket.png', 10, 350, 80, 100, 5)
rocket2 = Player('rocket.png', 610, 350, 80, 100, 5)
ball = Ball('asteroid.png', 350, 250, 80, 80, 3)
lose1 = font.render('игрок 1 проиграл', True, (255, 0, 0))
lose2 = font.render('игрок 2 проиграл', True, (255, 0, 0))

run = True
finish = False
while run:
    window.fill((18, 227, 227))
    rocket1.update()
    rocket2.update2()
    ball.update()
    rocket1.reset()
    rocket2.reset()
    ball.reset()

    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        if ball.rect.x >= 620:
            window.blit(lose2, (150, 200))
            finish = True
        elif ball.rect.x <= 5:
            window.blit(lose1, (150, 200))
            finish = True

    
        clock.tick(FPS)
        display.update()