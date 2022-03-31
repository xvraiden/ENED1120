from ev3dev2.display import Display

#show the text as input
def Draw(text):
    m_Display = Display()

    m_Display.text_grid(text, True, 0, 6)