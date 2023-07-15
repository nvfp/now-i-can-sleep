from nics.main.compile.customize.custom_config_yml import custom_config_yml
from nics.main.compile.customize.custom_constants_sass import custom_constants_sass
from nics.main.compile.customize.custom_favicon import custom_favicon


def customize_template_with_user_data(container, dock, cfg):

    ## /_includes/nav.html
    custom_nav_html()

    ## /_sass/constants.sass
    custom_constants_sass(dock, cfg.color_hue)

    ## /assets/images/favicon.svg or favicon.png
    custom_favicon()

    ## /pages/404/index.md
    custom_404()

    ## /pages/home/index.md
    custom_home()

    ## /pages/tree/
    custom_docs_tree()

    ## /_config.yml
    custom_config_yml(dock, cfg)