from asyncore import write
from grongier.pex import BusinessOperation
import os
import datetime


class CaliforniaOperation(BusinessOperation):
    """
    This operation receive a PostMessage and write down in the right company
    .txt all the important information and the time of the operation
    """
    def on_init(self):
        if hasattr(self,'path'):
            os.chdir(self.path)
    
    #write message to the file
    def on_message(self, request):
        write_to_file(request)
        
  
class PjmOperation(BusinessOperation):
    """
    This operation receive a PostMessage and write down in the right company
    .txt all the important information and the time of the operation
    """
    def on_init(self):
        if hasattr(self,'path'):
            os.chdir(self.path)

    #write message to the file
    def on_message(self, request):
        write_to_file(request)

class IsoneOperation(BusinessOperation):
    """
    This operation receive a PostMessage and write down in the right company
    .txt all the important information and the time of the operation
    """
    def on_init(self):
        if hasattr(self,'path'):
            os.chdir(self.path)

    #write message to the file
    def on_message(self, request):
        write_to_file(request)

#Funtion to write file based on the request.title
def write_to_file(request):
    ts = title = fuel_mix =  demand = supply = ""
    fuel_mix = request.post.fuel_mix
    demand = request.post.demand
    supply = request.post.supply

    if (request.post is not None):
        title = request.post.title
        ts = datetime.datetime.fromtimestamp(request.post.created_utc).__str__()

    line = ts+" : "+title
    filename = title+".txt"

    put_line(filename, line)
    put_line(filename, "")
    put_line(filename, fuel_mix)
    put_line(filename, "")
    put_line(filename, demand)
    put_line(filename, "")
    put_line(filename, supply)
    put_line(filename, " * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

    return 

def put_line(filename,string):
        try:
            with open(filename, "a",encoding="utf-8") as outfile:
                outfile.write(string)
        except Exception as e:
            raise e            