from sqlalchemy import create_engine
import sys


def organize_booking(booking_name, pas_in_booking, empty_seats_per_row,
        empty_seats, cols, engine):
    pass


def find_allocation_order(number_of_pas, cols, empty_seats_per_row):
    pass


def write_database(engine, command, data):
    pass


def main():
    # Get command line arguments

    # Read in bookings information

    # Create connection engine to database

    # Retrieve rows and seats information from rows_cols table

    # For each booking in the list of bookings
    for booking in bookings:
        # Set booking name and number of passengers in booking

        # If passengers in booking is invalid (negative)

        # Retrieve seat map from database, and refresh metrics

        # If no empty seats available

        # Build the allocation order

        # If the allocation order has splits

        # If allocation order has no splits
        pass


if __name__ == '__main__':
    main()