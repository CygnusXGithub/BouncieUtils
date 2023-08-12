# client.py

import requests

class BouncieClient:
    BASE_URL = "https://api.bouncie.dev/v1"
    
    def __init__(self, access_token):
        self.access_token = access_token

    def search_vehicles(self, vin=None, imei=None, limit=None, skip=None):
        """
        Search for vehicles based on the provided criteria.
        
        Args:
        - vin (str, optional): Vehicles with VIN matching the given value.
        - imei (str, optional): Vehicles with IMEI matching the given value.
        - limit (str, optional): Number of search results to limit (for paging).
        - skip (str, optional): Number of search results to skip (for paging).
        
        Returns:
        - list: A list of vehicles matching the given criteria.
        """
        headers = {
            "Authorization": self.access_token
        }
        
        params = {}
        if vin:
            params["vin"] = vin
        if imei:
            params["imei"] = imei
        if limit:
            params["limit"] = limit
        if skip:
            params["skip"] = skip
        
        response = requests.get(f"{self.BASE_URL}/vehicles", headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def search_trips(self, imei, gps_format, transaction_id=None, starts_after=None, ends_before=None):
        """
        Search for trips based on the provided criteria.
        
        Args:
        - imei (str): IMEI for the vehicle to retrieve trips for.
        - gps_format (str): One of: 'polyline' or 'geojson'.
        - transaction_id (str, optional): Unique Trip Identifier.
        - starts_after (str, optional): ISODate - Will match trips with a starting time after this parameter.
        - ends_before (str, optional): ISODate - Will match trips with an ending time before this parameter.
        
        Returns:
        - list: A list of trips matching the given criteria.
        """
        headers = {
            "Authorization": self.access_token
        }
        
        params = {
            "imei": imei,
            "gps-format": gps_format
        }
        if transaction_id:
            params["transaction-id"] = transaction_id
        if starts_after:
            params["starts-after"] = starts_after
        if ends_before:
            params["ends-before"] = ends_before
        
        response = requests.get(f"{self.BASE_URL}/trips", headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()