from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import logging
import time


def get_element(driver, action):
    try:
        element_xpath = _get_element_xpath(action)

        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, element_xpath))
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", element)

        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, element_xpath))
        )

        # should do the same as the above, however the above doesn't perform properly for some reason
        time.sleep(0.5)

        return element

    except:
        logging.error(f'Exception when getting element')


def get_ctrl_key(action):
    try:
        return action['ctrlKey']
    except Keyerror as ke:
        logging.error('Current action doesn\'t have a ctrlKey attribute')


def get_key(action):
    try:
        return action['key']
    except Keyerror as ke:
        logging.error('Current action doesn\'t have a key attribute')


def get_window_size(action):
    try:
        window_width = action['windowOuterWidth']
        window_height = action['windowOuterHeight']
        return window_width, window_height
    except Keyerror as ke:
        logging.error('error getting window size : action has no "windowInnerWidth" or "windowInnerHeight" field.')


def get_keys_to_input(action):
    try:
        action_data = action["data"]
    except Keyerror as ke:
        logging.error('error getting keys to input : action has no "data" field.')

    return action_data


def get_scroll_params(action):
    try:
        return action['scrollX'], action['scrollY']
    except Exception as e:
        print('Exception getting the scrollX and scrollY property.')
        return None


def get_action_type(action: dict):
    # it is imposed that any action object within a flow has a type
    try:
        return action['type']
    except Keyerror:
        logging.error('Current action has no "type" property')
        return None


def get_value(action):
    try:
        action_target = action['target']
    except:
        logging.error('Current action has no "target" property')
    else:
        try:
            return action_target['value']
        except Keyerror as ke:
            logging.error('Current action target has no "value" property')


def get_start_end(action):
    try:
        action_target = action['target']
    except:
        logging.error('Current action has no "target" property')
    else:
        try:
            return action_target['selectionStart'], action_target['selectionEnd']
        except Keyerror as ke:
            logging.error('Current action target has no "selectionStart" or "selectionEnd" property')


def _get_element_xpath(element):
    try:
        return element['xpath']
    except:
        logging.error('error getting element xpath : element has no "xpath" field.')
    return None


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
