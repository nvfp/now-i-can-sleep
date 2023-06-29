from mykit.kit.utils import printer


def update_footer(D_FOOTER, show_credit):

    text = (
        '<footer>'
            '<p id="copyright">&copy; {{ "now" | date: "%Y" }} {{ site.author.name }}</p>'
    )
    if show_credit:
        text += '<p id="credit">built with <a href="https://github.com/nvfp/now-i-can-sleep">now-i-can-sleep</a></p>'
    text += '</footer>'

    with open(D_FOOTER, 'w') as f: f.write(text)
    printer(f'INFO: Updated footer {repr(D_FOOTER)}.')