from datetime import datetime
from functools import wraps
from Backend.Database.Components.db_models import ViolationImage
from Backend.Database.Components.db_session import default_session, Session

from sqlalchemy import desc, func


class DatabaseManager:

    def __init__(self, session: Session = default_session):
        self.session = session

    def auto_session(func):
        """decorator design pattern automatically handles session management for each method by committing changes to the session upon successful execution and rolling back changes in case of an exception."""
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                result = func(self, *args, **kwargs)
                self.session.commit()
                return result
            except Exception as e:
                self.session.rollback()
                raise ValueError(">>> ERROR:",e)
            finally:
                self.session.close()

        return wrapper
    
    # CRUD Image
    @auto_session
    def create_image(self,
                data: bytes,
                license_plate :str,
                speed:int,
                speed_limit:int,
                record_time:datetime,
                latitude:float,
                longitude:float,
                device_info: str,
                distance:float = None,
                name: str = None,
                road_address: str = None,
                description: str = None,
                vehicle_type: str = None,
                capture_direction:str = None):
        # Check null
        if not data:
            return False
        if not license_plate:
            return False
        if not speed:
            return False
        if not speed_limit:
            return False
        if not record_time:
            return False
        if not latitude:
            return False
        if not longitude:
            return False
        # Create a new image
        image = ViolationImage(data = data,
                    license_plate = license_plate,
                    speed = speed,
                    speed_limit = speed_limit,
                    distance = distance,
                    record_time = record_time,
                    latitude = latitude,
                    longitude = longitude,
                    name = name,
                    road_address = road_address,
                    description = description,
                    vehicle_type = vehicle_type,
                    capture_direction = capture_direction,
                    device_info = device_info)
        self.session.add(image)
        return True
    
    def get_images(self):
        images = self.session.query(ViolationImage).order_by(ViolationImage.record_time).all()
        self.session.close()
        return images
    
    @auto_session
    def update_image(self,
                id: int,
                data: bytes,
                license_plate :str,
                speed:int,
                speed_limit:int,
                record_time:datetime,
                latitude:float,
                longitude:float,
                device_info: str,
                distance:float = None,
                name: str = None,
                road_address: str = None,
                description: str = None,
                vehicle_type: str = None,
                capture_direction:str = None):
        # Check null
        if not id:
            return False
        if not data:
            return False
        if not license_plate:
            return False
        if not speed:
            return False
        if not speed_limit:
            return False
        if not record_time:
            return False
        if not latitude:
            return False
        if not longitude:
            return False
        
        # Get image
        image = self.session.query(ViolationImage).get(id)
        if not image:
            return False

        # Update that image
        image.data = data
        image.license_plate = license_plate
        image.speed = speed
        image.speed_limit = speed_limit
        image.record_time = record_time
        image.latitude = latitude
        image.longitude = longitude
        image.device_info = device_info
        if name:
            image.name = name
        if road_address:
            image.road_address = road_address
        if description:
            image.description = description
        if vehicle_type:
            image.vehicle_type = vehicle_type
        if capture_direction:
            image.capture_direction = capture_direction
        if distance:
            image.distance = distance
        return True
    
    @auto_session
    def delete_image(self,
                     id:int):
        # Check null
        if not id:
            return False
        
        # Get image
        image = self.session.query(ViolationImage).get(id)
        if not image:
            return False
        
        # Delete that image
        self.session.delete(image)
        return True

class ImageDatabaseManager:
    def __init__(self):
        self.session = default_session
        soonest_record = self.session.query(ViolationImage).order_by(desc(ViolationImage.record_time)).first()
        self.current_record = soonest_record
        self.current_index = 0
        number_of_records = self.session.query(func.count(ViolationImage.id)).scalar()
        self.max_index = number_of_records - 1  # Don't forget to set the max_index accordingly

    def close(self):
        self.session.close()

    def get_current_record(self):
        return self.current_record
    
    def next(self):
        if self.current_record:
            next_record = self.session.query(ViolationImage).filter(ViolationImage.record_time > self.current_record.record_time).order_by(ViolationImage.record_time).first()
            if next_record:
                self.current_record = next_record
                self.current_index += 1
            return next_record
        
    def previous(self):
        if self.current_record:
            previous_record = self.session.query(ViolationImage).filter(ViolationImage.record_time < self.current_record.record_time).order_by(desc(ViolationImage.record_time)).first()
            if previous_record:
                self.current_record = previous_record
                self.current_index -= 1
            return previous_record
   
if __name__ == "__main__":
    # Create an instance of ImageDatabaseManager
    manager = ImageDatabaseManager()

    # Get the current record
    current_record = manager.get_current_record()

    # Print information about the current record
    if current_record:
        print(f">>> Current Record ID: {current_record.id}")
        print(f">>> Record Time: {current_record.record_time}")
        # Print other relevant fields here

    # Move to the previous record and query until the end
    while True:
        previous_record = manager.previous()
        if previous_record:
            print(f">>> Prev Record ID: {previous_record.id}")
            print(f">>> Prev Time: {previous_record.record_time}")
            # Print other relevant fields here
        else:
            # No more records, break the loop
            break

    # Move to the next record and query until the end
    while True:
        next_record = manager.next()
        if next_record:
            print(f">>> Next Record ID: {next_record.id}")
            print(f">>> Record Time: {next_record.record_time}")
            # Print other relevant fields here
        else:
            # No more records, break the loop
            break

    # Close the session when you're done
    manager.close()
    