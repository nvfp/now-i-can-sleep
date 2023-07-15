import os
import re

from mykit.kit.utils import printer


def update_header(C_TREE, D_HEADER, lowercase_the_url):
    ## reminder: index.md will not be included in the header

    text = (
        '<header>'
            '<h1>{{ page.title }}</h1>'
            '<div class="wrap">'
                '<button id="_root__nav">v Navigation</button>'
                '<div class="main" id="_root__nav-div">'
    )

    ## reminder: `base` is the X in foo.com/baseurl/{X}page
    ##           (e.g. nvfp.github.io/mykit/docs/guide/foo, then X='docs/guide/')
    def build_the_nested_divs_recursively(pth, base):
        out = ''

        for fd in sorted(os.listdir(pth)):  # reminder: the file/dir `fd` order in `pth` matters.
            fd_pth = os.path.join(pth, fd)

            if fd == 'index.md': continue  # index.md will not be shown in navigation bar
            if os.path.isfile(fd_pth) and (not fd.endswith('.md')): continue  # ignore non-markdown files

            res = re.match(r"^(?:\d+ - )?(?P<name>[\w \-'&\(\).]+?)(?:\.md)?$", fd)
            if res is None: raise AssertionError(f'Invalid docs-tree format: {repr(fd)}')
            name = res.group('name')
            url = name.replace(' ', '-').replace("'", '').replace('&', 'and').replace('(', '').replace(')', '').replace('.', '-')
            if lowercase_the_url: url = url.lower()
            printer(f'DEBUG: name: {repr(name)}; url: {repr(url)}')

            if os.path.isdir(fd_pth):
                out += f'<button id="{base.replace("/", "-")}{url}">> {name}</button>'  # remember to replace all slashes to hyphens
                out += f'<div class="child" id="{base.replace("/", "-")}{url}-div">'  # remember to replace all slashes to hyphens
                out += build_the_nested_divs_recursively(fd_pth, base+url+'/')
                out += '</div>'
            else:
                out += '<a href="{{ site.baseurl }}/' + f'{base}{url}">{name}</a>'
                printer(f'DEBUG: href {repr(name)} added.')

        return out
    text += build_the_nested_divs_recursively(C_TREE, '')

    text += (
                '</div>'
            '</div>'
        '</header>'
    )

    with open(D_HEADER, 'w') as f: f.write(text)
    printer(f'INFO: Updated header {repr(D_HEADER)}.')