
from grongier.pex import BusinessOperation, Utils

import iris

import os
import datetime
import smtplib
from email.mime.text import MIMEText


class FileOperation(BusinessOperation):
    """
    This operation receive a PostMessage and write down in the right company
    .txt all the important information and the time of the operation
    """
    def on_init(self):
        if hasattr(self,'path'):
            os.chdir(self.path)

    def on_message(self, request):
        
        ts = title = fuel_mix =  demand = supply = ""
        fuel_mix = request.post.fuel_mix
        demand = request.post.demand
        supply = request.post.supply

        if (request.post is not None):
            title = request.post.title
            ts = datetime.datetime.fromtimestamp(request.post.created_utc).__str__()

        line = ts+" : "+title
        filename = title+".txt"

        self.put_line(filename, line)
        self.put_line(filename, "")
        self.put_line(filename, fuel_mix)
        self.put_line(filename, "")
        self.put_line(filename, demand)
        self.put_line(filename, "")
        self.put_line(filename, supply)
        self.put_line(filename, " * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

        return 

    def put_line(self,filename,string):
        try:
            with open(filename, "a",encoding="utf-8") as outfile:
                outfile.write(string)
        except Exception as e:
            raise e

