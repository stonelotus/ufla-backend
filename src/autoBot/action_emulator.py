# emulates actions from a certain flow


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
			case 'mouseout':
				emulate_mouseout(chain, driver, action)
			case 'mouseleave':
				emulate_mouseout(chain, driver, action) # same function as mouseout
			# Commented as they add no value and increase error%
			case 'contextmenu':
				emulate_contextmenu(chain, driver, action)

			# Window events
			case 'scroll':
				emulate_scroll(chain, driver, action)
			case 'resize':
				emulate_resize(chain, driver, action)

			case 'DOMContentLoaded':
				# the purpose of this is to properly resize the window at the beginning of the session
				emulate_DOMContentLoaded(chain, driver, action)

			# keyboard events
			# case 'keydown':
			# 	emulate_keydown(chain, driver, action)
			# case 'keyup':
			# 	emulate_keyup(chain, driver, action)
			# case 'keypress':
			# 	emulate_keypress(chain, driver, action)
			
			# form events
			# case 'submit':
			# 	emulate_submit(chain, driver, action)
			case 'input':
				emulate_input(chain, driver, action)
			# case 'blur':
			# 	emulate_blur(chain, driver, action)
			# case 'focus':
			# 	emulate_focus(chain, driver, action)
			# case 'reset':
			# 	emulate_reset(chain, driver, action)
			# case 'change':
			# 	emulate_change(chain, driver, action)
			case 'select':
				emulate_select(chain, driver, action)

	time.sleep(5)

	driver.quit()

# MOUSE EVENTS
def emulate_click(chain, driver, action):
	try:
		element = helpers.get_element(driver, action)
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

	time.sleep(0.1) # make sure there is enough time for scroll

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


# Keyboard events
def emulate_keydown(chain, driver, action):
	try:
		key = helpers.get_key(action)
		ctrl_key = helpers.get_ctrl_key(action)

		if key is None:
			logging.error("Key must be specified for keydown event.")
			return

		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		chain.key_down(key).perform()

		if ctrl_key:
			chain.key_up(Keys.CONTROL)

		logging.info(f'Performed keydown on {key} with ctrlKey={ctrl_key}.')

	except Exception as e:
		logging.error(f'Exception when performing keydown with ctrlKey={ctrl_key}: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_keyup(chain, driver, action):
	try:
		key = helpers.get_key(action)
		ctrl_key = helpers.get_ctrl_key(action)
		if key is None:
			logging.error("Key must be specified for keyup event.")
			return

		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		chain.key_up(key).perform()

		if ctrl_key:
			chain.key_up(Keys.CONTROL)

		logging.info(f'Performed keyup on {key} with ctrlKey={ctrl_key}.')

	except Exception as e:
		logging.error(f'Exception when performing keyup with ctrlKey={ctrl_key}: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_keypress(chain, driver, action):
	try:
		key = helpers.get_key(action)
		ctrl_key = helpers.get_ctrl_key(action)
		if key is None:
			logging.error("Key must be specified for keypress event.")
			return

		if ctrl_key:
			chain.key_down(Keys.CONTROL)

		chain.send_keys(key).perform()

		if ctrl_key:
			chain.key_up(Keys.CONTROL)

		logging.info(f'Performed keypress on {key} with ctrlKey={ctrl_key}.')

	except Exception as e:
		logging.error(f'Exception when performing keypress with ctrlKey={ctrl_key}: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


# Form events
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


def emulate_blur(chain, driver, action):
	try:
		element = helpers.get_element(driver, action)
		if element is None:
			logging.error("Element must be specified for blur event.")
			return

		body = driver.find_element_by_tag_name('body')
		chain.move_to_element(element).click().move_to_element(body).click().perform()
		logging.info(f'Blurred the element.')

	except Exception as e:
		logging.error(f'Exception when blurring the element: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_focus(chain, driver, action):
	try:
		element = helpers.get_element(driver, action)
		if element is None:
			logging.error("Element must be specified for focus event.")
			return

		chain.move_to_element(element).click().perform()
		logging.info(f'Focused the element.')

	except Exception as e:
		logging.error(f'Exception when focusing the element: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_submit(driver, action):
	try:
		element = helpers.get_element(driver, action)
		if element is None:
			logging.error("Element must be specified for submit event.")
			return

		element.submit()
		logging.info(f'Submitted the form.')

	except Exception as e:
		logging.error(f'Exception when submitting the form: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_reset(driver, action):
	try:
		# TODO make sure this gets the right element in this context
		form_element = helpers.get_element(driver, action)
		if form_element is None:
			logging.error("Form element must be specified for reset event.")
			return

		reset_script = 'arguments[0].reset();'
		driver.execute_script(reset_script, form_element)
		logging.info(f'Reset the form.')

	except Exception as e:
		logging.error(f'Exception when resetting the form: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_change(chain, driver, action):
	try:
		element = helpers.get_element(driver, action)
		value = helpers.get_value(action)
		if element is None:
			logging.error("Element and value must be specified for change event.")
			return

		# Check if the element is a checkbox or radio button
		is_checkbox = element.tag_name == 'input' and element.get_attribute('type') == 'checkbox'
		is_radio = element.tag_name == 'input' and element.get_attribute('type') == 'radio'

		if is_checkbox or is_radio:
			# Simulate a space key press to toggle the checkbox or radio button
			chain.move_to_element(element).click().key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
		else:
			# Move to the element, click it, and send the new value
			chain.move_to_element(element).click().send_keys(value).perform()

		# Trigger the 'change' event on the element using ActionChains
		chain.move_to_element(element).click().perform()

		logging.info(f'Changed the value of the element.')

	except Exception as e:
		logging.error(f'Exception when changing the value of the element: ' + str(e))
		pass
	finally:
		logging.info('--------------- End of action -----------------')


def emulate_select(chain, driver, action):
	try:
		element = helpers.get_element(driver, action)
		start, end = helpers.get_start_end(action)

		print(start, end)

		if element is None:
			logging.error("Element must be specified for select event.")
			return

		if end is None or end == '':
			# If end is not specified, select from start to end of text
			end = len(helpers.get_value(action))

		# Move to the element and click to focus it
		chain.move_to_element(element).click().perform()

		# Select the text in the element using ActionChains
		actions = ActionChains(driver)
		actions.move_to_element(element).click_and_hold().move_by_offset(start, 0).move_by_offset(end - start, 0).release().perform()

		logging.info(f'Selected text in the element.')

	except Exception as e:
		logging.error(f'Exception when selecting text in the element: ' + str(e))
		pass
	finally:
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

