

REQUEST_BODY_JSON = """
{
    "from_place": "string",
    "to_place": "string",
    "travel_date_time": "2099-12-31 00:00:00",
    "is_flexible": true,
    "flexible_from_time": "2099-12-31 00:00:00",
    "no_of_assets": 1,
    "asset_type": "string",
    "asset_sensitivity": "HIGH_SENSITIVITY",
    "whom_to_deliver": "string"
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "string"
}
"""

