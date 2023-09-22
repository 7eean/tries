import ascii_magic

image_path = "media/boquita.png"
ascii_art = ascii_magic.from_image(image_path)
ascii_art.to_terminal(columns=int(50))