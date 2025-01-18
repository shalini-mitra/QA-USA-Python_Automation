import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance':'ALL'}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
                print("Connected to the Urban Routes server")
        else:
                print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(5)
        able_to_fill_from_field = urban_routes_page.get_from_field_text()
        assert able_to_fill_from_field, f'Failed to Enter the From address field'
        able_to_fill_to_field = urban_routes_page.get_to_field_text()
        assert able_to_fill_to_field, f'Failed to Enter the From address field'
        # The remaining steps are not needed, but they can be used for checking the full functionality
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'modes-container')))
        #WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(*urban_routes_page.ROUTE_OPTIONS_LOCATOR))
        is_route_options_displaying = urban_routes_page.get_route_options()
        assert is_route_options_displaying, "The router options panel is not displaying"
        actual_value = urban_routes_page.setting_the_route()
        expected_value = "Fastest"
        assert expected_value in actual_value, f'Failed to set the Route'

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(5)

        # Testing for selecting a plan
        urban_routes_page.calling_a_taxi()
        call_a_taxi_button_displaying = urban_routes_page.get_call_a_taxi_button()
        assert call_a_taxi_button_displaying, "'Call a taxi' button is not displaying on the page"
        urban_routes_page.click_taxi_icon()
        actual_plan = urban_routes_page.get_taxi_text()
        expected_plan = "Supportive"
        assert expected_plan in actual_plan, f'{expected_plan} should be displayed, but got {actual_plan}. Check line 34'

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(5)
        urban_routes_page.calling_a_taxi()
        call_a_taxi_button_displaying = urban_routes_page.get_call_a_taxi_button()
        assert call_a_taxi_button_displaying, "'Call a taxi' button is not displaying on the page"

        # Testing for filling Phone number
        urban_routes_page.select_phone_number()
        urban_routes_page.enter_the_phone_number_field(data.PHONE_NUMBER)
        actual_number = urban_routes_page.get_phone_number_value()
        #print(actual_number)
        expected_number = data.PHONE_NUMBER
        assert expected_number == actual_number, f'Phone number entry failed. Expected {expected_number}, but got {actual_number} in the phone number field'
        urban_routes_page.click_next_button()
        verification_code = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.enter_the_verification_code(verification_code)
        actual_verification_code = urban_routes_page.get_verification_code_value()
        expected_verification_code = verification_code
        assert expected_verification_code == actual_verification_code, f'Verification code entry failed. Expected {actual_verification_code}, but got {expected_verification_code}'
        urban_routes_page.click_confirm_button()
        assert self.driver.find_element(*urban_routes_page.PHONE_NUMBER_LOCATOR).get_property('textContent') == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(5)
        urban_routes_page.calling_a_taxi()
        call_a_taxi_button_displaying = urban_routes_page.get_call_a_taxi_button()
        assert call_a_taxi_button_displaying, "'Call a taxi' button is not displaying on the page"

        #Test filling the card
        urban_routes_page.select_payment_method()
        urban_routes_page.click_add_card()
        urban_routes_page.enter_card_number(data.CARD_NUMBER)
        entered_card_number = urban_routes_page.get_card_number()
        expected_card_number = data.CARD_NUMBER
        assert expected_card_number == entered_card_number, f"Failed to enter the card number"
        urban_routes_page.enter_card_code(data.CARD_CODE)
        entered_card_code = urban_routes_page.get_card_code()
        expected_card_code = data.CARD_CODE
        assert expected_card_code == entered_card_code, f"Failed to enter the correct card code"
        urban_routes_page.click_add_card_title()
        WebDriverWait(self.driver,3).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[text() = "Link"]')))
        urban_routes_page.click_link_button()
        urban_routes_page.click_close_payment_window()
        assert self.driver.find_element(*urban_routes_page.PAYMENT_METHOD_LOCATOR).get_property('textContent') == 'Card'


    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(5)
        able_to_fill_from_field = urban_routes_page.get_from_field_text()
        assert able_to_fill_from_field, f'Failed to Enter the From address field'
        able_to_fill_to_field = urban_routes_page.get_to_field_text()
        assert able_to_fill_to_field, f'Failed to Enter the To address field'
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'modes-container')))
        # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(*urban_routes_page.ROUTE_OPTIONS_LOCATOR))
        is_route_options_displaying = urban_routes_page.get_route_options()
        assert is_route_options_displaying, "The router options panel is not displaying"
        actual_value = urban_routes_page.setting_the_route()
        expected_value = "Fastest"
        assert expected_value in actual_value, f'Failed to set the Route'
        urban_routes_page.calling_a_taxi()
        call_a_taxi_button_displaying = urban_routes_page.get_call_a_taxi_button()
        assert call_a_taxi_button_displaying, "'Call a taxi' button is not displaying on the page"

        # Adding a comment for driver
        urban_routes_page.enter_message_driver(data.MESSAGE_FOR_DRIVER)
        able_to_comment_for_driver = urban_routes_page.get_message_to_driver()
        assert able_to_comment_for_driver, f" Unable to write a message for driver"

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(5)
        able_to_fill_from_field = urban_routes_page.get_from_field_text()
        assert able_to_fill_from_field, 'Failed to Enter the From address field'
        able_to_fill_to_field = urban_routes_page.get_to_field_text()
        assert able_to_fill_to_field, 'Failed to Enter the To address field'
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'modes-container')))
        # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(*urban_routes_page.ROUTE_OPTIONS_LOCATOR))
        is_route_options_displaying = urban_routes_page.get_route_options()
        assert is_route_options_displaying, "The router options panel is not displaying"
        actual_value = urban_routes_page.setting_the_route()
        expected_value = "Fastest"
        assert expected_value in actual_value, 'Failed to set the Route'
        urban_routes_page.calling_a_taxi()
        call_a_taxi_button_displaying = urban_routes_page.get_call_a_taxi_button()
        assert call_a_taxi_button_displaying, "'Call a taxi' button is not displaying on the page"
        urban_routes_page.click_taxi_icon()
        actual_plan = urban_routes_page.get_taxi_text()
        expected_plan = "Supportive"
        assert expected_plan in actual_plan, f'{expected_plan} should be displayed, but got {actual_plan}. Check line 34'

        # Testing the order blanket and handkerchiefs
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '(//span[@class = "slider round"])[1]')))
        urban_routes_page.turn_on_blanket_handkerchiefs_option()
        is_blanket_handkerchiefs_option_on = urban_routes_page.get_blanket_handkerchiefs_option_status()
        assert is_blanket_handkerchiefs_option_on, 'Order for blanket handkerchiefs failed'

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(5)
        able_to_fill_from_field = urban_routes_page.get_from_field_text()
        assert able_to_fill_from_field, 'Failed to Enter the From address field'
        able_to_fill_to_field = urban_routes_page.get_to_field_text()
        assert able_to_fill_to_field, 'Failed to Enter the To address field'
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'modes-container')))
        # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(*urban_routes_page.ROUTE_OPTIONS_LOCATOR))
        is_route_options_displaying = urban_routes_page.get_route_options()
        assert is_route_options_displaying, "The router options panel is not displaying"
        actual_value = urban_routes_page.setting_the_route()
        expected_value = "Fastest"
        assert expected_value in actual_value, 'Failed to set the Route'
        urban_routes_page.calling_a_taxi()
        call_a_taxi_button_displaying = urban_routes_page.get_call_a_taxi_button()
        assert call_a_taxi_button_displaying, "'Call a taxi' button is not displaying on the page"
        urban_routes_page.click_taxi_icon()
        actual_plan = urban_routes_page.get_taxi_text()
        expected_plan = "Supportive"
        assert expected_plan in actual_plan, f'{expected_plan} should be displayed, but got {actual_plan}. Check line 34'

        # Order 2 ice creams
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//div [@class = 'counter-value'])[1]")))
        ice_creams = 2
        for i in range(ice_creams):
            urban_routes_page.click_add_ice_cream()
        urban_routes_page.click_add_ice_cream()
        actual_ice_cream_quantity = urban_routes_page.get_ice_cream_quantity_locator()
        expected_ice_cream_quantity = '2'
        assert expected_ice_cream_quantity == actual_ice_cream_quantity, f" Expected ice cream quantity is {expected_ice_cream_quantity}, but got {actual_ice_cream_quantity}"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        self.driver.implicitly_wait(5)
        able_to_fill_from_field = urban_routes_page.get_from_field_text()
        assert able_to_fill_from_field, f'Failed to Enter the From address field'
        able_to_fill_to_field = urban_routes_page.get_to_field_text()
        assert able_to_fill_to_field, f'Failed to Enter the From address field'
        # The remaining steps are not needed, but they can be used for checking the full functionality
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'modes-container')))
        # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(*urban_routes_page.ROUTE_OPTIONS_LOCATOR))
        is_route_options_displaying = urban_routes_page.get_route_options()
        assert is_route_options_displaying, "The router options panel is not displaying"
        actual_value = urban_routes_page.setting_the_route()
        expected_value = "Fastest"
        assert expected_value in actual_value, f'Failed to set the Route'

        urban_routes_page.calling_a_taxi()
        call_a_taxi_button_displaying = urban_routes_page.get_call_a_taxi_button()
        assert call_a_taxi_button_displaying, "'Call a taxi' button is not displaying on the page"
        urban_routes_page.click_taxi_icon()
        actual_plan = urban_routes_page.get_taxi_text()
        expected_plan = "Supportive"
        assert expected_plan in actual_plan, f'{expected_plan} should be displayed, but got {actual_plan}. Check line 34'

        urban_routes_page.select_phone_number()
        urban_routes_page.enter_the_phone_number_field(data.PHONE_NUMBER)
        actual_number = urban_routes_page.get_phone_number_value()
        # print(actual_number)
        expected_number = data.PHONE_NUMBER
        assert expected_number == actual_number, f'Phone number entry failed. Expected {expected_number}, but got {actual_number} in the phone number field'
        urban_routes_page.click_next_button()
        verification_code = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.enter_the_verification_code(verification_code)
        actual_verification_code = urban_routes_page.get_verification_code_value()
        expected_verification_code = verification_code
        assert expected_verification_code == actual_verification_code, f'Verification code entry failed. Expected {actual_verification_code}, but got {expected_verification_code}'
        urban_routes_page.click_confirm_button()
        assert self.driver.find_element(*urban_routes_page.PHONE_NUMBER_LOCATOR).get_property('textContent') == data.PHONE_NUMBER

        urban_routes_page.select_payment_method()
        urban_routes_page.click_add_card()
        urban_routes_page.enter_card_number(data.CARD_NUMBER)
        entered_card_number = urban_routes_page.get_card_number()
        expected_card_number = data.CARD_NUMBER
        assert expected_card_number == entered_card_number, f"Failed to enter the card number"
        urban_routes_page.enter_card_code(data.CARD_CODE)
        entered_card_code = urban_routes_page.get_card_code()
        expected_card_code = data.CARD_CODE
        assert expected_card_code == entered_card_code, f"Failed to enter the correct card code"
        urban_routes_page.click_add_card_title()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[text() = "Link"]')))
        urban_routes_page.click_link_button()
        urban_routes_page.click_close_payment_window()
        assert self.driver.find_element(*urban_routes_page.PAYMENT_METHOD_LOCATOR).get_property('textContent') == 'Card'

        urban_routes_page.enter_message_driver(data.MESSAGE_FOR_DRIVER)
        able_to_comment_for_driver = urban_routes_page.get_message_to_driver()
        assert able_to_comment_for_driver, f" Unable to write a message for driver"

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '(//span[@class = "slider round"])[1]')))
        urban_routes_page.turn_on_blanket_handkerchiefs_option()
        is_blanket_handkerchiefs_option_on = urban_routes_page.get_blanket_handkerchiefs_option_status()
        assert is_blanket_handkerchiefs_option_on, 'Order for blanket handkerchiefs failed'

        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located((By.XPATH, "(//div [@class = 'counter-value'])[1]")))
        ice_creams = 2
        for i in range(ice_creams):
            urban_routes_page.click_add_ice_cream()
        urban_routes_page.click_add_ice_cream()
        actual_ice_cream_quantity = urban_routes_page.get_ice_cream_quantity_locator()
        expected_ice_cream_quantity = '2'
        assert expected_ice_cream_quantity == actual_ice_cream_quantity, f" Expected ice cream quantity is {expected_ice_cream_quantity}, but got {actual_ice_cream_quantity}"

        urban_routes_page.click_order_button()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[text() = "Car search"]')))
        actual_result = urban_routes_page.get_car_search_text()
        expected_result = "Car search"
        assert expected_result in actual_result, f'Expected {expected_result}, but got {actual_result}'
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "number" )))
        urban_routes_page.get_car_model_number()
        actual_car_model_number = urban_routes_page.get_car_model_number()
        assert actual_car_model_number, 'Failed to display the car model number'


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()