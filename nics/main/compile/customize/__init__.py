from nics.main.compile.customize.custom_nav_html import custom_nav_html
from nics.main.compile.customize.custom_constants_sass import custom_constants_sass
from nics.main.compile.customize.custom_favicon import custom_favicon
from nics.main.compile.customize.custom_404page import custom_404page
from nics.main.compile.customize.custom_homepage import custom_homepage
from nics.main.compile.customize.custom_docs_tree import custom_docs_tree
from nics.main.compile.customize.custom_config_yml import custom_config_yml


def customize_template_with_user_data(container, dock, cfg):

    ## /_includes/nav.html
    custom_nav_html()

    ## /_sass/constants.sass
    custom_constants_sass(dock, cfg.color_hue)

    ## /assets/images/favicon.svg or favicon.png
    custom_favicon()

    ## /pages/404/index.md
    custom_404page()

    ## /pages/home/index.md
    custom_homepage()

    ## /pages/tree/
    custom_docs_tree()

    ## /_config.yml
    custom_config_yml(dock, cfg)