Challenge 1: Create a custom bridge network and connect two containers (alpine and nginx)
  - create a network :> docker network create my-custom-network
  - Nginx Container on the Custom Network :> docker run -d --name nginx-container --network my-custom-network nginx
  - Alpine Container on the Same Network :> docker run -it --rm --name alpine-container --network my-custom-network alpine sh
  - test connection alpine to nginx :> 
        - apk add --no-cache curl
        - curl nginx-container
  - inspect the network to check attached containers :> docker network inspect my-custom-network

Challenge 2: Run a MySQL container with a named volume and confirm data persistence
  - create volumn: docker volume create mysql_data
  - create MySQL container with the Named Volume
    docker run -d --name mysql-container \
    -e MYSQL_ROOT_PASSWORD=rootpass \
    -e MYSQL_DATABASE=mydb \
    -v mysql_data:/var/lib/mysql \
    -p 3306:3306 \
     mysql:latest

  - Verify Data Persistence
      docker exec -it mysql-container mysql -uroot -prootpass -e "CREATE TABLE mydb.users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));"
      docker exec -it mysql-container mysql -uroot -prootpass -e "INSERT INTO mydb.users (name) VALUES ('Alice'), ('Bob');"
      docker exec -it mysql-container mysql -uroot -prootpass -e "SELECT * FROM mydb.users;"
  
  - delete and create db using same volumn and verify data persistance
      docker stop mysql-container
      docker rm mysql-container
      docker run -d --name mysql-container \
        -e MYSQL_ROOT_PASSWORD=rootpass \
        -e MYSQL_DATABASE=mydb \
        -v mysql_data:/var/lib/mysql \
        -p 3306:3306 \
        mysql:latest
      docker exec -it mysql-container mysql -uroot -prootpass -e "SELECT * FROM mydb.users;"

Challenge 3: docker-compose.yml for Flask API and PostgreSQL
    - create flask-api.py file
    - create dockerfile_4
    - write docker-compose.yml file
    - run compose file :> docker-compose up -d
    
    verify the containers
    - curl http://localhost:5000/
    - curl http://localhost:5000/db-status

Challenge 5: Deploy a WordPress site using Docker Compose (WordPress + MySQL)