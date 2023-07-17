import os

from mykit.kit.utils import printer


def custom_constants_sass(dock, color_hue):
    printer(f'DEBUG: Rewriting /_sass/constants.sass file.')

    text = f'$color-hue: {max(0, min(359, color_hue))};'
    with open(os.path.join(dock, '_sass', 'constants.sass'), 'w') as f:
        f.write(text)