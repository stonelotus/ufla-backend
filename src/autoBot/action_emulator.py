# emulates actions from a certain flow


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import logging
import time

from driver_loader import get_driver_for_browser_ip
from flow_getter import get_all_flows
import helpers


def emulate_all_flows():
	for flow in get_all_flows():
		logging.info('Executing flow.')
		emulate_one_flow(flow)
		logging.info('================== End of flow ==================')


def emulate_one_flow(flow):
	driver = get_driver_for_browser_ip()
	chain = ActionChains(driver)

	for action in flow:
		action_type = helpers.get_action_type(action)
		logging.info(action_type)
	
		match action_type:
			# Mouse events
			case 'click':
				emulate_click(chain, driver, action)
			case 'dblclick':
				emulate_dblclick(chain, driver, action)
			case 'mousedown':
				emulate_mousedown(chain, driver, action)
			case 'mouseup':
				emulate_mouseup(chain, driver, action)
			case 'mousemove':
				emulate_mousemove(chain, driver, action)
			case 'mouseover':
				emulate_mouseover(chain, driver, action)
			case 'mouseenter':
				emulate_mouseover(chain, driver, action) # same function as mouseover
			# case 'mouseout':
			# 	emulate_mouseout(chain, driver, action)
			# case 'mouseleave':
			# 	emulate_mouseout(chain, driver, action) # same function as mouseout
			# # Commented as they add no value and increase error%
			case 'contextmenu':
				emulate_contextmenu(chain, driver, action)

			# Window events
			case 'scroll':
				emulate_scroll(chain, driver, action)
			case 'input':
				emulate_input(chain, driver, action)
			case 'DOMContentLoaded':
				# the purpose of this is to properly resize the window at the beginning of the session
				emulate_DOMContentLoaded(chain, driver, action)
			case 'resize':
				emulate_resize(chain, driver, action)

	time.sleep(5)

	driver.quit()

# MOUSE EVENTS
def emulate_click(chain, driver, action):
	try:
		element = helpers.get_element(driver, action)
		# time.sleep(1) # added timing needed to get to the middle of the object
		ctrl_key = helpers.get_ctrl_key(action)
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		chain.move_to_element(element).click().perform()
		
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		logging.info(f'Clicked element.')

	except Exception as e:
		logging.error(f'Exception when clicking.: ' + str(e))
		pass
	# else:
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_dblclick(chain, driver, action):
	try:
		element = helpers.get_element(driver, action)
		
		ctrl_key = helpers.get_ctrl_key(action)
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		chain.move_to_element(element).double_click().perform()
		
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		logging.info(f'Double-clicked element.')

	except Exception as e:
		logging.error(f'Exception when double-clicking: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_mousedown(chain, driver, action):
	try:
		element = helpers.get_element(driver, action)
		
		ctrl_key = helpers.get_ctrl_key(action)
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		chain.move_to_element(element).click_and_hold().perform()
		
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		logging.info(f'Mouse down on element.')

	except Exception as e:
		logging.error(f'Exception when performing mouse down: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_mouseup(chain, driver, action):
	try:
		element = helpers.get_element(driver, action)

		ctrl_key = helpers.get_ctrl_key(action)
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		chain.move_to_element(element).release().perform()
		
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		logging.info(f'Mouse up on element.')

	except Exception as e:
		logging.error(f'Exception when performing mouse up: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_mousemove(chain, driver, action):
	try:
		element = helpers.get_element(driver, action)

		ctrl_key = helpers.get_ctrl_key(action)
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		chain.move_to_element(element).perform()
		
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		logging.info(f'Moved mouse to element.')

	except Exception as e:
		logging.error(f'Exception when moving mouse: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


# Both mouseover and mouseenter can be handled with the same function
def emulate_mouseover(chain, driver, action):
	try:
		element = helpers.get_element(driver, action)
		
		ctrl_key = helpers.get_ctrl_key(action)
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		chain.move_to_element(element).perform()
		
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		logging.info(f'Mouse over/enter element.')

	except Exception as e:
		logging.error(f'Exception when performing mouse over/enter: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


# Both mouseout and mouseleave can be handled with the same function
def emulate_mouseout(chain, driver, action):
	try:
		element = helpers.get_element(driver, action)
		
		ctrl_key = helpers.get_ctrl_key(action)
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		chain.move_to_element_with_offset(element, -10, -10).perform()
		
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		logging.info(f'Mouse out/leave element.')

	except Exception as e:
		logging.error(f'Exception when performing mouse out/leave: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_contextmenu(chain, driver, action):
	try:
		element = helpers.get_element(driver, action)
		
		ctrl_key = helpers.get_ctrl_key(action)
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		chain.move_to_element(element).context_click().perform()
		
		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		logging.info(f'Right-clicked element.')

	except Exception as e:
		logging.error(f'Exception when right-clicking: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


# WINDOW EVENTS
def emulate_scroll(chain, driver, action):
	# TODO add scroll_width
	try:
		scrollX, scrollY = helpers.get_scroll_params(action)

		scroll_script = f'window.scrollTo({scrollX}, {scrollY});'
		driver.execute_script(scroll_script)

		logging.info(f'Executed scroll.')

	except Exception as e:
		logging.error(f'Exception when scrolling.' + str(e))
		pass
	# else:
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_DOMContentLoaded(chain, driver, action):
	try:
		outer_width, outer_height = helpers.get_window_size(action)
		if outer_width is not None and outer_height is not None:
			driver.set_window_size(outer_width, outer_height)
			logging.info(f'Properly sized window for DOMContentLoaded.')
		else:
			logging.info(f'Received "None" sizes when sizing window for DOMContentLoaded.')

	except Exception as e:
		logging.error(f'Exception when sizing window for DOMContentLoaded.:\n {e}')
		pass
	# else:
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_resize(chain, driver, action):
	try:
		outer_width, outer_height = helpers.get_window_size(action)

		if outer_width is not None and outer_height is not None:
			driver.set_window_size(outer_width, outer_height)
			logging.info(f'Properly sized window for resize.')
		else:
			logging.info(f'Received "None" sizes when sizing window for resize.')

	except Exception as e:
		logging.error(f'Exception when sizing window for resize.')
		pass
	# else:
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_input(chain, driver, action):
	input_element = helpers.get_element(driver, action)
	keys_to_input = helpers.get_keys_to_input(action)

	input_type = action['inputType']
	match input_type:
		case 'insertText':
			_handle_insert_text_event(chain, input_element, keys_to_input)
		case 'deleteContentBackward':
			_handle_delete_content_backward_event(input_element)
		case 'deleteContentForward':
			_handle_delete_content_forward_event(input_element)
		case 'insertFromPaste':
			_handle_insert_from_paste_event(chain, input_element)
		case 'insertFromDrop':
			_handle_insert_from_drop_event(chain, input_element, keys_to_input)
		case 'insertCompositionText':
			_handle_insert_composition_text_event(input_element, keys_to_input)
		case 'insertLineBreak':
			_handle_insert_line_break_event(input_element)
		case _:
			raise ValueError(f'Unknown inputType value: {input_type}')

	logging.info('--------------- End of action -----------------')


def _handle_insert_text_event(chain, input_element, keys_to_input):
	chain.move_to_element(input_element).click().send_keys(keys_to_input).perform()
	logging.info('Inserted text.')


def _handle_delete_content_backward_event(input_element):
	input_element.send_keys(Keys.BACKSPACE)
	logging.info('Deleted content backward.')


def _handle_delete_content_forward_event(input_element):
	input_element.send_keys(Keys.DELETE)
	logging.info('Deleted content forward.')


def _handle_insert_from_paste_event(chain, input_element):
	chain.move_to_element(input_element).click().key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
	logging.info('Inserted content from paste.')


def _handle_insert_from_drop_event(chain, input_element, keys_to_input):
	chain.drag_and_drop(keys_to_input, input_element).perform()
	logging.info('Inserted content from drop.')


def _handle_insert_composition_text_event(input_element, keys_to_input):
	input_element.send_keys(keys_to_input)
	logging.info('Inserted composition text.')


def _handle_insert_line_break_event(input_element):
	input_element.send_keys(Keys.ENTER)
	logging.info('Inserted line break.')

