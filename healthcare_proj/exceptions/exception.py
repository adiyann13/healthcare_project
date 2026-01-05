import os
import sys

class CustomException(Exception):
    def __init__(self, error_mssg , error_details:sys):
        self.error_mssg = error_mssg
        _, _,tb = error_details.exc_info()
        self.filename = tb.tb_frame.f_code.co_filename
        self.lineno = tb.tb_lineno
    
    def __str__(self):
        return f"{self.error_mssg} in {self.filename} at line {self.lineno}"
    


