
from nics.main.utils.favicon_maker import create_favicon_svg_file
from nics.main.compile.customize.custom_config_yml import custom_config_yml


def customize_template_with_user_data(container, dock, cfg):

    ## Rewrite nav.html in _includes
    rewrite_nav_html()

    ## Rewrite constants.sass in _sass
    rewrite_constants_sass()

    ## 
    rewrite_favicon()

    ## Rewrite 404 page in pages/404/index.md
    rewrite_404()

    ## Rewrite homepage in pages/home/index.md
    rewrite_home()

    ## Rewrite the pages/tree/
    rewrite_docs_tree()

    ## Update _config.yml
    custom_config_yml(dock, cfg)