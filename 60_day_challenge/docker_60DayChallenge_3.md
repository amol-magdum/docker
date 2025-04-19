challenge 1: Making Docker Containers Production-Ready - multistage dockerfile
  - STEP : 1
    - create a dockerfile_5
    - command 
        - docker build -t flask-single-stage .
        - command :> docker images | grep flask-single-stage

  - STEP : 2
    - create multistage dockerfile_6
    - commands
        - docker build -t flask-multi-stage .
        - docker images | grep flask
  
  - Test the Optimized Image
      - docker run --rm -p 5000:5000 flask-multi-stage
      - curl http://localhost:5000

Challenge 2: Run a lightweight Alpine-based container (python:3.9-alpine or node:14-alpine).
    - create a alpine dockerfile_7
    - commands
        - docker build -t flask-alpine .
        - docker images | grep flask

challenge 3: Add a HEALTHCHECK in a Dockerfile for a web application (curl or wget).
    - Update the Dockerfile with HEALTHCHECK (dockerfile_8)
    - build image
        - docker build -t flask-app-healthcheck .
    - run container
        - docker run -d --name flask-container -p 5000:5000 flask-app-healthcheck
    - Verify Container Health Status
        - docker ps
















































































