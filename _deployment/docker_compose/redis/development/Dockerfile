FROM redis:6.0.1
RUN mkdir -p /var/log/redis/ && touch /var/log/redis/redis-server.log && chmod -R 777 /var/log/redis
CMD ["redis-server", "--include /usr/local/etc/redis/redis.conf"]