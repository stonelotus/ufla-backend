# emulates actions from a certain flow


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver_loader import get_driver_for_browser_ip
from flow_getter import get_all_flows


def emulate_all_flows():
	for flow in get_all_flows():
		# print(f'Executing flow : "{flow}"')
		print('Executing flow.')
		emulate_one_flow(flow)
		print('====================================')


def emulate_one_flow(flow):
	driver = get_driver_for_browser_ip()
	for action in flow:
		action_type = _get_action_type(action)
		print(action_type)
	
		match action_type:
			case 'click':
				_emulate_click(driver, action)
			case 'scroll':
				_emulate_scroll(driver, action)
			case 'input':
				_emulate_input(driver, action)
			case 'DOMContentLoaded':
				# the purpose of this is to properly resize the window at the beginning of the session
				_emulate_DOMContentLoaded(driver, action)
			case 'resize':
				_emulate_resize(driver, action)

	driver.quit()


def _emulate_click(driver, action):
	try:
		element = WebDriverWait(driver, 10).until(
			_get_element_identifier_for_click(action)
		)

		element.click()
		print(f'Clicked element.')

	except Exception as e:
		print(f'Exception when clicking.')
		pass
	# else:
	finally:
		print('--------------------------------')


def _emulate_scroll(driver, action):
	try:
		scroll_height = _get_scroll_height(action)

		script = "window.scrollTo(0, " + str(scroll_height) + ");"

		driver.execute_script(script)

		print(f'Executed scroll.')

	except Exception as e:
		print(f'Exception when scrolling.')
		pass
	# else:
	finally:
		print('--------------------------------')


def _emulate_input(driver, action):
	# TODO add behaviour for special cases e.g. "inputType": "deleteContentBackward",
	try:
		input_element = WebDriverWait(driver, 10).until(
			_get_element_identifier_for_input(action)
		)

		keys_to_input = _get_keys_to_input(action)

		input_element.send_keys(keys_to_input)
		print(f'Sent input.')

	except Exception as e:
		print(f'Exception when inputting.')
		pass
	# else:
	finally:
		print('--------------------------------')


def _emulate_DOMContentLoaded(driver, action):
	try:
		inner_height, inner_width = _get_window_size_for_DOMContentLoaded(action)

		if inner_width is not None and inner_height is not None:
			driver.set_window_size(inner_height, inner_width)
			print(f'Properly sized window for DOMContentLoaded.')
		else:
			print(f'Received "None" sizes when sizing window for DOMContentLoaded.')

	except Exception as e:
		print(f'Exception when sizing window for DOMContentLoaded.')
		pass
	# else:
	finally:
		print('--------------------------------')


def _emulate_resize(driver, action):
	try:
		inner_height, inner_width = _get_window_size_for_resize(action)

		if inner_width is not None and inner_height is not None:
			driver.set_window_size(inner_height, inner_width)
			print(f'Properly sized window for resize.')
		else:
			print(f'Received "None" sizes when sizing window for resize.')

	except Exception as e:
		print(f'Exception when sizing window for resize.')
		pass
	# else:
	finally:
		print('--------------------------------')


def _get_element_identifier_for_click(action):
	# this returns an EC.function corresponding to the looked for element

	element_id = _get_action_id(action)
	if element_id is not None:
		return EC.presence_of_element_located((By.ID, element_id))

	css_selector = _get_action_css_selector(action)
	if css_selector is not None:
		return EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))

	print('Error fetching object. Object has no id or css_selector')
	return None


def _get_element_identifier_for_input(action):
	# this returns an EC.function corresponding to the looked for element
	# identical to the one for click. Are separated since they might need particular modifications later on

	element_id = _get_action_id(action)
	if element_id is not None:
		return EC.presence_of_element_located((By.ID, element_id))

	css_selector = _get_action_css_selector(action)
	if css_selector is not None:
		return EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))

	print('Error fetching object. Object has no id or css_selector')
	return None


def _get_window_size_for_DOMContentLoaded(action):
	try:
		action_target = action['target']
	except KeyError as ke:
		print('Error getting window size : action has no "target" field.')
	else:
		try:
			action_target_default_view =  action_target['defaultView']
		except KeyError as ke:
			print('Error getting window size for DOMContentLoaded : action target has no "defaultView" field.')
		else:
			try:
				inner_height = action_target_default_view['innerHeight']
				inner_width = action_target_default_view['innerWidth']
			except KeyError as ke:
				print('Error getting window size for DOMContentLoaded : action target default view has no "innerHeight" or "innerWidth" field.')

	return inner_height, inner_width


def _get_window_size_for_resize(action):
	try:
		action_target = action['target']
	except KeyError as ke:
		print('Error getting window size for resize : action has no "target" field.')
	else:
		try:
			inner_height = action_target['innerHeight']
			inner_width = action_target['innerWidth']
		except KeyError as ke:
			print('Error getting window size for resize : action target has no "innerHeight" or "innerWidth" field.')

	return inner_height, inner_width


def _get_keys_to_input(action):
	try:
		action_data = action["data"]
	except KeyError as ke:
		print('Error getting keys to input : action has no "data" field.')

	return action_data


def _get_action_id(action):
	try:
		action_target = action['target']
	except KeyError as ke:
		print('Error getting action ID : action has no "target" field.')
	else:
		try:
			action_id =  action_target["id"]
		except KeyError as ke:
			print('Error getting action ID : action target has no "id" field.')

	if action_id is None or action_id is "":
		return None

	return action_id


def _get_action_css_selector(action):
	try:
		action_target = action['target']
	except KeyError as ke:
		print('Error getting action css_selector : action has no "target" field.')
	else:
		try:
			action_class_name =  action_target["className"]
		except KeyError as ke:
			print('Error getting action css_selector : action target has no "className" field.')

	if action_class_name is None or action_class_name is "":
		return None

	return action_class_name


def _get_scroll_height(action):
	try:
		action_target = action['target']
	except KeyError as ke:
		print('Error getting action scroll height : action has no "target" field.')
	else:
		try:
			action_scrolling_element =  action_target["scrollingElement"]
		except KeyError as ke:
			print('Error getting action scroll height : action target has no "scrollingElement" field.')
		else:
			try:
				action_scroll_height = action_scrolling_element["scrollHeight"]
			except KeyError as ke:
				print('Error getting action scroll height: action target scrollingElement has no "scrollHeight" field.')

	# if action_scroll_height is None:
	# 	return None

 	## if 0 then ok to return 0 to execute an empty scroll
	return action_scroll_height


def _get_action_type(action: dict):
	# it is imposed that any action object within a flow has a type
	try:
		return action['type']
	except KeyError:
		print('Current action has no "type" property')
		return None

