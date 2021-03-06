import argparse

from kafka.tools.assigner.models.broker import Broker
from kafka.tools.assigner.models.cluster import Cluster
from kafka.tools.assigner.models.topic import Topic


def set_up_cluster():
    cluster = Cluster()
    cluster.add_broker(Broker(1, "brokerhost1.example.com"))
    cluster.add_broker(Broker(2, "brokerhost2.example.com"))
    cluster.add_topic(Topic("testTopic1", 2))
    cluster.add_topic(Topic("testTopic2", 2))
    partition = cluster.topics['testTopic1'].partitions[0]
    partition.add_replica(cluster.brokers[1], 0)
    partition.add_replica(cluster.brokers[2], 1)
    partition = cluster.topics['testTopic1'].partitions[1]
    partition.add_replica(cluster.brokers[2], 0)
    partition.add_replica(cluster.brokers[1], 1)
    partition = cluster.topics['testTopic2'].partitions[0]
    partition.add_replica(cluster.brokers[2], 0)
    partition.add_replica(cluster.brokers[1], 1)
    partition = cluster.topics['testTopic2'].partitions[1]
    partition.add_replica(cluster.brokers[1], 0)
    partition.add_replica(cluster.brokers[2], 1)
    return cluster


def set_up_subparser():
    aparser = argparse.ArgumentParser(prog='kafka-assigner', description='Rejigger Kafka cluster partitions')
    subparsers = aparser.add_subparsers(help='Select manipulation module to use')
    return (aparser, subparsers)
