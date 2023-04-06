# emulates actions from a certain flow


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import logging
import time

from driver_loader import get_driver_for_browser_ip
from flow_getter import get_all_flows


def emulate_all_flows():
	for flow in get_all_flows():
		logging.info('Executing flow.')
		emulate_one_flow(flow)
		logging.info('================== End of flow ==================')


def emulate_one_flow(flow):
	driver = get_driver_for_browser_ip()
	chain = ActionChains(driver)

	for action in flow:
		action_type = _get_action_type(action)
		logging.info(action_type)
	
		match action_type:
			case 'click':
				_emulate_click(chain, driver, action)
			# case 'scroll':
			# 	_emulate_scroll(chain, driver, action)
			case 'input':
				_emulate_input(chain, driver, action)
			# case 'DOMContentLoaded':
			# 	pass
			# 	print('reaches here')
			# 	# the purpose of this is to properly resize the window at the beginning of the session
			# 	_emulate_DOMContentLoaded(driver, action)
			# case 'resize':
			# 	pass
			# 	_emulate_resize(driver, action)

	driver.quit()


def _emulate_click(chain, driver, action):
	try:
		element = _get_element(driver, action)
		chain.move_to_element(element).click().perform()
		logging.info(f'Clicked element.')

	except Exception as e:
		logging.error(f'Exception when clicking.: ' + str(e))
		pass
	# else:
	finally:
		logging.info('--------------- End of action -----------------')


def _emulate_scroll(chain, driver, action):
	# TODO add scroll_width
	try:
		scroll_height = _get_scroll_height(action)

		driver.execute_script('window.scrollTo(0, arguments[0]);', scroll_height)
		logging.info(f'Executed scroll.')

	except Exception as e:
		logging.error(f'Exception when scrolling.' + str(e))
		pass
	# else:
	finally:
		logging.info('--------------- End of action -----------------')


def _emulate_input(chain, driver, action):
	# TODO add behaviour for special cases e.g. "inputType": "deleteContentBackward",
	try:
		input_element = _get_element(driver, action)
		keys_to_input = _get_keys_to_input(action)
		
		chain.move_to_element(input_element).click().send_keys(keys_to_input).perform()
		logging.info(f'Sent input.')

	except Exception as e:
		logging.error(f'Exception when inputting.' + str(e))
		pass
	# else:
	finally:
		logging.info('--------------- End of action -----------------')



def _emulate_DOMContentLoaded(chain, action):
	try:
		inner_height, inner_width = _get_window_size_for_DOMContentLoaded(action)

		if inner_width is not None and inner_height is not None:
			driver.set_window_size(inner_height, inner_width)
			logging.info(f'Properly sized window for DOMContentLoaded.')
		else:
			logging.info(f'Received "None" sizes when sizing window for DOMContentLoaded.')

	except Exception as e:
		logging.error(f'Exception when sizing window for DOMContentLoaded.')
		pass
	# else:
	finally:
		logging.info('--------------------------------')


def _emulate_resize(chain, action):
	try:
		inner_height, inner_width = _get_window_size_for_resize(action)

		if inner_width is not None and inner_height is not None:
			driver.set_window_size(inner_height, inner_width)
			logging.info(f'Properly sized window for resize.')
		else:
			logging.info(f'Received "None" sizes when sizing window for resize.')

	except Exception as e:
		logging.error(f'Exception when sizing window for resize.')
		pass
	# else:
	finally:
		logging.info('--------------------------------')


def _get_element(driver, action):
	try:
		element_xpath = _get_element_xpath(action)

		element = WebDriverWait(driver, 2).until(
			EC.presence_of_element_located((By.XPATH, element_xpath))
		)

		driver.execute_script("arguments[0].scrollIntoView(true);", element)

		element = WebDriverWait(driver, 10).until(
			EC.visibility_of_element_located((By.XPATH, element_xpath))
		)

		time.sleep(1)
		# should do the same as the above, however the above doesn't perform properly for some reason
		return element

	except:
		logging.error(f'Exception when getting element')


def _get_window_size_for_DOMContentLoaded(action):
	try:
		action_target = action['target']
	except Keyerror as ke:
		logging.error('error getting window size : action has no "target" field.')
	else:
		try:
			action_target_default_view =  action_target['defaultView']
		except Keyerror as ke:
			logging.error('error getting window size for DOMContentLoaded : action target has no "defaultView" field.')
		else:
			try:
				inner_height = action_target_default_view['innerHeight']
				inner_width = action_target_default_view['innerWidth']
			except Keyerror as ke:
				logging.error('error getting window size for DOMContentLoaded : action target default view has no "innerHeight" or "innerWidth" field.')

	return inner_height, inner_width


def _get_window_size_for_resize(action):
	try:
		action_target = action['target']
	except Keyerror as ke:
		logging.error('error getting window size for resize : action has no "target" field.')
	else:
		try:
			inner_height = action_target['innerHeight']
			inner_width = action_target['innerWidth']
		except Keyerror as ke:
			logging.error('error getting window size for resize : action target has no "innerHeight" or "innerWidth" field.')

	return inner_height, inner_width


def _get_element_xpath(element):
	try:
		return element['xpath']
	except:
		logging.error('error getting element xpath : element has no "xpath" field.')
	return None


def _get_keys_to_input(action):
	try:
		action_data = action["data"]
	except Keyerror as ke:
		logging.error('error getting keys to input : action has no "data" field.')

	return action_data


def _get_action_id(action):
	try:
		action_target = action['target']
	except Keyerror as ke:
		logging.error('error getting action ID : action has no "target" field.')
	else:
		try:
			action_id =  action_target["id"]
		except Keyerror as ke:
			logging.error('error getting action ID : action target has no "id" field.')

	if action_id == None or action_id == "":
		return None

	return action_id


def _get_action_css_selector(action):
	try:
		action_target = action['target']
	except Keyerror as ke:
		logging.error('error getting action css_selector : action has no "target" field.')
	else:
		try:
			action_class_name =  action_target["className"]
		except Keyerror as ke:
			logging.error('error getting action css_selector : action target has no "className" field.')

	if action_class_name == None or action_class_name == "":
		return None

	return action_class_name


def _get_scroll_height(action):
	# try:
	# 	return action['scrollY']
	# except Exception as e:
	# 	print('Exception getting the scrollY property'.)
	# 	return None

	try:
		action_target = action['target']
	except Keyerror as ke:
		logging.error('error getting action scroll height : action has no "target" field.')
	else:
		try:
			action_scrolling_element =  action_target["scrollingElement"]
		except Keyerror as ke:
			logging.error('error getting action scroll height : action target has no "scrollingElement" field.')
		else:
			try:
				action_scroll_height = action_scrolling_element["scrollHeight"]
			except Keyerror as ke:
				logging.error('error getting action scroll height: action target scrollingElement has no "scrollHeight" field.')

 	## if 0 then ok to return 0 to execute an empty scroll
	return action_scroll_height


def _get_action_type(action: dict):
	# it is imposed that any action object within a flow has a type
	try:
		return action['type']
	except Keyerror:
		logging.error('Current action has no "type" property')
		return None

