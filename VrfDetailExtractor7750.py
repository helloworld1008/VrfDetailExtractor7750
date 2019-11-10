#!/usr/bin/env python

import re

input_file = raw_input("Enter absolute path of file: ")

####################

vprn_object = re.compile(r"^\s*?vprn (\d+)( name \"(.*?)\")? customer.*$")
interface_object = re.compile(r"^\s*?interface \"(.*?):(\d+)\" create$")
description_object = re.compile(r"^\s*?description \"(.*?)\"$")
address_object = re.compile(r"^\s*?address (.*?)$")
ingress_object = re.compile(r"^\s*?ingress$")
egress_object = re.compile(r"^\s*?egress$")
qos_object = re.compile(r"^\s*?qos (\d+)$")

####################

vrf_name = "null"
vrf_id = "null"
interface_name = "null"
port = "null"
vlan = "null"
interface_description = "null"
interface_address = "null"
ingress_qos_id = "null"
egress_qos_id = "null"

####################

interface_creation_flag = 0
description_flag = 0
ingress_qos_flag = 0
egress_qos_flag = 0

####################

fo = open('service_mapping_sheet.csv', 'w')
fo.write("port,vlan,description,IP_address,vprn_id,vrf,ingress_qos_id,egress_qos_id\n")
fi = open(input_file, 'r')

line = fi.readline()

####################

while line:

	vprn_result = vprn_object.match(line)
	interface_result = interface_object.match(line)
	description_result = description_object.match(line)
	address_result = address_object.match(line)
	ingress_result = ingress_object.match(line)
	egress_result = egress_object.match(line)
	qos_result = qos_object.match(line)


	if vprn_result is not None:

		new_vrf_name = vprn_result.group(3)
		new_vrf_id = vprn_result.group(1)

		interface_creation_flag = 0


	if interface_result is not None:

		fo.write("{0},{1},{2},{3},{4},{5},{6},{7}\n".format(port,vlan,interface_description,interface_address,vrf_id,vrf_name,ingress_qos_id,egress_qos_id))

		interface_creation_flag = 1
		description_flag = 0

		port = interface_result.group(1)
		vlan = interface_result.group(2)
		vrf_name = new_vrf_name
		vrf_id = new_vrf_id

		interface_description = "null"
		interface_address = "null"
		ingress_qos_id = "null"
		egress_qos_id = "null"


	if description_result is not None and interface_creation_flag == 1 and description_flag == 0:

		interface_description = description_result.group(1)
		description_flag = 1


	if address_result is not None:

		interface_address = address_result.group(1)


	if ingress_result is not None:

		ingress_qos_flag = 1

	if egress_result is not None:

		egress_qos_flag = 1

	if qos_result is not None and ingress_qos_flag == 1:

		ingress_qos_id = qos_result.group(1)
		ingress_qos_flag = 0

	if qos_result is not None and egress_qos_flag == 1:

		egress_qos_id = qos_result.group(1)
		egress_qos_flag = 0


	line = fi.readline()

	if line == '':

		fo.write("{0},{1},{2},{3},{4},{5},{6},{7}\n".format(port,vlan,interface_description,interface_address,vrf_id,vrf_name,ingress_qos_id,egress_qos_id))		

####################

fo.close()
fi.close()

#################### 
