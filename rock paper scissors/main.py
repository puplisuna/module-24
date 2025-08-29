import random
import pygame

print("welcome to my rockpaper scissors game")
print("you will be playing against the computer")

class Button:
    def __init__(self, color, x, y, width, height, name):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name

    def clicked(self, mouse_pos=None):
        if mouse_pos is None:
            mouse_pos = pygame.mouse.get_pos()
        return (self.x < mouse_pos[0] < self.x + self.width) and (self.y < mouse_pos[1] < self.y + self.height)


class RPSGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("rps smasher")

        # load images (may raise if files missing)
        self.bg = pygame.image.load("background.jpeg").convert()
        self.r_btn = pygame.image.load("rock button.png").convert_alpha()
        self.p_btn = pygame.image.load("paper button.png").convert_alpha()
        self.s_btn = pygame.image.load("scissors button.png").convert_alpha()
        self.choose_rock = pygame.image.load("rock.png").convert_alpha()
        self.choose_paper = pygame.image.load("paper.png").convert_alpha()
        self.choose_scissors = pygame.image.load("scissors.png").convert_alpha()

        # buttons (positions and sizes should match your images)
        self.rock_btn = Button((255, 0, 0), 20, 500, 250, 80, "rock")
        self.paper_btn = Button((0, 255, 0), 330, 500, 250, 80, "paper")
        self.scissors_btn = Button((0, 0, 255), 640, 500, 250, 80, "scissors")

        # fonts and texts
        self.font = pygame.font.Font('freesansbold.ttf', 48)
        self.title_text = self.font.render('rock paper scissors', True, (0, 0, 0))
        self.small_font = pygame.font.Font('freesansbold.ttf', 24)

        # scores and choices
        self.player_score = 0
        self.computer_score = 0
        self.p_option = None
        self.pc_random_choice = None

    def player(self, mouse_pos):
        if self.rock_btn.clicked(mouse_pos):
            self.p_option = "rock"
        elif self.paper_btn.clicked(mouse_pos):
            self.p_option = "paper"
        elif self.scissors_btn.clicked(mouse_pos):
            self.p_option = "scissors"

    def computer(self):
        options = ["rock", "paper", "scissors"]
        self.pc_random_choice = random.choice(options)

    def update_scores(self):
        pl = self.p_option
        pc = self.pc_random_choice
        if pl is None or pc is None:
            return
        if pl == pc:
            return
        # cases where player loses
        if (pl == "rock" and pc == "paper") or (pl == "paper" and pc == "scissors") or (pl == "scissors" and pc == "rock"):
            self.computer_score += 1
        else:
            self.player_score += 1

    def draw_choices(self):
        # player choice on left
        if self.p_option == "rock":
            self.screen.blit(self.choose_rock, (120, 200))
        elif self.p_option == "paper":
            self.screen.blit(self.choose_paper, (120, 200))
        elif self.p_option == "scissors":
            self.screen.blit(self.choose_scissors, (120, 200))

        # computer choice on right
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
        self.screen.blit(self.title_text, (200, 20))

    def draw_score(self):
        score_text = self.small_font.render(f"Player: {self.player_score}   Computer: {self.computer_score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def game_loop(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    # set player choice based on click
                    self.player(pos)
                    # if a choice was made, pick for computer and update scores
                    if self.p_option is not None:
                        self.computer()
                        self.update_scores()

            self.image_reset()
            self.draw_score()
            self.draw_choices()
            pygame.display.update()
            clock.tick(30)

        pygame.quit()


if __name__ == "__main__":
    rps = RPSGame()
    rps.game_loop()