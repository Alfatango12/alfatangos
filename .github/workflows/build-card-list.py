name: Update Banlist

on:
  push:
    branches: [ "main" ]
    paths:
      - 'banlist.txt' # Only run when banlist.txt is modified
  workflow_dispatch:

# Grant the action permission to push code back to the repo
permissions:
  contents: write

jobs:
  update-json:
    runs-on: ubuntu-latest

    steps:
    - name: Check out repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Execute Python script
      run: python carte.py

    # Commit and push the modified JSON file
    - name: Commit and push changes
      run: |
        # Set up a bot account to author the commit
        git config --global user.name 'github-actions[bot]'
        git config --global user.email 'github-actions[bot]@users.noreply.github.com'
        
        # Add the modified JSON file
        git add banlist.json
        
        # Commit the change. The "|| true" prevents the workflow from failing if the JSON didn't actually change
        git commit -m "Auto-update banlist.json from banlist.txt" || true
        
        # Push to the repository
        git push
