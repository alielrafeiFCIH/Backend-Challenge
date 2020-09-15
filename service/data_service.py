#!/usr/bin/python
# -*- coding: utf-8 -*-
from data.coffee_machine import Coffee_machine
from data.Coffee_pods import Coffee_pod
from mongoengine.queryset.visitor import Q
import mongoengine


def add_new_machine(Product_type, Water_line, Product_code):
    coffee_machine = Coffee_machine()
    coffee_machine.Product_type = Product_type
    coffee_machine.Product_code = Product_code
    coffee_machine.Water_line = Water_line
    coffee_machine.save()


def add_new_pod(product_type,coffee_flavor,pack_size,product_code):
    coffee_pod = Coffee_pod()
    coffee_pod.product_type = product_type
    coffee_pod.pack_size = pack_size
    coffee_pod.coffee_flavor = coffee_flavor
    coffee_pod.product_code = product_code
    coffee_pod.save()


def pods_filter(product_type, coffee_flavor, pack_size):
    query = Q()
    if len(product_type)!=0:
        query = query & Q(product_type=product_type)
    if len(coffee_flavor)!=0:
        query = query & Q(coffee_flavor=coffee_flavor)
    if len(pack_size)!=0:
        query = query & Q(pack_size=int(pack_size))
    pods = Coffee_pod.objects().filter(query)
    return pods.to_json()


def machine_filter(product_type, water_line):
    query = Q()
    if len(product_type)!=0:
        query = query & Q(Product_type=product_type)
    if len(water_line)!=0:
        query = query & Q(Water_line=bool(water_line))
    machines = Coffee_machine.objects().filter(query)
    return machines.to_json()


