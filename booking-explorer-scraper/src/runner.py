thon
import sys
import json
from extractors.booking_parser import parse_booking_data
from outputs.data_exporter import export_data
from config.settings import load_settings

def run_scraper():
    settings = load_settings()
    hotel_data = parse_booking_data(settings["search_query"])
    export_data(hotel_data, settings["output_file"])

if __name__ == "__main__":
    run_scraper()