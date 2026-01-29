import sys 
from ML_PROJECT.logger import logging


def error_detail(error_message,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    line_number=exc_tb.tb_lineno
    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message=f"Error occured in script :[{file_name}] at line number :[{line_number}] error message :[{error_message}]"
    return error_message


class CustomException(Exception):
    def __init__(self, message,error_detail:sys):
        super().__init__(message)
        self.message=message
        self.error_detail=error_detail(error_message,error_details)

    def __str__(self):
        return f"{self.message}  {self.error_detail}"
    