import pygame


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.astarx, self.astary = self.mid_w, self.mid_h + 30
        self.dijkx, self.dijky = self.mid_w, self.mid_h + 50
        self.bfsx, self.bfsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.astarx + self.offset, self.astary)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Astar (A*)", 20, self.astarx, self.astary)
            self.game.draw_text("Dijkstra", 20, self.dijkx, self.dijky)
            self.game.draw_text("Breath First Search", 20, self.bfsx, self.bfsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Astar (A*)':
                self.cursor_rect.midtop = (self.dijkx + self.offset, self.dijky)
                self.state = 'Dijkstra'
            elif self.state == 'Dijkstra':
                self.cursor_rect.midtop = (self.bfsx + self.offset, self.bfsy)
                self.state = 'Breath First Search'
            elif self.state == 'Breath First Search':
                self.cursor_rect.midtop = (self.astarx + self.offset, self.astary)
                self.state = 'Astar (A*)'
        elif self.game.UP_KEY:
            if self.state == 'Astar (A*)':
                self.cursor_rect.midtop = (self.bfsx + self.offset, self.bfsy)
                self.state = 'Breath First Search'
            elif self.state == 'Dijkstra':
                self.cursor_rect.midtop = (self.astarx + self.offset, self.astary)
                self.state = 'Astar (A*)'
            elif self.state == 'Breath First Search':
                self.cursor_rect.midtop = (self.dijkx + self.offset, self.dijky)
                self.state = 'Dijkstra'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Astar (A*)':
                self.game.playing = True
            elif self.state == 'Dijkstra':
                self.game.playing = True
            elif self.state == 'Breath First Search':
                self.game.playing = True
            self.run_display = False
