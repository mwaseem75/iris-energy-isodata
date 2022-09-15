from pickle import NONE
from grongier.pex import BusinessService
import json
import requests
import isodata
from message import PostMessage
from obj import PostClass

#Service to get data by using isodata library


#Service to get data by using isodata library
class CaliforniaService(BusinessService):
    """
    This service use an Ens.InboundAdapter to, on_process_input every 5
    seconds, use requests to fetch self.limit posts as data from the isodata
    API before calling the FilterPostRoutingRule process.
    """
    def get_adapter_type():
        """
        Name of the registred Adapter
        """
        
        return "Ens.InboundAdapter"

    def on_init(self):
        
        if not hasattr(self,'feed'):
            self.feed = "/new/"
        
        if not hasattr(self,'limit'):
            raise TypeError('no limit field')

        if not hasattr(self,'target'):
            self.target = "Isodata.FilterRoutingRule"
        
        self.last_post_name = ""
        
        return 1

    def on_process_input(self,request):

        post = self.on_task()
        if post is not None:
            msg = PostMessage()
            msg.post = post
            self.send_request_sync(self.target,msg)

    def on_task(self) -> PostClass:
          
        try:                    
            data = json.loads("""{"data":{"children":[{"kind": "t3", "data": {"title": "", "name": "", "created_utc": 1647879710.0}}]}}""")
            updateLast = 0

            iso = isodata.get_iso('caiso')
            caiso = iso()
            #Get fuel mix
            getdata = str(caiso.get_latest_fuel_mix())
            #Get Demand
            demandpd = caiso.get_demand_today()
            demand = str(demandpd['Demand'].iloc[0])
            #Get Supply
            supplypd = caiso.get_supply_today()
            supply = str(supplypd['Supply'].iloc[0])
                
            for key, value in enumerate(data['data']['children']):
                              
                post = PostClass.from_dict(value['data'])
                post.fuel_mix = getdata
                post.title="caiso"
                post.demand = demand+" NW"
                post.supply = supply+" NW"

                if not updateLast:
                    self.last_post_name = value['data']['name']
                    updateLast = 1
                    return post

        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 429:
                self.log_warning(err.__str__())
            else:
                raise err
        except Exception as err: 
            self.log_error(err.__str__())
            raise err

        return None 


#Service to get data by using isodata library
class PjmService(BusinessService):
    """
    This service use an Ens.InboundAdapter to, on_process_input every 5
    seconds, use requests to fetch self.limit posts as data from the isodata
    API before calling the FilterPostRoutingRule process.
    """
    def get_adapter_type():
        """
        Name of the registred Adapter
        """
        
        return "Ens.InboundAdapter"

    def on_init(self):
        
        if not hasattr(self,'feed'):
            self.feed = "/new/"
        
        if not hasattr(self,'limit'):
            raise TypeError('no limit field')

        if not hasattr(self,'target'):
            self.target = "Isodata.FilterRoutingRule"
        
        self.last_post_name = ""
        
        return 1

    def on_process_input(self,request):

        post = self.on_task()
        if post is not None:
            msg = PostMessage()
            msg.post = post
            self.send_request_sync(self.target,msg)

    def on_task(self) -> PostClass:
          
        try:                    
            data = json.loads("""{"data":{"children":[{"kind": "t3", "data": {"title": "", "name": "", "created_utc": 1647879710.0}}]}}""")
            updateLast = 0

            iso = isodata.get_iso('pjm')
            caiso = iso()
            #Get fuel mix
            getdata = str(caiso.get_latest_fuel_mix())
            #Get Demand
            demandpd = caiso.get_demand_today()
            demand = str(demandpd['Demand'].iloc[0])
            #Get Supply
            supplypd = caiso.get_supply_today()
            supply = str(supplypd['Supply'].iloc[0])
                
            for key, value in enumerate(data['data']['children']):
                              
                post = PostClass.from_dict(value['data'])
                post.fuel_mix = getdata
                post.title="pjm"
                post.demand = demand+" NW"
                post.supply = supply+" NW"

                if not updateLast:
                    self.last_post_name = value['data']['name']
                    updateLast = 1
                    return post

        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 429:
                self.log_warning(err.__str__())
            else:
                raise err
        except Exception as err: 
            self.log_error(err.__str__())
            raise err

        return None 

         
#Service to get data by using isodata library
class IsoneService(BusinessService):
    """
    This service use an Ens.InboundAdapter to, on_process_input every 5
    seconds, use requests to fetch self.limit posts as data from the isodata
    API before calling the FilterPostRoutingRule process.
    """
    def get_adapter_type():
        """
        Name of the registred Adapter
        """
        
        return "Ens.InboundAdapter"

    def on_init(self):
        
        if not hasattr(self,'feed'):
            self.feed = "/new/"
        
        if not hasattr(self,'limit'):
            raise TypeError('no limit field')

        if not hasattr(self,'target'):
            self.target = "Isodata.FilterRoutingRule"
        
        self.last_post_name = ""
        
        return 1

    def on_process_input(self,request):

        post = self.on_task()
        if post is not None:
            msg = PostMessage()
            msg.post = post
            self.send_request_sync(self.target,msg)

    def on_task(self) -> PostClass:
          
        try:                    
            data = json.loads("""{"data":{"children":[{"kind": "t3", "data": {"title": "", "name": "", "created_utc": 1647879710.0}}]}}""")
            updateLast = 0

            iso = isodata.get_iso('isone')
            caiso = iso()
            #Get fuel mix
            getdata = str(caiso.get_latest_fuel_mix())
            #Get Demand
            demandpd = caiso.get_demand_today()
            demand = str(demandpd['Demand'].iloc[0])
            #Get Supply
            supplypd = caiso.get_supply_today()
            supply = str(supplypd['Supply'].iloc[0])
                
            for key, value in enumerate(data['data']['children']):
                              
                post = PostClass.from_dict(value['data'])
                post.fuel_mix = getdata
                post.title="isone"
                post.demand = demand+" NW"
                post.supply = supply+" NW"

                if not updateLast:
                    self.last_post_name = value['data']['name']
                    updateLast = 1
                    return post

        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 429:
                self.log_warning(err.__str__())
            else:
                raise err
        except Exception as err: 
            self.log_error(err.__str__())
            raise err

        return None         