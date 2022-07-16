import pygame
import sys


class Music():
    def __init__(self):
        self.songs = [pygame.mixer.Sound("Assets/Death of an Octopus.wav"),  pygame.mixer.Sound("Assets/Generation Music.mp3"), pygame.mixer.Sound("Assets/Melody Loop.mp3"), pygame.mixer.Sound("Assets/Peaceful Hip Hop.mp3"), pygame.mixer.Sound("Assets/Short Fairy Tale Trailer.wav")]
        self.curr_song = -1
        self.pause = False
        self.song_playing = False

    def play_song(self):
        self.songs[self.curr_song].play()


    def stop(self):
        self.songs[self.curr_song].stop()

class Interact(Music):
    def __init__(self):
        Music.__init__(self)
        # self.user_select = -1

    def display_list(self):
        font = pygame.font.Font("Assets/praysire/ttf/praysire-praysire-400.ttf", 10)
        songs_list = ["1. Death of an Octopus", "2. Generation Music", "3. Melody Loop", "4. Peaceful Hip Hop",
                      "5. Short Fairy Tale Trailer"]
        label = []
        rect = []

        for song in range(len(songs_list)):
            label.append(font.render(songs_list[song], False, (0, 0, 0)))

        for k in range(len(label)):
            rect.append(label[k].get_rect(center=(WIDTH / 4, 160 + (k * 20))))

        for w in range(len(rect)):
            screen.blit(label[w], rect[w])

    def user_selection_font(self):
        font = pygame.font.Font("Assets/praysire/ttf/praysire-praysire-400.ttf", 10)
        font_render = font.render("Press the corresponding number on your keyboard to select a song.", False, "#F07A90")
        font_rect = font_render.get_rect(center=(WIDTH/2, 350))
        screen.blit(font_render, font_rect)

    def user_selection(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.curr_song = 0
            self.song_playing = True
        elif keys[pygame.K_2]:
            self.curr_song = 1
            self.song_playing = True
        elif keys[pygame.K_3]:
            self.curr_song = 2
            self.song_playing = True
        elif keys[pygame.K_4]:
            self.curr_song = 3
            self.song_playing = True
        elif keys[pygame.K_5]:
            self.curr_song = 4
            self.song_playing = True
    def draw(self):
        tree = pygame.image.load("Assets/sakura.png")
        tree = pygame.transform.scale(tree, (80, 80))
        screen.blit(tree, (WIDTH/2,150))

        play_button = pygame.image.load("Assets/play-button.png")
        play_button = pygame.transform.scale(play_button, (50, 50))
        play_button_rect = play_button.get_rect(center=(100, 50))

        pause_button = pygame.image.load("Assets/pause.png")
        pause_button = pygame.transform.scale(pause_button, (50, 50))
        pause_button_rect = pause_button.get_rect(center=(100, 50))

        stop_button = pygame.image.load("Assets/stop-button.png")
        stop_button = pygame.transform.scale(stop_button, (50, 50))
        stop_button_rect = stop_button.get_rect(center=(200, 50))

        print(str(self.song_playing))
        # Draws either play or pause
        if self.song_playing == False:
            screen.blit(play_button, play_button_rect)
        elif self.pause:
            screen.blit(play_button, play_button_rect)

        else:
            screen.blit(pause_button, pause_button_rect)

        screen.blit(stop_button, stop_button_rect)

        if not self.curr_song == -1 and self.song_playing:
            self.play_song()


        self.display_list()
        self.user_selection_font()
        self.user_selection()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if play_button_rect.collidepoint(pos):
                    if self.pause == False:
                        self.pause = True
                        pygame.mixer.pause()
                    else:
                        self.pause = False
                        pygame.mixer.unpause()
                if stop_button_rect.collidepoint(pos):
                    self.song_playing = False
                    self.songs[self.curr_song].stop()
                    pygame.mixer.stop()


# Window Setup
pygame.init()
WIDTH = 400
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

interact = Interact()



def main():
    while True:
        clock.tick(30)
        screen.fill((255, 255, 255))

        interact.draw()
        pygame.display.update()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


