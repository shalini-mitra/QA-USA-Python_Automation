import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
       if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
        print("Connected to the Urban Routes server")
       else:
           print("Cannot connect to Urban Routes. Check the server is on and still running")
# Add in S8
    def test_set_route(self):
        print("Function created for set route")
# Add in S8
    def test_select_plan(self):
        print("Function created for select plan")
        pass
    # Add in S8
    def test_fill_phone_number(self):
        print("Function created for fill phone number")
        pass
    # Add in S8
    def test_fill_card(self):
        print("Function created for fill card")
        pass
    # Add in S8
    def test_comment_for_driver(self):
        print("Function created for comment for driver")
        pass
    # Add in S8
    def test_order_blanket_and_handkerchiefs(self):
        print("Function created for order blanket and handkerchiefs")
        pass
    # Add in S8
    def test_order_2_ice_creams(self):
        print("Function created for order 2 ice creams")
        for i in range(2):
    # Add in S8
            pass

    # Add in S8
    def test_car_search_model_appears(self):
        print("Function created for car search model appears ")
        pass