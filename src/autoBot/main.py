# main point of entry for the autoBot

from emulator_logging import logging_init
from action_emulator import emulate_all_flows


if __name__ == "__main__":
	logging_init()
	emulate_all_flows()
	
