#!/usr/bin/env python3

#Simple program showcasing namesilo.
#Program reads the apikey and domain from files 
#named apikey and domain repectively and the prints
#the return of the list_dns_records as dictionary
#objects 

import pprint
import namesilo

with open('apikey', 'r') as f:
    apikey = f.read().strip('\r\n')

with open('domain', 'r') as f:
    domain = f.read().strip('\r\n')

#ns = namesilo.NameSilo(apikey, live=True, legacy=True) #Utilizing legacy naming convention
ns = namesilo.NameSilo(apikey, live=True)

#reply = ns.list_dns_records(domain=domain) #Legacy naming convention
reply = ns.dnsListRecords(domain=domain)

dnsRecords = []

for rec in reply.resource_record:
    d = {}
    keys = dir(rec)
    for key in keys:
        d[key] = eval('rec.%s.cdata'%key)
    dnsRecords.append(d)

pprint.pprint(dnsRecords)
