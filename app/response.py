

class Response_:
    
    def success_message(response):
        return {
            "status_code":200,
            "message":"successfully",
            "response":response
        }
    
    def upload_message(response):
        return {
            "status_code":201,
            "message":"data create successfully",
            "response":response
        }
    
    def unprocess_message(response):
        return {
            "status_code":404,
            "message":"un-process entity",
            "response":response
        }
    
    def internalserver(response):
        return {
            "status_code":500,
            "message":"internal server error",
            "response":response
        }
    
    def conflict(response):
        return {
            "status_code":409,
            "message":"intity already exists",
            "response":response
        }
    
    def unauthorised(response):
        return {
            "status_code":401,
            "message":"intity already exists",
            "response":response
        }



