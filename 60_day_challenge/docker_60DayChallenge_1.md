Install docker 
  - sudo apt update
  - sudo apt install apt-transport-https ca-certificates curl software-properties-common
  - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  - sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
  - apt-cache policy docker-ce
  - sudo apt install docker-ce

check the docker service is running
  - sudo systemctl status docker
    IF service INACTIVE
  - sudo systemctl start docker

Add docker to sudo group to avoid typing sudo with docker commands
  - sudo usermod -aG docker ${USER}
  - su - ${USER}
  to check if user added to group
  - groups

* RUN your first docker program using nginx
  - docker run -d -p 80:80 nginx
  - check localhost:80

