#!/bin/bash
set -e
chmod 400 /var/lib/rabbitmq/.erlang.cookie

HOSTNAME=`env hostname`

/usr/local/bin/docker-entrypoint.sh rabbitmq-server -detached
sleep 5
rabbitmqctl wait /var/lib/rabbitmq/mnesia/rabbit\@$HOSTNAME.pid
rabbitmqctl stop_app
rabbitmqctl join_cluster rabbit@rabbit_node_1
rabbitmqctl start_app

tail -f /var/log/rabbitmq/*.log