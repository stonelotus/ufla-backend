
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver_loader import get_driver_for_browser_ip
from flow_getter import get_flows, get_ids_in_flow


def click_by_ids(driver, ids):

	for id in ids:
		try:
			button = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.CLASS_NAME, id))
			)

			button.click()
			print(f'Clicked button with id : {id}')

		except Exception as e:
			# print(f'Exception for id {id} :  {e}')
			print(f'Exception for id {id}')
			# button.click()
			# print(f'Clicked button with id : {id}')
			pass
		# else:
		finally:
			print('--------------------------------')



if __name__ == "__main__":

	driver = get_driver_for_browser_ip()

	for flow in get_flows():
		print(f'Executing flow : "{flow}"')
		ids = get_ids_in_flow(flow)
		click_by_ids(driver, ids)
		print('====================================')

	driver.quit()

