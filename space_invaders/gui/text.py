#draws text on given surface
def draw_text(surface,text,font,text_color,x,y):
    image = font.render(text,True,text_color)
    surface.blit(image,(x, y))