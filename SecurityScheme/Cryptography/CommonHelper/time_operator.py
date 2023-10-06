from datetime import datetime


class TimeOperator:
    @staticmethod
    def GetCurrentTime():
        """
        Get current time\n
        -> datetime
        """
        current_time = datetime.now()
        return current_time
    
    @staticmethod
    def TimeToBinary(time):
        """
        Convert datetime to binary utf-8 format\n
        + time: datetime to convert\n
        -> bytes
        """
        if not isinstance(time, datetime):
            raise ValueError("Invalid datetime object")

        binary_time = time.strftime('%d%m%Y%H%M%S').encode('utf-8')
        return binary_time
    
    @staticmethod
    def BinaryToTime(binary_time):
        """
        Convert binary utf-8 format to datetime\n
        + binary_time: binary utf-8 format to convert\n
        -> datetime
        """
        if not isinstance(binary_time, bytes):
            raise ValueError("Invalid binary data")
        
        try:
            decoded_time = datetime.strptime(binary_time.decode('utf-8'), '%d%m%Y%H%M%S')
        except ValueError as e:
            raise ValueError("Failed to decode binary data") from e
        
        return decoded_time
