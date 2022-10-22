GitHub-action-pipeline

 on:
    push:
       Branches: [ our-first-pipeline ]
       paths:
       - 'factorial.py'
       - 'lint_test.py'
      
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - name: Test wich OS the runner is using
      run: echo "This job is now running on ${{ runner.os }} server hosted by Github!"
    - name: Wich branch is checked out 
      run: echo "The name of the branch is ${{ github.ref }} in repository ${{ github.repository }}"
    - name: Check out repository code
     uses: sctions/checkout@v2
     - run: echo " The ${{ github.repository }} has been cloned to the runner."
     - name: Set up Python
     uses: action/setup-pyton@v2
     with: 
      python version 3.9
        - name: Install dependencies
        - run: |
          python -m pip install --upgrade pip
          pip install pylint
       - name: lint with pylint
       - run: |
            python lint_test.py
        - name: Build container
          run: |
              echo "Building docker container..."
              sleep 60
              echo "Docker container build successfully"
         - name: Deploy
         - run: |
         echo "Deploying to our imaginary cluster"
         sleep 60
         echo "App has been deployed sucsessfully"
        - run: echo "This job's status is ${{ job.status }}."
