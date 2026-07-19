#Create your own shooter

from pygame import *
from random import randint

img_back  = "yippe.png"
img_hero = "steve.png"
img_enemy = "zoombie.png"
img_bulet = "bullet.png"
score = 0
lost = 0
life = 3

#window
width = 700
height = 500
display.set_caption("Minecraft Shooter  Game")
window = display.set_mode((width, height))
background = transform.scale(image.load(img_back), (width, height))
#,music,  sounds
mixer.init()
mixer.music.load("space.ogg")
mixer.music.set_volume(0.001)
mixer.music.play()

font.init()
font1 = font.Font(None, 35)
font2 = font.Font(None,80)
win = font2.render("WIN! :D", True, (0, 220, 225))
lose = font2.render("YOU LOSE! ", True, (255, 0, 0))

shoot = mixer.Sound("fire.ogg")

#paren classes
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#main player class
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

    def fire(self):
        bullet = Bullet(img_bulet, player.rect.centerx, player.rect.top, 10, 40, 60)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost

        if self.rect.y > height:
            self.rect.y > height
            self.rect.x = randint(80, width - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

#sprites
player = Player(img_hero, 100, 400, 80, 100, 10)

monsters = sprite.Group()
for i in range(1, 60):
    monster = Enemy(img_enemy, randint(80, width - 80), 0, 80, 40, randint(1, 10))
    monsters.add(monster)

bullets = sprite.Group()

finish = False
#game loop
run  = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
                shoot.play()

    if not finish:
        window.blit(background, (0, 0))
 
        text_score = font1.render("Kills: " + str(score), 1, (0, 220, 225))
        window.blit(text_score, (10, 20))
        text_missed = font1.render("Attacks: " + str(lost), 1, (0, 220, 225))
        window.blit(text_missed, (10,50))
        text_life = font1.render("Health: " + str(life), 1, (0, 220, 225))
        window.blit(text_life, (10,80))

        player.update()
        monsters.update()
        monsters.draw(window)
        player.reset()
        bullets.update()
        bullets.draw(window)
        

        interaksi1 = sprite.groupcollide(bullets,  monsters, True, True)
        for c in interaksi1:
            score = score+1
            monster = Enemy(img_enemy, randint(80, width-80), randint(-50,0), 80, 40, randint(1,5))
            monsters.add(monster)
        
        if sprite.spritecollide(player, monsters, True):
            life = life -1
            monster = Enemy(img_enemy, randint(80, width - 80), randint(-50, 0), 80, 40, randint(1, 5))
            monsters.add(monster)

        if lost >= 100 or life <= 0:
            finish = True
            window.blit(lose, (200, 250))

        if score >= 100:
            finish = True
            window.blit(win, (200, 250))
#peluru
        display.update()
    
    else:
        finish = False
        score = 0
        lost =0 
        life = 20
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        time.delay(3000)
        for i in range(1,60):
            monster = Enemy(img_enemy, randint(80, width-80), randint(-50, 0), 80, 40, randint(1, 5))
            monsters.add(monster)
    
    time.delay(50)





window.blit(background, (0, 0))
player.update()
player.reset()
display.update()
   
time.delay(50)



""" ____         __Д.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,Д.,.,.,.,.,.,.,_
\ \     \_/_\      -o    ===       ------  ;;;;;;;;;;;;;;;;;;;;▄▄▄▄▄▄    
/_-----   /    /(/_)‾‾‾ ██/‾‾ {_/‾     " " (_-___}----------------------------------------------------
           /__/            {██}  

    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢶⣶⣶⠼⣦⣤⣼⣼⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⣯⠿⠟⠛⠻⢶⣿⣯⣿⣿⣃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣖⣺⡿⠿⠷⠶⠒⢶⣶⠖⠀⠉⡻⢻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⢻⣭⣫⣿⠁⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣖⡿⠋⢙⣿⠿⢿⠿⣿⡦⠄⠀⠀⠀⣠⣾⠟⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣰⣿⣴⣿⡿⠿⠿⠿⢿⣦⣄⠀⠀⠀⣠⣾⣿⠃⠀⢀⣸⡿⣳⣶⣲⡄⠀⠀⠀⠀⠀⠀
⠀⠀⣾⣽⡿⣛⣵⠾⠿⠿⠷⣦⣌⠻⣷⣄⢰⣿⠟⠁⠀⢠⣾⠿⢡⣯⠸⠧⢽⣄⠀⠀⠀⠀⠀
⠀⢸⡇⡟⣴⡿⢟⣽⣾⣿⣶⣌⠻⣧⣹⣿⡿⠋⠀⠀⠀⣾⠿⡇⣽⣿⣄⠀⠀⠉⠳⣄⢀⡀⠀
⠀⢸⠇⢳⣿⢳⣿⣿⣿⣿⣿⣿⡆⢹⡇⣿⡇⠀⡆⣠⣼⡏⢰⣿⣿⣿⣿⣦⠀⠀⠀⠈⠳⣅⠀
⠀⣸⡀⢸⣿⢸⣿⣿⣿⣿⣿⣿⡇⣸⡇⣿⡇⠀⡟⣻⢳⣷⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠘⣧
⢰⡟⡿⡆⠹⣧⡙⢿⣿⣿⠿⡟⢡⣿⢷⣿⣧⠾⢠⣿⣾⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠘
⠀⠻⡽⣦⠀⠈⠙⠳⢶⣦⡶⠞⢻⡟⡸⠟⠁⢠⠟⠉⠉⠙⠿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⡴
⠀⠀⢸⣿⡇⠀⠀⣀⣠⠀⢀⡀⠸⣹⠇⠀⣰⡟⡀⠀⠈⠛⠻⢿⣻⣿⡿⠀⠀⠀⠀⠀⠀⡠⠁
⠀⠀⢸⣿⣇⣴⢿⣿⣿⣿⣮⣿⣷⡟⠀⣰⣿⢰⠀⣀⠀⠀⠀⢀⣉⣿⡇⠀⠀⠀⠀⠀⣸⠃⠀
⠀⠀⢸⣿⡟⣯⠸⣿⣿⣿⣿⢈⣿⡇⣼⣿⠇⣸⡦⣙⣷⣦⣴⣯⠿⠛⢷⡀⠀⠀⠀⣰⡟⠀⠀
⠀⠀⠘⣿⣿⡸⣷⣝⠻⠟⢋⣾⣟⣰⡏⣠⣤⡟⠀⠀⠈⠉⠁⠀⠀⠀⠀⢻⣶⠀⢀⣿⠁⠀⠀
⠀⠀⠀⢸⡿⣿⣦⣽⣛⣛⣛⣭⣾⣷⡶⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠁⢸⢻⠁⠀⠀⠀⠀
⠀⠀⠀⠀⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣤⣀⣀⣀⣀⣀⣠⣤⠶⠛⠁⢀⣾⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣻⣿⣿⣿⣿⣿⣿⣎⣿⡅⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⣼⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡷⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⠻⢿⣿⣿⣟⣂⣀⣀⣀⣀⣀⣀⣤⠴⠋⠁⣾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣷⣷⡄⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⣤⣤⣤⣤⣄⣤⣤⡤⠴⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀"""
                                                
                                               