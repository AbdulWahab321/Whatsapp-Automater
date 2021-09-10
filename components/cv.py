from msgboxpy import *
from PIL import Image
import os

def get_id_from_invite_link(invite_link=""):
    if "https://chat.whatsapp.com/" not in invite_link:
        alert("Incorrect Invite Link",Styles.Icons.ICON_ERROR," IILx255")
    else:    
        invite_link = invite_link.replace("https://chat.whatsapp.com/","")
        return invite_link



def image_to_ascii_art(img_path: str,output_path: str, output_file: str = "pywhatkit_asciiart") -> str:
    """Converts the given image to ascii art and save it to output_file"""

    # pass the image as command line argument
    img = Image.open(img_path)

    # resize the image
    width, height = img.size
    aspect_ratio = height / width
    new_width = 80
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    # new size of image
    # print(img.size)

    # convert image to greyscale format
    img = img.convert('L')

    pixels = img.getdata()

    # replace each pixel with a character from array
    chars = ["*", "?", ".", "#", "!", "@", "$", "&", "%", "~", "`"]
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to the new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width]
                   for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    if os.path.exists(output_path):
        output = os.path.join(output_path,output_file)
        if output.endswith(".txt"):
            with open(f"{output}", "w") as f:
                f.write(ascii_image)
        else:
            with open(f"{output}.txt", "w") as f:
                f.write(ascii_image)     
        return ascii_image        
    else:
        alrt = alert("Given Path does not exists, Do you want to make Directories along the way if it doesn't exists?",Styles.Buttons.OK_CANCEL|Styles.Icons.ICON_QUESTION,"PTHX2D7")
        if alrt == "yes":
            os.makedirs(output_path)
            output = os.path.join(output_path,output_file)
            if output.endswith(".*"):
                with open(f"{output}", "w") as f:
                    f.write(ascii_image)
            else:
                with open(f"{output}.txt", "w") as f:
                    f.write(ascii_image)                                      
            return ascii_image