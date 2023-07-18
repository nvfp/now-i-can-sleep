import logging


logger = logging.getLogger(__name__)


def create_favicon_svg_file(file_path, hue):
    logger.debug('Writing favicon.svg file.')

    ## The SVG is from https://feathericons.com/
    svg = f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="hsl({hue}, 65%, 83%)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
        <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
    </svg>
    """
    with open(file_path, 'w') as f:
        f.write(svg)

    logger.debug(f'Done, created at {repr(file_path)}.')