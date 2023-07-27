Pending features:
- coloring_type: Allows users to choose the coloring style for the pages (with three options: full, signature, and template). Currently, only the 'signature' option is being used.
- container name: currently, container folder must be named "docs" and placed at root
- dock name: currently, target branch must be named "docs"
- Handle lowercase URL: Redirect `foo.github.io/REPO/my-lib-case-sensitive` to `foo.github.io/REPO/My-LIB-Case-Sensitive`.
- If a favicon is not specified, the default favicon will be used.


Note:
- Code within the `nics_compiler/` folder can use code from `nics/` folder. However, code within `nics/` folder shouldn't access code outside `nics/` folder, as it's a distribution package for users.