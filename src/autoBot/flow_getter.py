import os

def get_flows():


	# TODO modify as 
	'''
	for file in db:
		do stuff to get the current flow
		yield flow

	'''


	filepath = '../../data/static_file.txt'

	with open(filepath) as input_file:

		lines = input_file.readlines()

		lines = [line.replace('\n', '') for line in lines]

	flows = [lines]

	for flow in flows:
		yield flow # TODO add when DB is set up


def get_ids_in_flow(flow):
	return flow

