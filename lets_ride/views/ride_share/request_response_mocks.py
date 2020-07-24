

REQUEST_BODY_JSON = """
{
    "from_place": "string",
    "to_place": "string",
    "is_flexible": true,
    "flexible_from_time": "2099-12-31 00:00:00",
    "flexible_to_time": "2099-12-31 00:00:00",
    "travel_date_time": "2099-12-31 00:00:00",
    "no_of_seats_available": 1,
    "assets_quantity": 1
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_FLEXIBLE_DATETIME"
}
"""

