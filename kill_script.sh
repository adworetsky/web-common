#!/bin/bash
# This is hacky kill script for docker-compose for Docker 17
# Unfortunately, it can take up to 2-3 minutes to kill the containers...
echo "Removing Containers..."
echo "The below command will take ~45 seconds to complete and error out. This is expected."
docker-compose down
echo "The below command will take ~45 seconds to complete and error out. This is expected."
docker-compose down
docker network disconnect -f web-common_main web-common-gunicorn-1
docker network disconnect -f web-common_main web-common-postgres-1
docker-compose down
