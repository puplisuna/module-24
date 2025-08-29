import random
import pygame

print("welcome to my rockpaper scissors game")
print("you will be playing against the computer")

class button():
    def __init__(self, color, x, y, width, height, pos):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos

        def clicked(self, pos):
            mouse_pos = pygame.mouse.get_pos()
            if (self.x <mouse_pos[0] < self.x + self.width) and (self.y < mouse_pos[1] < self.y + self.height):
                return True
            return False
    
    class rpsgame():
        def __init__(self):
            pygame.init()
            self.screen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("rps smasher")
            self.bg = pygame.image.load("background.jpeg")
            self.r_btn = pygame.image.load("rock button.png").convert_alpha()
            self.p_btn = pygame.image.load("paper button.png").convert_alpha()
            self.s_btn = pygame.image.load("scissors button.png").convert_alpha()
            self.choose_rock = pygame.image.load("rock.png").convert_alpha()
            self.choose_paper = pygame.image.load("paper.png").convert_alpha()
            self.choose_scissors = pygame.image.load("scissors.png").convert_alpha()
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.r_btn, (20, 500))
            self.screen.blit(self.p_btn, (330, 500))
            self.screen.blit(self.s_btn, (640, 500))
            self.rock_button = button((255, 0, 0), 20, 500, 250, 80, "rock")
            self.paper_button = button((0, 255, 0), 330, 500, 250, 80, "paper")
            self.scissors_button = button((0, 0, 255), 640, 500, 250, 80, "scissors")
            self.font = pygame.font.Font('freesansbold.ttf', 90)
            self.text = self.font.render('rock paper scissors', True, (0, 0, 0))
            self.player_score = 0
            self.computer_score = 0
            self.p_option = None
            self.pc_random_choice = None

def player(self):
    if self.roch_button.clicked():
        self.p_option = "rock"
    elif self.paper_button.clicked():
        self.p_option = "paper"
    elif self.scissors_button.clicked():
        self.p_option = "scissors"
    return self.p_option

def computer(self):
    option = ["rock", "paper", "scissors"]
    pc_choice = random.choice(option)
    self.pc_random_choice = random.choice(option)
    self.pc_random_choice = pc_choice 
    return self.pc_random_choice 

def udate_scores(self):
    pl = self.p_option
    pc = self.pc_random_choice
    if (pl == "rock" and pc == "paper") or (pl == "paper" and pc == "scissors") or (pl == "scissors" and pc == "rock"):
    self.pc_score += 1
    elif pl == pc:
    pass
    else:
        self.player_score += 1
    

def draw_choices(self):
    if self.p_option == "rock":
        self.screen.blit(self.choose_rock, (120, 200))
    elif self.p_option == "paper":
        self.screen.blit(self.choose_paper, (120, 200))
    elif self.p_option == "scissors":
        self.screen.blit(self.choose_scissors, (120, 200))
    
    if self.pc_random_choice == "rock":
        self.screen.blit(self.choose_rock, (720, 200))
    elif self.pc_random_choice == "paper":
        self.screen.blit(self.choose_paper, (720, 200))
    elif self.pc_random_choice == "scissors":
        self.screen.blit(self.choose_scissors, (720, 200))




def image_reset(self):
    self.screen.blit(self.bg, (0, 0))
    self.screen.blit(self.r_btn, (20, 500))
    self.screen.blit(self.p_btn, (330, 500))
    self.screen.blit(self.s_btn, (640, 500))
    self.screen.blit(self.title text, (330, 100))

def draw_score(self):

score_text = self.small_font.render(f"Player: {self.pl_score} Computer: {self.pc_score}", True, (255, 255, 255))

self.screen.blit(score_text, (330, 100))

def game loop(self):
    run = True
    clock = pygame.time.Clock()
while run:
    self.image_reset()
    self.draw_score()
    self.draw_choices()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        f event.type == pygame.MOUSEBUTTONDOWN:

if self.rock_btn.clicked() or self.paper_btn.clicked() or self.scissors_btn.clicked():

self.player()

self.computer()

self.update_scores()

clock.tick(30)
    pygame.quit()


if __name__ == "__main__":
    rps = rpsgame()
    rps.game_loop()