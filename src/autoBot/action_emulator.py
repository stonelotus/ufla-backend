# emulates actions from a certain flow


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver_loader import get_driver_for_browser_ip
from flow_getter import get_all_flows


def emulate_all_flows():
	for flow in get_all_flows():
		print(f'Executing flow : "{flow}"')
		emulate_one_flow(flow)
		print('====================================')


def emulate_one_flow(flow):
	driver = get_driver_for_browser_ip()
	for action in flow:
		action_type = _get_action_type(action)
	
	match action_type:
		case 'click':
			_emulate_click(action)
		case 'scroll':
			_emulate_scroll(action)
		case 'input':
			_emulate_scroll(input)

	driver.quit()


def _get_action_type(action: dict):
	# it is imposed that any action object within a flow has a type
	try:
		return action['type']
	except KeyError:
		print('Current action has no "type" property')
		return None


def _click_by_ids(driver, ids):
	# deprecated
	# to be removed

	for id in ids:
		try:
			button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.CLASS_NAME, id))
			)

			button.click()
			print(f'Clicked button with id : {id}')

		except Exception as e:
			print(f'Exception for id {id}')
			pass
		# else:
		finally:
			print('--------------------------------')






