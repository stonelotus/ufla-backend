# Prepares a mock driver to execute actions on the website


from selenium.webdriver import Chrome, ChromeOptions

_DEFAULT_BROWSER = 'Chrome'
_DEFAULT_IP = 'http://127.0.0.1:8080'


def get_driver_for_browser_ip(browserName=_DEFAULT_BROWSER, ip=_DEFAULT_IP):

	driver = _get_driver(browserName)
	# driver.set_window_size(1042, 1494)
	driver.maximize_window()

	driver.get(ip)

	print('Bot has enetered chat.')

	return driver


def _get_driver(browserName=_DEFAULT_BROWSER):

	match browserName:
		case 'Chrome':

			# Create options for Chrome
			chrome_options = ChromeOptions()

			# Disable notifications
			prefs = {"profile.default_content_setting_values.notifications": 2}
			chrome_options.add_experimental_option("prefs", prefs)
			# chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

			# Launch the Chrome browser
			driver = Chrome(options=chrome_options)

		case _:
			print('Wrong browser name.')
			return None

	return driver
