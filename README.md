# VrfDetailExtractor7750
VrfDetailExtractor7750 is a python-based utility to extract VRF details from a Nokia SR 7750 router configuration file and dump them into a CSV file.
It extracts the following details:
- Physical port belonging to the VRF
- Vlan of the interface
- VRF name
- Interface description
- IP address of the interface
- VRF ID
- Ingress and Egress QoS policy applied on the VRF interface

## Requirements
Linux machine with python 2.7 installed

## How to use
Create a file and copy the VRF definition section from the Nokia SR 7750 router configuration to this file

```
$ touch VrfConfig
$
$ cat VrfConfig
        vprn 1001 name "mob_iub" customer 1001 create
            description "mob_iub"
            vrf-import "mob_iub_Import"
            vrf-export "mob_iub_Export"
            autonomous-system 100
            route-distinguisher 2.2.2.2:1
            auto-bind-tunnel
                resolution-filter
                    ldp
                exit
                resolution filter
            exit
            enable-bgp-vpn-backup ipv4 ipv6
            interface "GE-1/1/1:401" create
                description "For_site_1_IuB"
                address 192.168.123.1/30
                sap 1/1/1:401 create
                    description "For_site_1_IuB"
                    ingress
                        qos 15
                    exit
                    egress
                        qos 15
                    exit
                    dist-cpu-protection "dist-cpu-arp"
                exit
            exit
            interface "GE-1/1/4:402" create
                description "For_site_2_IuB"
                address 192.168.125.1/30
                sap 1/1/4:402 create
                    description "For_site_2_IuB"
                    ingress
                        qos 15
                    exit
                    egress
                        qos 15
                    exit
                    dist-cpu-protection "dist-cpu-arp"
                exit
            exit

        vprn 2001 name "mob_mub" customer 2001 create
            description "mob_mub"
            vrf-import "mob_mub_Import"
            vrf-export "mob_mub_Export"
            autonomous-system 100
            route-distinguisher 2.2.2.2:2
            auto-bind-tunnel
                resolution-filter
                    ldp
                exit
                resolution filter
            exit
            enable-bgp-vpn-backup ipv4 ipv6
            interface "GE-1/1/1:501" create
                description "For_site_1_MuB"
                address 192.168.124.1/30
                sap 1/1/1:501 create
                    description "For_site_1_MuB"
                    ingress
                        qos 15
                    exit
                    egress
                        qos 15
                    exit
                    dist-cpu-protection "dist-cpu-arp"
                exit
            exit
            interface "GE-1/1/4:502" create
                description "For_site_2_MuB"
                address 192.168.126.1/30
                sap 1/1/4:502 create
                    description "For_site_2_MuB"
                    ingress
                        qos 15
                    exit
                    egress
                        qos 15
                    exit
                    dist-cpu-protection "dist-cpu-arp"
                exit
            exit

```

Give execute permissions to your script
```
$ chmod 755 VrfDetailExtractor7750.py
```

Run the script
```
$ ./VrfDetailExtractor7750.py 

Enter absolute path of file: VrfConfig

$ 
```

The script generates a file named "service_mapping_sheet.csv". Display the file contents using cat command
```
$ ls
service_mapping_sheet.csv	VrfConfig                VrfDetailExtractor7750.py
$ 
$ cat service_mapping_sheet.csv 
port,vlan,description,IP_address,vprn_id,vrf,ingress_qos_id,egress_qos_id
null,null,null,null,null,null,null,null
GE-1/1/1,401,For_site_1_IuB,192.168.123.1/30,1001,mob_iub,15,15
GE-1/1/4,402,For_site_2_IuB,192.168.125.1/30,1001,mob_iub,15,15
GE-1/1/1,501,For_site_1_MuB,192.168.124.1/30,2001,mob_mub,15,15
GE-1/1/4,502,For_site_2_MuB,192.168.126.1/30,2001,mob_mub,15,15
$
```
