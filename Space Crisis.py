import pygame
import random
import time
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_a,
    K_b,
    K_c,
    K_d,
    K_e,
    K_f,
    K_g,
    K_h,
    K_i,
    K_j,
    K_k,
    K_l,
    K_m,
    K_n,
    K_o,
    K_p,
    K_q,
    K_r,
    K_s,
    K_t,
    K_u,
    K_v,
    K_w,
    K_x,
    K_y,
    K_z,
    K_SPACE,
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        pimage = pygame.image.load("Mongoose_large.png")
        pimage = pygame.transform.scale(pimage, (75,48))
        self.surf = pimage.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > X:
            self.rect.right = X
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= Y:
            self.rect.bottom = Y


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        eimage = pygame.image.load("asteroid.png")
        eimage = pygame.transform.scale(eimage, (40, 40))
        self.surf = eimage.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(X + 20, X + 100),
                random.randint(0, Y),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
     
#initiate pygame        
pygame.init()

X = 900
Y = 500
black = (0,0,0)
white = (255,255,255)
spacecolor = (0,34,64)
lives = 5
gamemode = 0
switch = 1
clock = pygame.time.Clock()
mcycle = 0
m = False
count = 0
score = 0
end = False
starttime = 0
endtime = 0

screen = pygame.display.set_mode([X,Y])

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)



player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)




pygame.display.set_caption('Space Crisis')

font = pygame.font.Font('freesansbold.ttf', 32)
startfont = pygame.font.Font('Debrosee.ttf', 32)
lbtext = startfont.render(' Among Asteroids ', True, white, spacecolor)
rbtext = startfont.render(' Rocket Type ', True, white, spacecolor)
dbtext = startfont.render(' Cycle Music ', True, white, spacecolor)
lbRect = lbtext.get_rect()
lbRect.center = (X / 3, Y / 5 * 3)
rbRect = rbtext.get_rect()
rbRect.center = (X / 3 * 2, Y / 5 * 3)
dbRect = dbtext.get_rect()
dbRect.center = (X / 2, Y / 5 * 4)

gamefont = pygame.font.Font('Freedom.ttf', 120)
title = gamefont.render('SPACE CRISIS', True, (0, 250, 230))
titleRect = title.get_rect()
titleRect.center = (X / 2, Y / 3)

def word():
    lst=["hi","bye", "vent", "suspicious", "button", "meeting", "astronaut", "roll", "bear", "red", "blue" ,"hall", "person", "panda",
         "mouse", "food", "imposter", "search", "look", "fun", "type", "monkey", "crewmate", "sus", "innocent", "cyan", "green", "yellow",
         "generator", "security", "amogus", "ship", "thrusters", "navigation", "computer", "game", "space", "stars", "learning", "turtle",
         "penguin", "bruh", "pikachu", "pokemon", "headphones", "keyboard", "type", "asteroid", "planet", "sun", "moon", "solar", "lunar",
         "system", "galaxy", "milky", "way", "stars", "star", "among us", "amogus", "lime", "white", "black", "orange", "pink", "purple",
         "lie", "discuss", "vote", "believe", "earth", "charizard"
         ]
    ran=random.choice(lst)
    return ran
    
def sentence(numofwords):
    typelst=[]
    for i in range(numofwords):
        typelst.append(word())
    strlst=" ".join(typelst)
    return strlst

def lsttostr(string):
    li = list(string.split(" "))
    return li

def strtolst(list):
    st= " ".join(list)
    return st
typethis = sentence(random.randint(6, 7))
strthis=lsttostr(typethis)
print(strthis)

charcount = len(typethis)
wordlength = len(typethis)


def start():
    screen.fill(white)
    spacebg = pygame.image.load("space.jpg")
    spacebg = pygame.transform.scale(spacebg, (900, 600))
    screen.blit(spacebg, (0, 0))
    screen.blit(lbtext, lbRect)
    screen.blit(rbtext, rbRect)
    screen.blit(dbtext, dbRect)
    screen.blit(title, titleRect)
    pygame.mixer.music.load("1 - Everybody Falls (Fall Guys Theme).mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.7)

def musicstart():
    pygame.mixer.music.pause()
    pygame.mixer.music.load("Roundstart.mp3")
    pygame.mixer.music.play()
    time.sleep(2.5)
    randomint = random.randint(0, 8)
    if randomint == 0:
        pygame.mixer.music.load("1 - Everybody Falls (Fall Guys Theme).mp3")
    elif randomint == 1:
        pygame.mixer.music.load("1-03 - Battlefield.mp3")
    elif randomint == 2:
        pygame.mixer.music.load("1-14 GREEN GREENS (Kirby's Dream Land).mp3")
    elif randomint == 3:
        pygame.mixer.music.load("3 - Survive the Fall.mp3")
    elif randomint == 4:
        pygame.mixer.music.load("01 Home.mp3")
    elif randomint == 5:
        pygame.mixer.music.load("06 Match Loading.mp3")
    elif randomint == 6:
        pygame.mixer.music.load("Die For You ft. Grabbitz Instrumental.mp3")
    elif randomint == 7:
        pygame.mixer.music.load("2 - Fall 'N' Roll.mp3")
    elif randomint == 8:
        pygame.mixer.music.load("Among Us Drip.mp3")
    pygame.mixer.music.play(-1)


def musiccycle(m):
    pygame.mixer.music.pause()
    if m == 0:
        pygame.mixer.music.load("1 - Everybody Falls (Fall Guys Theme).mp3")
    elif m == 1:
        pygame.mixer.music.load("1-03 - Battlefield.mp3")
    elif m == 2:
        pygame.mixer.music.load("1-14 GREEN GREENS (Kirby's Dream Land).mp3")
    elif m == 3:
        pygame.mixer.music.load("3 - Survive the Fall.mp3")
    elif m == 4:
        pygame.mixer.music.load("01 Home.mp3")
    elif m == 5:
        pygame.mixer.music.load("06 Match Loading.mp3")
    elif m == 6:
        pygame.mixer.music.load("Die For You ft. Grabbitz Instrumental.mp3")
    elif m == 7:
        pygame.mixer.music.load("2 - Fall 'N' Roll.mp3")
    elif m == 8:
        pygame.mixer.music.load("Among Us Drip.mp3")
    pygame.mixer.music.play(-1)

def gameend():
    screen.fill(black)
    wallpaper = pygame.image.load("among-us-wallpaper.jpg")
    wallpaper = pygame.transform.scale(wallpaper, (900, 500))
    screen.blit(wallpaper, (0, 0))
    defeat = gamefont.render('Mission', True, (255, 0, 100))
    defeatRect = defeat.get_rect()
    defeatRect.center = (X / 2, Y / 4)
    screen.blit(defeat, defeatRect)
    defeat2 = gamefont.render('Failed', True, (255, 0, 100))
    defeat2Rect = defeat2.get_rect()
    defeat2Rect.center = (X / 2, Y / 2)
    screen.blit(defeat2, defeat2Rect)
    pygame.display.flip()
    pygame.mixer.music.pause()
    randomint = random.randint(0, 1)
    if randomint == 0:
        pygame.mixer.music.load("Impostor Kill.mp3")
    elif randomint == 1:
        pygame.mixer.music.load("2-08 Too Bad.mp3")
    pygame.mixer.music.play()

def gamevictory():
    screen.fill(black)
    wallpaper = pygame.image.load("among-us-wallpaper.jpg")
    wallpaper = pygame.transform.scale(wallpaper, (900, 500))
    screen.blit(wallpaper, (0, 0))
    victory = gamefont.render('Mission', True, (0, 255, 150))
    victoryRect = victory.get_rect()
    victoryRect.center = (X / 2, Y / 4)
    screen.blit(victory, victoryRect)
    victory2 = gamefont.render('Success', True, (0, 255, 150))
    victory2Rect = victory2.get_rect()
    victory2Rect.center = (X / 2, Y / 2)
    screen.blit(victory2, victory2Rect)
    pygame.display.flip()
    pygame.mixer.music.pause()
    randomint = random.randint(0, 3)
    if randomint == 0:
        pygame.mixer.music.load("Victory Crew.mp3")
    elif randomint == 1:
        pygame.mixer.music.load("09 Victory.mp3")
    elif randomint == 2:
        pygame.mixer.music.load("2-07 Congratulations!.mp3")
    elif randomint == 3:
        pygame.mixer.music.load("6 - Didn't Fall! (You Win).mp3")
    pygame.mixer.music.play()
    

def setup():
    screen.fill(spacecolor)
    background = pygame.image.load("background.jfif")
    screen.blit(background, (0, 0))
    

start()
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_m:
                if gamemode != 2:
                    if m == False:
                        m = True
                        pygame.mixer.music.set_volume(0)
                    elif m == True:
                        m = False
                        pygame.mixer.music.set_volume(0.7)
        elif event.type == ADDENEMY and gamemode == 1:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == pygame.QUIT:
                    running = False
            
        if gamemode == 0:
            if event.type == KEYDOWN:
                if event.key == K_e:
                    gamemode = 100
                if event.key == K_LEFT:
                    gamemode = 1
                    loading = pygame.image.load("among-us-loading.jpg")
                    loading = pygame.transform.scale(loading, (900, 500))
                    screen.blit(loading, (0, 0))
                    pygame.display.flip()
                elif event.key == K_RIGHT:
                    gamemode = 2
                    loading = pygame.image.load("among-us-loading.jpg")
                    loading = pygame.transform.scale(loading, (900, 500))
                    screen.blit(loading, (0, 0))
                    pygame.display.flip()
                elif event.key == K_DOWN:
                    if mcycle != 8:
                        mcycle += 1
                    else:
                        mcycle = 0
                    musiccycle(mcycle)
                    
    #You found the easter egg!
    if gamemode == 100:
        setup()
        hiddentext = font.render("You found the easter egg!", True, black, white)
        hiddenRect = hiddentext.get_rect()
        hiddenRect.center = (X / 2, Y / 2)
        screen.blit(hiddentext, hiddenRect)
        endlesstext = font.render("You have unlocked endless mode!", True, black, white)
        endlessRect = endlesstext.get_rect()
        endlessRect.center = (X / 2, Y / 3 * 2)
        screen.blit(endlesstext, endlessRect)
        pygame.display.flip()
        lives = 100
        count = 100
        pygame.mixer.music.pause()
        pygame.mixer.music.load("Never Gonna Give You Up Original.mp3")
        pygame.mixer.music.play(-1)
        time.sleep(5)
        gamemode = 1
    
    if gamemode == 1:
        setup()
        if count == 0:
            musicstart()
            count += 1
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        l = str(lives)
        livestext = font.render("Lives: " + l, True, white)
        livesRect = livestext.get_rect()
        livesRect.center = (80, 30)
        screen.blit(livestext, livesRect)
        scoretext = font.render("Score: " + str(score), True, white)
        scoreRect = scoretext.get_rect()
        scoreRect.center = (300, 30)
        screen.blit(scoretext, scoreRect)

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        if pygame.sprite.spritecollideany(player, enemies):
            for sprite in enemies:
                if pygame.sprite.spritecollideany(player, enemies):
                    sprite.kill()
            lives -= 1
            if lives < 1:
                gameend()
                player.kill()
                time.sleep(3)
                running = False
        clock.tick(30)
        score += 2
        if count < 100 and score > 2000:
            gamevictory()
            player.kill()
            time.sleep(6)
            running = False
            
    if gamemode == 2:
        setup()
        if count == 0:
            musicstart()
            starttime = time.time()
            count += 1
        mfont = pygame.font.SysFont('comicsansms.', 32)
        ttext = mfont.render(typethis[wordlength-charcount:len(typethis)], True, black, white)
        tRect = ttext.get_rect()
        tRect.center = (X / 2, Y / 2)
        screen.blit(ttext,tRect)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if pygame.key.name(event.key) == typethis[wordlength-charcount:len(typethis)][0]:
                    charcount -= 1
                elif event.key == K_SPACE and " " == typethis[wordlength-charcount:len(typethis)][0]:
                    charcount -= 1
            elif event.type == pygame.QUIT:
                running = False

        if charcount < 1:
            endtime = time.time()
            t = round(endtime - starttime, 2)
            print("Time = " + str(t) + " seconds")
            print("Wordlength = " + str(wordlength) + " characters")
            wpm = round((wordlength / 5)/(t / 60))
            print("WPM = " + str(wpm))
            gamevictory()
            timetext = font.render("Words Per Minute: " + str(wpm), True, spacecolor, white)
            timeRect = timetext.get_rect()
            timeRect.center = (X / 2, Y / 3 * 2)
            screen.blit(timetext, timeRect)
            pygame.display.flip()
            time.sleep(6)
            running = False
    
    pygame.display.flip()
pygame.quit()

