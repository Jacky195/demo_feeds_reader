docker rmi -f $(docker images -qa -f 'dangling=true')
docker volume rm $(docker volume ls -qf dangling=true)