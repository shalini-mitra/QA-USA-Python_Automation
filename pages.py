from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

    # Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, "from")
    TO_LOCATOR = (By.ID, "to")
    CALL_A_TAXI_BUTTON = (By.XPATH, '//button[text() = "Call a taxi"]')
    TAXI_ICON_LOCATOR = (By.XPATH,'(// img[@ src = "/static/media/kids.27f92282.svg"])[1]')
    TAXI_TEXT_LOCATOR = (By.XPATH, '(//div[text() = "Supportive"])[1]')
    PHONE_NUMBER_LOCATOR = (By.CLASS_NAME, 'np-text')
    PHONE_NUMBER_FIELD_LOCATOR = (By.ID, 'phone')
    ENTER_THE_VERIFICATION_CODE_LOCATOR = (By.XPATH, '//input[@id = "code"][1]')
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text() = "Next"]')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[text() = "Confirm"]')
    PAYMENT_METHOD_LOCATOR = (By.CLASS_NAME, "pp-value-text")
    ADD_CARD_LOCATOR = (By.XPATH, '//div[text() = "Add card"]')
    CARD_NUMBER_FILED_LOCATOR = (By.ID, 'number')
    CARD_CODE_LOCATOR = (By.NAME, 'code')
    ADDING_A_CARD_TITLE_LOCATOR = (By.XPATH,'//div[text() = "Adding a card"]')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//button[text() = "Link"]')
    CLOSE_PAYMENT_METHOD_LOCATOR = (By.XPATH, '(//button[@class = "close-button section-close"])[3]')
    MESSAGE_TO_THE_DRIVER_LOCATOR = (By.ID, 'comment')
    BLANKET_AND_HANDKERCHIEFS_BUTTON_LOCATOR = (By.XPATH,'(//span[@class = "slider round"])[1]')
    ICE_CREAM_PLUS_OPTION_LOCATOR = (By.XPATH, '//div[@class = "counter-plus"][1]')
    ORDER_BUTTON_LOCATOR = (By.XPATH, '//span[text() = "Order"]')
    CAR_SEARCH_TEXT_LOCATOR =  (By.XPATH, '//div[text() = "Car search"]')
    CAR_MODEL_NUMBER_LOCATOR = (By.CLASS_NAME, "number" )
    ROUTE_OPTIONS_LOCATOR = (By.CLASS_NAME, 'modes-container')
    BLANKET_AND_HANDKERCHIEFS_CHECK_LOCATOR = (By.CLASS_NAME, 'switch-input')
    ICE_CREAM_QUANTITY_LOCATOR = (By.XPATH, "(//div [@class = 'counter-value'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        # Enter the From Address Field
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Enter the To Address Field
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def calling_a_taxi(self):
        # Click on Call a taxi button
        self.driver.find_element(*self.CALL_A_TAXI_BUTTON).click()

    def click_taxi_icon(self):
        # Select the taxi option
        self.driver.find_element(*self.TAXI_ICON_LOCATOR).click()

    def get_taxi_text(self):
        # Return the taxi text
        return self.driver.find_element(*self.TAXI_TEXT_LOCATOR).text

    def select_phone_number(self):
        # Click on Phone number field
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()

    def enter_the_phone_number_field(self, phone_number):
        # Enter the Phone number
        self.driver.find_element(*self.PHONE_NUMBER_FIELD_LOCATOR).send_keys(phone_number)

    def enter_the_verification_code(self, verification_code):
        # Enter the verification code
        self.driver.find_element(*self.ENTER_THE_VERIFICATION_CODE_LOCATOR).send_keys(verification_code)

    def click_next_button(self):
        # Click on 'Next' Button
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def click_confirm_button(self):
        # Click on Confirm button
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def select_payment_method(self):
        # Click on Payment method
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

    def click_add_card(self):
        # Click on add card number
        self.driver.find_element(*self.ADD_CARD_LOCATOR).click()

    def enter_card_number(self, card_number):
        # Enter the card number for payment
        self.driver.find_element(*self.CARD_NUMBER_FILED_LOCATOR).send_keys(card_number)

    def enter_card_code(self, card_code):
        # Enter the card code
        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(card_code)

    def click_add_card_title(self):
        # Click on add card title
        self.driver.find_element(*self.ADDING_A_CARD_TITLE_LOCATOR).click()

    def click_link_button(self):
        # Click on 'Link' button
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def click_close_payment_window(self):
        # Close the payment method window
        self.driver.find_element(*self.CLOSE_PAYMENT_METHOD_LOCATOR).click()

    def enter_message_driver(self, message):
        # Write a Message to driver
        self.driver.find_element(*self.MESSAGE_TO_THE_DRIVER_LOCATOR).send_keys(message)

    def turn_on_blanket_handkerchiefs_option(self):
        # Add blanket and handkerchiefs to order
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_BUTTON_LOCATOR).click()

    def click_add_ice_cream(self):
        # Add ice cream to order
        self.driver.find_element(*self.ICE_CREAM_PLUS_OPTION_LOCATOR).click()

    def click_order_button(self):
        # Click on Order button
        self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).click()

    def get_car_search_text(self):
        # Return Car search text
        return self.driver.find_element(*self.CAR_SEARCH_TEXT_LOCATOR).text

    def get_car_model_number(self):
        # Return car model number
        return self.driver.find_element(*self.CAR_MODEL_NUMBER_LOCATOR).is_displayed()

        # One step for enter locations
    def enter_locations(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def get_phone_number_value(self):
        return self.driver.find_element(*self.PHONE_NUMBER_FIELD_LOCATOR).get_attribute('value')

    def get_verification_code_value(self):
        return self.driver.find_element(*self.ENTER_THE_VERIFICATION_CODE_LOCATOR).get_attribute('value')

    def setting_the_route(self):
        return self.driver.find_element(*self.ROUTE_OPTIONS_LOCATOR).text

    def get_route_options(self):
        #try:

        return self.driver.find_element(*self.ROUTE_OPTIONS_LOCATOR).is_displayed()
        #except NoSuchElementException:
            #return False

    def get_call_a_taxi_button(self):
        return self.driver.find_element(*self.CALL_A_TAXI_BUTTON).is_displayed()

    def get_from_field_text(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute("value")

    def get_to_field_text(self):
        return self.driver.find_element(*self. TO_LOCATOR).get_attribute("value")

    def get_card_number(self):
        return self.driver.find_element(*self.CARD_NUMBER_FILED_LOCATOR).get_attribute('Value')

    def get_card_code(self):
        return self.driver.find_element(*self.CARD_CODE_LOCATOR).get_attribute('Value')

    def get_message_to_driver(self):
        return self.driver.find_element(*self.MESSAGE_TO_THE_DRIVER_LOCATOR).get_attribute("value")

    def get_blanket_handkerchiefs_option_status(self):
        return self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_CHECK_LOCATOR).get_property("checked")

    def get_ice_cream_quantity_locator(self):
        return self.driver.find_element(*self.ICE_CREAM_QUANTITY_LOCATOR).get_attribute('textContent')

