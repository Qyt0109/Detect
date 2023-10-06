from sqlalchemy import Table, create_engine, ForeignKey, Column, Integer, Float, BLOB,Boolean, DATETIME, String, LargeBinary, DateTime, Text, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from Backend.Common.defined_constants import ImageCaptureDirections

#from Crypto.Hash import SHA256

# Create a base class for declarative models
Base = declarative_base()

class ViolationImage(Base):
    """Hình ảnh vi phạm căn cứ xử phạt (Bản ảnh chuẩn hoá)\n
    Một hình ảnh có thể được sử dụng để làm căn cứ xử phạt cần phải có đủ những yếu tố được quy định trong Thông tư 65/2020/TT-BCA [3] như sau:
    - Điểm ngắm bắn tốc độ (dấu chấm đỏ) đúng vào xe vi phạm
    - Có thời gian (đầy đủ định dạng ngày, tháng, năm, giờ, phút, giây) tại thời điểm bắn tốc độ
    - Có tọa độ nơi chụp được hình ảnh vi phạm. Trường hợp thiết bị ghi hình không có chức năng xác định địa điểm thì trong phiếu xác nhận kết quả thiết bị ghi hình phải ghi rõ địa điểm ghi hình
    - Có điểm giằng (như biển báo, cột điện, nhà cửa… có vị trí cố định) mà không có ở chỗ khác để xác định vị trí của xe trên thực tế có đang đi trên đoạn đường hạn chế tốc độ không
    - Biển số xe vi phạm phải rõ nét, không bị mờ, loá, che mất ký tự,... để khẳng định đúng là xe đó vi phạm;
    - Hiện tốc độ xe chạy thực tế tại thời điểm bị bắn tốc độ
    """
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    data = Column(BLOB, nullable=False)
    vehicle_type = Column(String)
    license_plate = Column(String, nullable=False)
    speed = Column(Integer, nullable=False)
    speed_limit = Column(Integer, nullable=False)
    distance = Column(Float)
    capture_direction = Column(String)
    record_time = Column(DateTime, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    road_address = Column(String)
    description = Column(String)
    device_info = Column(String, nullable=False)

    def __init__(self,
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
        self.data = data
        self.license_plate = license_plate
        self.speed = speed
        self.speed_limit = speed_limit
        self.distance = distance
        self.record_time = record_time
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.road_address = road_address
        self.description = description
        self.vehicle_type = vehicle_type
        self.capture_direction = capture_direction
        self.device_info = device_info

    def __repr__(self):
        return f"### BEGIN IMAGE ### >>\
        id: {self.id}, name: {self.name}, \
        data: {self.data[:20] + b'...' if len(self.data) > 20 else {self.data}}, \
        lisence plate number: {self.license_plate}, \
        spd: {self.speed}, spd limit: {self.speed_limit}, \
        road address: {self.road_address}, \
        vehicle type: {self.vehicle_type}, \
        device info: {self.device_info}, capture datetime: {self.record_time}, \
        capture direction: {self.capture_direction}, speed: {self.speed}, \
        distance: {self.distance}, lat, lon: {self.latitude}, {self.longitude}, \
        description: {self.description}\
        << ### END IMAGE ###"

"""
# One-to-one
class Citizen(Base):

    __tablename__ = "citizen"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

    # Relationships
    passport = relationship("Passport")

class Passport(Base):

    __tablename__ = "passport"

    id = Column(Integer, primary_key=True)
    citizen_id = Column(Integer, ForeignKey("citizen.id"))
    passport_id = Column(String(25), unique=True, nullable=False)

    # Relationships
    citizen = relationship("Citizen")

# One-to-many
class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    orders = relationship("Order", back_populates="customer")

class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))

    # Relationship
    customer = relationship("Customer", back_populates="orders")

# For example, to get the orders for a customer, we can write:
customer = session.query(Customer).get(1)
orders = customer.orders

# For example, to get the customer for an order, we can write:
order = session.query(Order).get(1)
customer = order.customer

Many-to-many
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Relationship
    courses = relationship("Course", secondary="student_course", back_populates="students")

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Relationship
    students = relationship("Student", secondary="student_course", back_populates="courses")

class StudentCourse(Base):
    __tablename__ = 'student_course'
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'), primary_key=True)

# For example, to get the courses for a student, we can write:
student = session.query(Student).get(1)
courses = student.courses
"""

"""
Sure! Here are some examples of how you can perform CRUD operations on the Users and Clients models with the many-to-many relationship:

Create a new user and associate it with one or more clients:
python
Copy code
# Create a new user
new_user = Users(username='john', password='password123', role='admin')

# Add clients to the user's clients list
client1 = Clients(id=b'client1')
client2 = Clients(id=b'client2')
new_user.clients.extend([client1, client2])

# Add the user to the session and commit the changes
session.add(new_user)
session.commit()
Get all clients associated with a specific user:
python
Copy code
# Get a specific user by username
user = session.query(Users).filter_by(username='john').first()

# Access the associated clients using the clients attribute
clients = user.clients
for client in clients:
    print(client.id)
Add a new client and associate it with one or more existing users:
python
Copy code
# Create a new client
new_client = Clients(id=b'client3')

# Get existing users
users = session.query(Users).filter(Users.username.in_(['john', 'alice'])).all()

# Add the new client to each user's clients list
for user in users:
    user.clients.append(new_client)

# Commit the changes
session.commit()
Remove a client from a user's clients list:
python
Copy code
# Get a specific user by username
user = session.query(Users).filter_by(username='john').first()

# Remove a client from the user's clients list
client_to_remove = session.query(Clients).filter_by(id=b'client1').first()
user.clients.remove(client_to_remove)

# Commit the changes
session.commit()
Delete a user and automatically remove the association with clients:
python
Copy code
# Get a specific user by username
user = session.query(Users).filter_by(username='john').first()

# Delete the user
session.delete(user)

# Commit the changes
session.commit()
These examples demonstrate how to create, read, update, and delete data in the Users and Clients models while maintaining the many-to-many relationship.
"""