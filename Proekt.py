from pygame import *
from random import randint

print("Управление на A, D, лвк")

window = display.set_mode((700, 500))
display.set_caption('challenge')

life = 1

font.init()
font2 = font.SysFont(None, 36)
font1 = font.SysFont(None, 80)
win = font1.render('You win!', True, (255,25,255))
lose = font1.render('You lose!', True, (255,25,255))

mixer.init()
mixer.music.load('musica.wav')

img_Vrag1 = "abobA.png"
img_Vrag2 = "kamen.png"
img_Vrag3 = "derevo.png"
img_hero = "noletmediem.png"

win_width = 700
win_height = 500

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys_pressed[K_a] and x2 > 5:
            x2 -= speed
        if keys_pressed[K_d] and x2 < 595:
            x2 += speed
        if keys_pressed[K_w] and y2 > 5:
            y2 -= speed
        if keys_pressed[K_s] and y2 < 395:
            y2 += speed


class Enemy1(GameSprite):
    def update(self):
        if self.rect.y > win_height:
            self.rect.y -= self.speed
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0

class Enemy2(GameSprite):
    def update(self):
        if self.rect.y < win_height:
            self.rect.y += self.speed
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 500

class Enemy3(GameSprite):
    def update(self):
        if self.rect.x < win_width:
            self.rect.x -= self.speed
            self.rect.y = randint(80, win_height - 80)
            self.rect.x = 0 

monsters1 = sprite.Group()
for i in range(1,6):
    monster = Enemy2(img_Vrag2, randint(80, win_width - 80), -40, 80,50, randint(5,10))
    monsters1.add(monster)

monsters2 = sprite.Group()
for i in range(1,6):
    monster1 = Enemy1(img_Vrag1, randint(80, win_width - 80), 540, 80,50, randint(5,10))
    monsters2.add(monster1)
monsters3 = sprite.Group()
for i in range(1,6):
    monster2 = Enemy3(img_Vrag1, randint(80, win_height - 80), 740, 80,50, randint(5,10))
    monsters3.add(monster1)
hero = Player(img_hero, 350, 250, 25, 25, 50)

background = transform.scale(image.load('background.jpg'), (700, 500))


hero = transform.scale(image.load('noletmediem.png'), (25, 25))
monster = transform.scale(image.load('abobA.png'), (100, 100))
monster1 = transform.scale(image.load('kamen.png'), (250, 250))
monster2 = transform.scale(image.load('derevo.png'), (250, 250))

speed = 10

run = True
clock = time.Clock()
FPS = 60


while run:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            run = False

        hero.draw(window)




    display.update()
clock.tick(FPS)