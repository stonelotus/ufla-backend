# Loads flow from database and properly formats data


import os
import json


def get_all_flows():
	# Gets all the flows from the database

	# TODO modify as 
	'''
	for file in db:
		do stuff to get the current flow
		yield flow

	'''


	filepath = '../../data/static_file.json'

	with open(filepath) as input_file:

		data = input_file.read()

		jsonData = '[' + data[:-1] + ']'
		# add first and last [ ] while removing the last ',' character

		flow = json.loads(jsonData)

	flows = [flow]

	for flow in flows:
		yield flow # TODO add when DB is set up

