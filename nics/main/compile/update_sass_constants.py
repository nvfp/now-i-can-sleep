from mykit.kit.utils import printer


def update_sass_constants(D_SASS_CONSTANTS, color_hue):

    text = f'$hue-signature: {color_hue};'
    with open(D_SASS_CONSTANTS, 'w') as f: f.write(text)
    printer(f'INFO: Updated sass constants {repr(D_SASS_CONSTANTS)}.')