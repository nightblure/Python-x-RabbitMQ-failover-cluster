# Python x RabbitMQ failover cluster in Docker
Implementing a simple RabbitMQ failover cluster with load balancer HAProxy in Docker

**Commands** (from **cmd** or **container terminal** without ```docker exec -it <container_name> <command>```):

**Up** docker-containers: ```docker-compose up -d```

**Connect** slave nodes to master node:
* ```rabbitmqctl stop_app```
* ```rabbitmqctl reset```
* ```rabbitmqctl join_cluster rabbit@rabbit_node_1```
* ```rabbitmqctl start_app```

Check the **status of the cluster nodes** using one of the following methods:
* **monitoring interface of HAProxy**: ```http://localhost:8100/```
* **rabbitmq monitoring interface**: ```http://localhost:15672/```
* any **node's terminal**: ```rabbitmqctl cluster_status```

---

## Commands:

* Install **nano**: ```apk add nano``` or ```apt-get install nano```

* Get **erlang-cookie** value: ```cat /var/lib/rabbitmq/.erlang.cookie```

---

## Links:

* [Testing](https://www.youtube.com/watch?v=aLhRP_PsD5Y&list=WL&index=18&t=752s&ab_channel=bigtown2012)

* [Manual RMQ cluster deploy](https://www.youtube.com/watch?v=vWLbvVPMfqk&list=WL&index=17&ab_channel=bigtown2012)

* [Deploy RMQ cluster in Docker](https://www.youtube.com/watch?v=FzqjtU2x6YA&list=WL&index=26&t=2s&ab_channel=ThatDevOpsGuy)



