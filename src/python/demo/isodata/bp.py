from grongier.pex import BusinessProcess

from message import PostMessage
from obj import PostClass

import iris

class FilterPostRoutingRule(BusinessProcess):
    """
    This process receive a PostMessage and send to operation based on the title
    """
    def on_init(self):
        
        if not hasattr(self,'target'):
            self.target = "Isodata.CaliforniaOperation"
        
        return

    def iris_to_python(self, request:'iris.dc.Demo.PostMessage'):

        request = PostMessage(post=PostClass(title=request.Post.Title,                                             
                                             created_utc=request.Post.CreatedUTC,
                                             fuel_mix=request.Post.OriginalJSON))
        return self.on_python_message(request)

    def on_python_message(self, request: PostMessage):
        if 'caiso'.upper() in request.post.title.upper():
            target = "Isodata.CaliforniaOperation" 
        elif 'ercot'.upper() in request.post.title.upper():
            target = "Isodata.TexasOperation"
        elif 'nyiso'.upper() in request.post.title.upper():
            target = "Isodata.NewYorkOperation"
        elif 'spp'.upper() in request.post.title.upper():
            target = "Isodata.SouthWestOperation"
        elif 'pjm'.upper() in request.post.title.upper():
            target = "Isodata.PjmOperation"
        elif 'miso'.upper() in request.post.title.upper():
            target = "Isodata.MidcontinentOperation"    
        elif 'isone'.upper() in request.post.title.upper():
            target = "Isodata.IsoneOperation"                                

        if target is not None:
            self.send_request_sync(target,request)
            rsp = iris.cls('Ens.StringResponse')._New(f"{request.post.title}")
            return rsp
        else:
            return
