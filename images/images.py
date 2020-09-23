from PIL import Image, ImageFilter

if __name__ == "__main__":
    image = Image.open(r'images\pokemons\bulbasaur.jpg')

    grey_filter = image.convert('L')
    blur_filter = image.filter(ImageFilter.BLUR)

    blur_filter.show()
    grey_filter.show()
