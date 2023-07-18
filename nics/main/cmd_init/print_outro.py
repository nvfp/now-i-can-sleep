

def print_outro():
    text = f"""
Almost done, now you need to do these final steps:
1. Create docs branch
   - git add .
   - git commit -m "NICS init"
   - git checkout --orphan docs
   - git rm -rf .
   - git commit --allow-empty -m init
   - git push origin docs
2. Activate the GitHub Pages
   - Visit https://github.com/{gh_username}/{gh_repo}/settings/pages
   - Under 'Build and deployment' section,
     - For 'Source', select 'Deploy from a branch'
     - For 'Branch', select 'docs' branch
     - Click the 'Save' button
3. Back to {main_branch_name} branch
   - git checkout {main_branch_name}
   - git push

That's it! The documentation will be at https://{gh_username}.github.io/{gh_repo} .
Visit https://nvfp.github.io/now-i-can-sleep/usage/init-command to visually see the final steps above."""
    print(text)