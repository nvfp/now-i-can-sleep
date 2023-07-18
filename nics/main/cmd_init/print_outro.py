

def print_outro(load, dock, gh_username, gh_repo_name):
    text = f"""
Almost done, now you need to do these final steps:
1. Create {dock} branch
   - git add .
   - git commit -m "NICS init"
   - git checkout --orphan {dock}
   - git rm -rf .
   - git commit --allow-empty -m init
   - git push origin {dock}
2. Activate the GitHub Pages
   - Visit https://github.com/{gh_username}/{gh_repo_name}/settings/pages
   - Under 'Build and deployment' section,
     - For 'Source', select 'Deploy from a branch'
     - For 'Branch', select '{dock}' branch
     - Click the 'Save' button
3. Back to {load} branch
   - git checkout {load}
   - git push

That's it! The documentation will be at https://{gh_username}.github.io/{gh_repo_name} ."""
    print(text)