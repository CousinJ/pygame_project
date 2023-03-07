import pygame
import UI
import settings


def main():

    screen = settings.screen
    center_x = settings.WINDOW_WIDTH // 2
    center_y = settings.WINDOW_HEIGHT // 2

    #setting variable of instantiated UI button class. params are (x pos, y pos, color)
    my_button1 = UI.Button(center_x - (UI.Button.width //2), center_y - (UI.Button.height //2) , (250, 20, 100))
    my_button2 = UI.Button(center_x - (UI.Button.width //2), center_y - (UI.Button.height //2) + 200, (0, 170, 40) )

    bg_p1 = UI.BackGround("./assets/parallax-mountain-bg.png")
    bg_p2 = UI.BackGround("./assets/parallax-mountain-montain-far.png")
    bg_p3 = UI.BackGround("./assets/parallax-mountain-mountains.png")


    my_title = UI.Title(settings.font_color, settings.font_path, settings.font_size, settings.title_text, settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT // 5)

    #array of bg components
    my_bg = [bg_p1, bg_p2, bg_p3, ]

    def render_bg():
        for i in range(3):
            my_bg[i].resize(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
            my_bg[i].draw(screen)



    #static renders

    render_bg()
    my_button1.draw(screen)
    my_button2.draw(screen)
    my_title.draw(screen)

    #update
   