#============================================================
#
#
# Copyright (c) 2017 NetApp, Inc. All rights reserved.
# Specifications subject to change without notice.
#
# This sample code is provided AS IS, with no support or
# warranties of any kind, including but not limited to
# warranties of merchantability or fitness of any kind,
# expressed or implied.
#
# Min Python Version = python 2.7
#
#============================================================


#!/usr/bin/python

from ansible.module_utils.basic import *

import requests
import warnings
import sys
import json
import time
warnings.filterwarnings("ignore")


def get():
    url_path        = "/api/2.0/ontap/"

    flag=0

    url_path+="storage-pool-aggregate-relationships"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if storage_pool_key != None:
        if flag is 0:
            url_path+="?storage_pool_key="+storage_pool_key
            flag=1
        else:
            url_path+="&storage_pool_key="+storage_pool_key
    if aggregate_key != None:
        if flag is 0:
            url_path+="?aggregate_key="+aggregate_key
            flag=1
        else:
            url_path+="&aggregate_key="+aggregate_key
    if allocated_capacity != None:
        if flag is 0:
            url_path+="?allocated_capacity="+allocated_capacity
            flag=1
        else:
            url_path+="&allocated_capacity="+allocated_capacity
    if allocated_unit_count != None:
        if flag is 0:
            url_path+="?allocated_unit_count="+allocated_unit_count
            flag=1
        else:
            url_path+="&allocated_unit_count="+allocated_unit_count
    if raid_type != None:
        if flag is 0:
            url_path+="?raid_type="+raid_type
            flag=1
        else:
            url_path+="&raid_type="+raid_type
    if sortBy != None:
        if flag is 0:
            url_path+="?sortBy="+sortBy
            flag=1
        else:
            url_path+="&sortBy="+sortBy
    if maxRecords != None:
        if flag is 0:
            url_path+="?maxRecords="+maxRecords
            flag=1
        else:
            url_path+="&maxRecords="+maxRecords
    if nextTag != None:
        if flag is 0:
            url_path+="?nextTag="+nextTag
            flag=1
        else:
            url_path+="&nextTag="+nextTag
    response=http_request_for_get(url_path)
    json_response=response.json()
    return json_response

def post():
    url_path        = "/api/2.0/ontap/"
    url_path+="storage-pool-aggregate-relationships"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (storage_pool_key != None) & (storage_pool_key != key):
        payload['storage_pool_key']=storage_pool_key
    if (aggregate_key != None) & (aggregate_key != key):
        payload['aggregate_key']=aggregate_key
    if (allocated_capacity != None) & (allocated_capacity != key):
        payload['allocated_capacity']=allocated_capacity
    if (allocated_unit_count != None) & (allocated_unit_count != key):
        payload['allocated_unit_count']=allocated_unit_count
    if (raid_type != None) & (raid_type != key):
        payload['raid_type']=raid_type
    if (sortBy != None) & (sortBy != key):
        payload['sortBy']=sortBy
    if (maxRecords != None) & (maxRecords != key):
        payload['maxRecords']=maxRecords
    if (nextTag != None) & (nextTag != key):
        payload['nextTag']=nextTag

    response=http_request_for_post(url_path,**payload)
    json_response=response.headers
    return json_response

def put():
    url_path        = "/api/2.0/ontap/"
    url_path+="storage-pool-aggregate-relationships/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (storage_pool_key != None) & (storage_pool_key != key):
        payload['storage_pool_key']=storage_pool_key
    if (aggregate_key != None) & (aggregate_key != key):
        payload['aggregate_key']=aggregate_key
    if (allocated_capacity != None) & (allocated_capacity != key):
        payload['allocated_capacity']=allocated_capacity
    if (allocated_unit_count != None) & (allocated_unit_count != key):
        payload['allocated_unit_count']=allocated_unit_count
    if (raid_type != None) & (raid_type != key):
        payload['raid_type']=raid_type
    if (sortBy != None) & (sortBy != key):
        payload['sortBy']=sortBy
    if (maxRecords != None) & (maxRecords != key):
        payload['maxRecords']=maxRecords
    if (nextTag != None) & (nextTag != key):
        payload['nextTag']=nextTag
    if key != None:
        url_path+=key
        response=http_request_for_put(url_path,**payload)
        json_response=response.headers
        return json_response
    else:
        return "Provide the object key"

def delete():
    url_path        = "/api/2.0/ontap/"
    url_path+="storage-pool-aggregate-relationships/"

    if key != None:
        url_path+=key
        response=http_request_for_delete(url_path)
        json_response=response.headers
        return json_response
    else:
        return "Provide the object key for deletion"

def http_request_for_get(url_path,**payload):
	response = requests.get("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_put(url_path,**payload):
	response = requests.put("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_post(url_path,**payload):
	response = requests.post("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_delete(url_path,**payload):
	response = requests.delete("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response



def main():
        fields = {
                "action" : {
                        "required": True,
                        "choices": ['get', 'put', 'post', 'delete'],
                        "type": 'str'
                        },
                "host" : {"required": True, "type": "str"},
                "port" : {"required": True, "type": "str"},
                "user" : {"required": True, "type": "str"},
                "password" : {"required": True, "type": "str"},
                "key" : {"required": False, "type": "str"},
                "storage_pool_key" : {"required": False, "type": "str"},
                "aggregate_key" : {"required": False, "type": "str"},
                "allocated_capacity" : {"required": False, "type": "str"},
                "allocated_unit_count" : {"required": False, "type": "str"},
                "raid_type" : {"required": False, "type": "str"},
                "sortBy" : {"required": False, "type": "str"},
                "maxRecords" : {"required": False, "type": "str"},
                "nextTag" : {"required": False, "type": "str"},
                }

        module = AnsibleModule(argument_spec=fields)

        # NetApp Service Level Manager details
        global api_host
        global api_port
        global api_user_name
        global api_user_password

        global lun_key
        global nfs_share_key
        global cifs_share_key
        api_host                = module.params["host"]
        api_port                = module.params["port"]
        api_user_name           = module.params["user"]
        api_user_password       = module.params["password"]

        # Properties details
        global key
        key = module.params["key"]
        global storage_pool_key
        storage_pool_key = module.params["storage_pool_key"]
        global aggregate_key
        aggregate_key = module.params["aggregate_key"]
        global allocated_capacity
        allocated_capacity = module.params["allocated_capacity"]
        global allocated_unit_count
        allocated_unit_count = module.params["allocated_unit_count"]
        global raid_type
        raid_type = module.params["raid_type"]
        global sortBy
        sortBy = module.params["sortBy"]
        global maxRecords
        maxRecords = module.params["maxRecords"]
        global nextTag
        nextTag = module.params["nextTag"]

        global json_response

        # Actions
        if module.params["action"] == "get":
                result=get()
                module.exit_json(changed=False,meta=result)
        elif module.params["action"] == "put":
                result=put()
                module.exit_json(changed=True,meta=result['Location'].split("/jobs/")[1])
        elif module.params["action"] == "post":
                result=post()
                module.exit_json(changed=True,meta=result['Location'].split("/jobs/")[1])
        elif module.params["action"] == "delete":
                result=delete()
                module.exit_json(changed=True,meta=result['Location'].split("/jobs/")[1])


if __name__ == '__main__':
    main()