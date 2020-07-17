"""
File: darker.py
Author: Chenoa Yorgason (a Summer 2020 CS 106A student!)
Sources to learn more:
Research paper: https://solomonmg.github.io/pdf/HSVmetricsCampaignsDarknessPOQFINAL.pdf
Press coverage: https://www.washingtonpost.com/news/wonk/wp/2015/12/29/obamas-skin-looks-a-little-different-in-these-gop-campaign-ads/
----------------
Studies in political science have shown that individuals (particularly
whites) approve less of political figures like Obama when presented with a
darker-skinned image of the political figure. A research question that I'm
interested in involves political attitudes towards abortion when the circumstances of
the woman interested in the abortion varies (including her race). A common problem in this kind of
experimental work is ensuring that the respondent understands that an experimental frame belongs to
a particular race, without being super overt and cueing them into knowing that the study is explicitly about
race (as they'll try to not appear racially biased if this is known). Including a picture is often a good solution,
however, there are additional biases that can arise if pictures of different people are presented: do we like
candidate A because candidate A is old and looks venerable or do we like candidate A because candidate B is a woman
and we have biases against women?

This can be partially combated by presenting the same image but with one kind of change. If we give half the
respondents candidate A (light skinned) and half the respondents candidate A' with darker skin but all the same
features otherwise, we can attribute the difference in opinion about A vs A' to be about skin tone.

Images are mostly taken from the Chicago Face Database (Ma, Correll, Wittenbrink 2015), aside from the one Obama image.
Because I'm interested in attitudes about abortion, I've chosen mostly young women.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage
import os
import PIL


def highlight_img(filename):
    """
    This function should highlight the "red" pixels in the image passed in
    and grayscale all other pixels in the image in order to highlight areas
    of wildfires.

    Input:
        filename (string): name of image file to be read in

    Returns:
        highlighted image with "sufficiently red" pixels highlighted
    """
    image = SimpleImage(filename)

    for pixel in image:

        in_red = pixel.red >= 90 and pixel.red <= 260
        in_green = pixel.green >= 40 and pixel.green <= 200
        in_blue = pixel.blue >= 20 and pixel.blue <= 160

        if in_red and in_green and in_blue:
            pixel.red = .85 * pixel.red
            pixel.blue = .85 * pixel.blue
            pixel.green = .85 * pixel.green
        else:
            pixel.red = pixel.red
            pixel.blue = pixel.blue
            pixel.green = pixel.green


    return image


def main():
    """
    works for all files in 'darker' folder.
    for convenience, only 3 are done, but they should all work
    """

    original_img = SimpleImage('darker/test4.jpg')
    original_img.show()
    highlighted_img = highlight_img('darker/test4.jpg')
    highlighted_img.show()

    original_img = SimpleImage('darker/test10.jpg')
    original_img.show()
    highlighted_img = highlight_img('darker/test10.jpg')
    highlighted_img.show()

    original_img = SimpleImage('darker/test2.jpg')
    original_img.show()
    highlighted_img = highlight_img('darker/test2.jpg')
    highlighted_img.show()

if __name__ == '__main__':
    main()
