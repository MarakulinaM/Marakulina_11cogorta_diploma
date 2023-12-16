import sender_stand_request
import data

track = sender_stand_request.get_track()

def test_check_order_track():
    order_response = sender_stand_request.check_order()
    assert order_response.status_code == 200