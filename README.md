# Docker-Postgres
## Deploying Postgres into Ec2 instance using Docker compose
### steps to achieve it manually without cloning to my repo
- Step 1: Clone the repo(git clone 
- Step 2: Creates a directory named docker-postgres and navigates into it.
- Step 3: Creates an empty docker-compose.yml file in the directory.
- Step 4: Open the docker-compose.yml file using a text editor (nano in this case).
- Step 5: Adds the PostgreSQL service configuration to the docker-compose.yml file.
- Step 6: Run the docker-compose command to start the PostgreSQL container

### Steps using my git repo :
- Step 1: Clone the repo(git clone 
- Step 2: Creates a directory named docker-postgres. Navigate into it.
- Step 3: Run the docker-compose.yaml file 
          (docker-compose up -d)
- Step 4: (docker ps -a) verify the container 

Note: Download and install docker-compose(if not installed)
- (sudo curl -L “https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose)
- (sudo chmod +x /usr/local/bin/docker-compose)
- (docker-compose --version) for verification


