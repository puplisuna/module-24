import os
import random
import pygame

class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if (self.x < mouse_pos[0] < self.x + self.width) and (self.y < mouse_pos[1] < self.y + self.height):
            return True
        return False

class RpsGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("RPS Smasher")

        base = os.path.dirname(__file__)

        def safe_load_image(filename, size=None):
            path = os.path.join(base, filename)
            try:
                img = pygame.image.load(path).convert_alpha()
                if size:
                    img = pygame.transform.smoothscale(img, size)
                return img
            except Exception:
                # placeholder transparent surface if missing
                w, h = size if size else (200, 100)
                surf = pygame.Surface((w, h), flags=pygame.SRCALPHA)
                surf.fill((100, 100, 100, 180))
                return surf

        # Background and assets (use the actual names in the folder)
        self.bg = safe_load_image("background.jpeg", (960, 640))

        # Button images (folder has names with spaces)
        self.r_btn = safe_load_image("rock button.png", (200, 100))
        self.p_btn = safe_load_image("paper button.png", (200, 100))
        self.s_btn = safe_load_image("scissors button.png", (200, 100))

        # Choice images
        self.choose_rock = safe_load_image("rock.png", (150, 150))
        self.choose_paper = safe_load_image("paper.png", (150, 150))
        self.choose_scissors = safe_load_image("scissors.png", (150, 150))

        # Buttons (positions match original layout)
        self.rock_btn = Button(20, 500, 200, 100)
        self.paper_btn = Button(330, 500, 200, 100)
        self.scissors_btn = Button(640, 500, 200, 100)

        self.font = pygame.font.Font(None, 90)
        self.small_font = pygame.font.Font(None, 40)
        self.title_text = self.font.render("RPS SMASHER", True, (255, 255, 255))

        self.pl_score = 0
        self.pc_score = 0
        self.p_option = None
        self.pc_random_choice = None

    def player(self):
        if self.rock_btn.clicked():
            self.p_option = "rock"
        elif self.paper_btn.clicked():
            self.p_option = "paper"
        elif self.scissors_btn.clicked():
            self.p_option = "scissors"
        return self.p_option

    def computer(self):
        option = ["rock", "paper", "scissors"]
        self.pc_random_choice = random.choice(option)
        return self.pc_random_choice

    def update_scores(self):
        pl = self.p_option
        pc = self.pc_random_choice
        if pl is None or pc is None:
            return
        if (pl == "rock" and pc == "paper") or (pl == "paper" and pc == "scissors") or (pl == "scissors" and pc == "rock"):
            self.pc_score += 1
        elif pl == pc:
            pass
        else:
            self.pl_score += 1

    def draw_choices(self):
        # Draw player's choice
        if self.p_option == "rock":
            self.screen.blit(self.choose_rock, (120, 200))
        elif self.p_option == "paper":
            self.screen.blit(self.choose_paper, (120, 200))
        elif self.p_option == "scissors":
            self.screen.blit(self.choose_scissors, (120, 200))

        # Draw computer's choice (same art used for PC for now)
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
        self.screen.blit(self.title_text, (330, 0))

    def draw_score(self):
        score_text = self.small_font.render(f"Player: {self.pl_score}   Computer: {self.pc_score}", True, (255, 255, 255))
        self.screen.blit(score_text, (300, 100))

    def game_loop(self):
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # if any button was clicked, set player choice, get computer choice and update scores
                    if self.rock_btn.clicked() or self.paper_btn.clicked() or self.scissors_btn.clicked():
                        self.player()
                        self.computer()
                        self.update_scores()

            clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    game = RpsGame()

game.game_loop()