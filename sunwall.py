from datetime import datetime, date, time
from PIL import Image

SUNSCALE = 1/8

def generate(i: Image, t: time):
    '''
    Generate a sunwall image based on the given mode and time
    '''
    w, h = i.size
    sunsize = int(w * SUNSCALE)
    x = arc_x(t, w - sunsize)
    y = arc_y(x, w, h)
    sun = load_sun_image()
    i = i.convert('RGBA')
    sun = sun.resize((sunsize, sunsize), resample=0) 
    Image.Image.paste(i, sun, (int(x), int(y)), mask=sun)
    return i

def load_sun_image():
    return Image.open('img/sun_800.png')

def arc_x(t: time, w: int):
    x = None
    if 7 <= t.hour <= 19: #If the sun is up
        hour = t.hour - 7 
        divisor = w  / 12
        x = hour * divisor
    return x

def arc_y(x: int, w: int, h: int):
    '''
    Determine the 
    '''
    a = 1 / (w * 1.5) #Calculate the arc's scale based on the image width
    return a*(x-(w/2))**2 + (h/54) #Return the y-value of the arc at point x

def main():
    images = []
    image = Image.open('input.jpg')
    times = [time(7, 0), time(8, 0), time(9, 0), time(10, 0), time(11, 0), time(12, 0), time(13, 0), time(14, 0), time(15, 0), time(16, 0), time(17, 0), time(18, 0), time(19, 0)]
    for t in times:
        i = generate(image, t)
        i.save(f'out/output_{t.hour}.png')
        images.append(i)

if __name__ == '__main__':
    main()