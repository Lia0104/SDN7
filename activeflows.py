import requests
from requests.auth import HTTPBasicAuth
import json


def http_get(url):
	url= url
	headers = {}
	params = {}
	resp = requests.get(url,auth=HTTPBasicAuth('admin', 'admin'))
	return resp


if __name__ == "__main__":
	url = "http://127.0.0.1:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0"
	resp = http_get(url)
	#print resp.content
	jsonobj = json.loads(resp.content)
	print jsonobj
	print ""
	print "active-flows = "+ str(jsonobj["flow-node-inventory:table"][0]["opendaylight-flow-table-statistics:flow-table-statistics"]["active-flows"])



