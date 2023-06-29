


def rewrite_the_footer(footer_pth, show_credit):

    text = (
        '<footer>'
            '<p id="copyright">&copy; {{ "now" | date: "%Y" }} {{ site.author.name }}</p>'
    )
    if show_credit:
        text += '<p id="credit">built with <a href="https://github.com/nvfp/now-i-can-sleep">now-i-can-sleep</a></p>'
    text += '</footer>'

    with open(footer_pth, 'w') as f:
        f.write(text)