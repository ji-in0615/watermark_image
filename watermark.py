from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys,os

# def get_position(img,pos):
#     if pos == "topleft": return (0,0)
#     if pos == "bottomleft": return (0, img.size[1] - text.size[1])
#     if pos == "topright": return (img.size[0] - text.size[0] ,0)
#     if pos == "bottomright": return (img.size[0] - text.size[0] , img.size[1] - text.size[1])
#     if pos == "center": return ( (img.size[0] - text.size[0])/2 ,( img.size[1] - text.size[1])/2 )

def pictures_watermark(input_image_path, output_image_path, text, pos):
        count = 0
        files = os.listdir(input_image_path)
        extenstions = ['png', 'bmp', 'jpg', 'gif', 'jpeg']

        for filename in os.listdir(input_image_path):
            if any([filename.lower().endswith(ext) for ext in extenstions]) and filename:
                img = Image.open(input_image_path + '/' + filename).convert("RGBA")
                txt = Image.new('RGBA', img.size, (255,255,255,0))
                # txt = Image.new('RGBA', img.size, (0,0,0,0))
                font = ImageFont.truetype('./fonts/Roboto.ttf', 150)
                Draw = ImageDraw.Draw(txt)
                
                #text color, opacity adjustment
                Draw.text((10,10), text, fill=(255,255,255,70), font=font)
                
                #img, txt combine + save
                combined = Image.alpha_composite(img, txt)
                im = combined.convert('RGB')
                im.save(output_image_path + '/' + 'comb_' + filename)
                
                print('Added watermark to ' + output_image_path + '/' + filename)

if __name__ == "__main__":
    pictures_watermark("./images", "./output", 'watermark', 'center')
    # pictures_watermark("panda.png", "panda_comb.png", 'panda')

# run
# python watermark.py