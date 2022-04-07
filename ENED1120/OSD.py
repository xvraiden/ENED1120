from ev3dev2.display import Display
import ev3dev2.fonts as fonts


#show the text as input
def Draw(text):
    m_Display = Display()

    m_Display.text_grid(text, True, 0, 6, 'black', font=fonts.load('charB124'))