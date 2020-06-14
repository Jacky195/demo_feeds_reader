NEW_LINE=$'\n'
MY_ENV_DEV="development"
MY_ENV_STAG="staging"
MY_ENV_PROD="production"

./_remove_nonetag.sh

echo "--------------+++++ Environment: ${MY_CUSTOM_ENV_DOCKER} +++++--------------"


echo "${NEW_LINE}${NEW_LINE}--------------+++++ ${MY_CUSTOM_ENV_DOCKER}: Docker-Compose DOWN +++++--------------"
if [ "$MY_CUSTOM_ENV_INITIAL" == true ]
then
    ./_compose_down.sh
    echo "${NEW_LINE}${NEW_LINE}--------------+++++ ${MY_CUSTOM_ENV_DOCKER}: Removing old Database +++++--------------"
    rm -rf ./postgres/${MY_CUSTOM_ENV_DOCKER}/mounted/data/*
    touch ./postgres/${MY_CUSTOM_ENV_DOCKER}/mounted/data/.gitkeep
else
     ./_compose_down.sh
fi


echo "${NEW_LINE}${NEW_LINE}--------------+++++ ${MY_CUSTOM_ENV_DOCKER}: Docker-Compose UP +++++--------------"
COMPOSE_HTTP_TIMEOUT=300 docker-compose -f ./docker-compose.${MY_CUSTOM_ENV_DOCKER}.yml up -d --build





if [ "$MY_CUSTOM_ENV_INITIAL" == true ]
then
    echo "${NEW_LINE}${NEW_LINE}--------------+++++ ${MY_CUSTOM_ENV_DOCKER}: Sleep 15s before initializing database +++++--------------"
    sleep 15
    docker exec feeds_reader_server_${MY_CUSTOM_ENV_DOCKER} bash -c 'python /opt/app/manage.py makemigrations && python /opt/app/manage.py migrate'
    sleep 5
    docker restart feeds_reader_server_${MY_CUSTOM_ENV_DOCKER}
fi




echo "${NEW_LINE}${NEW_LINE}--------------+++++ ${MY_CUSTOM_ENV_DOCKER}: Docker-Compose LOGGING +++++--------------"
docker-compose -f ./docker-compose.${MY_CUSTOM_ENV_DOCKER}.yml logs -f feeds_reader_client_${MY_CUSTOM_ENV_DOCKER} > ../logs/${MY_CUSTOM_ENV_DOCKER}/dc_services/feeds_reader_client.log &
docker-compose -f ./docker-compose.${MY_CUSTOM_ENV_DOCKER}.yml logs -f feeds_reader_pgadmin_${MY_CUSTOM_ENV_DOCKER} > ../logs/${MY_CUSTOM_ENV_DOCKER}/dc_services/feeds_reader_pgadmin.log &
docker-compose -f ./docker-compose.${MY_CUSTOM_ENV_DOCKER}.yml logs -f feeds_reader_server_${MY_CUSTOM_ENV_DOCKER} > ../logs/${MY_CUSTOM_ENV_DOCKER}/dc_services/feeds_reader_server.log &
docker-compose -f ./docker-compose.${MY_CUSTOM_ENV_DOCKER}.yml logs -f feeds_reader_database_${MY_CUSTOM_ENV_DOCKER} > ../logs/${MY_CUSTOM_ENV_DOCKER}/dc_services/feeds_reader_database.log &


echo "${NEW_LINE}${NEW_LINE}--------------+++++ ${MY_CUSTOM_ENV_DOCKER}: Done, it's good to go :) "
