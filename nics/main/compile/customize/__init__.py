from nics.main.compile.customize.custom_config_yml import custom_config_yml


def customize_template_with_user_data(container, dock, cfg):

    ## /_includes/nav.html
    rewrite_nav_html()

    ## /_sass/constants.sass
    rewrite_constants_sass()

    ## /assets/images/favicon.svg or favicon.png
    rewrite_favicon()

    ## /pages/404/index.md
    rewrite_404()

    ## /pages/home/index.md
    rewrite_home()

    ## /pages/tree/
    rewrite_docs_tree()

    ## /_config.yml
    custom_config_yml(dock, cfg)