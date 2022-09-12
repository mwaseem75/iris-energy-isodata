from grongier.pex import BusinessService

import iris

import json
import requests
import isodata
from message import PostMessage
from obj import PostClass


class FuelMixService(BusinessService):
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
            # data = response.json()
            data = json.loads("""
                {"data":{"children":[{"kind": "t3", "data": {"approved_at_utc": null, "subreddit": "Livros", "author_fullname": "t2_1g037lor", "saved": false, "mod_reason_title": null, "gilded": 0, "clicked": false, "title": "VENDER LIVROS \\u00c9 UM DOS TRABALHO MAIS SIGNIFICANTES EM UMA \\u00c9POCA DE OBSCURANTISMO.", "link_flair_richtext": [], "subreddit_name_prefixed": "r/Livros", "hidden": false, "pwls": null, "link_flair_css_class": "", "downs": 0, "thumbnail_height": null, "top_awarded_type": null, "hide_score": true, "name": "t3_tjflyd", "quarantine": false, "link_flair_text_color": "light", "upvote_ratio": 1.0, "author_flair_background_color": null, "subreddit_type": "public", "ups": 1, "total_awards_received": 0, "media_embed": {}, "thumbnail_width": null, "author_flair_template_id": null, "is_original_content": false, "user_reports": [], "secure_media": null, "is_reddit_media_domain": false, "is_meta": false, "category": null, "secure_media_embed": {}, "link_flair_text": "Mercado editorial e pol\\u00edticas p\\u00fablicas", "can_mod_post": false, "score": 1, "approved_by": null, "is_created_from_ads_ui": false, "author_premium": false, "thumbnail": "self", "edited": false, "author_flair_css_class": null, "author_flair_richtext": [], "gildings": {}, "content_categories": null, "is_self": true, "mod_note": null, "created": 1647879710.0, "link_flair_type": "text", "wls": null, "removed_by_category": null, "banned_by": null, "author_flair_type": "text", "domain": "self.Livros", "allow_live_comments": false, "selftext_html": "&lt;!-- SC_OFF --&gt;&lt;div class=\\"md\\"&gt;&lt;p&gt;Ol\\u00e1 amigos do Reddit; &lt;/p&gt;\\n\\n&lt;p&gt;&amp;#x200B;&lt;/p&gt;\\n\\n&lt;p&gt;Gostaria de vir compartilhar um pensamento que venho tendo nessas \\u00faltimas semanas. &lt;/p&gt;\\n\\n&lt;p&gt;\\u201cO incentivo \\u00e0 leitura nunca foi t\\u00e3o importante em compara\\u00e7\\u00e3o as d\\u00e9cadas anteriores.\\u201d&lt;/p&gt;\\n\\n&lt;p&gt;Nunca foi t\\u00e3o dif\\u00edcil ser brasileiro: infla\\u00e7\\u00e3o que supera 2 d\\u00edgitos, governo federal que n\\u00e3o liga pra educa\\u00e7\\u00e3o da popula\\u00e7\\u00e3o e alto n\\u00edvel de desemprego. &lt;/p&gt;\\n\\n&lt;p&gt;Diante desse cen\\u00e1rio preocupante, digo que tenho muito orgulho do meu trabalho, exercendo ele vejo uma mudan\\u00e7a real em como a popula\\u00e7\\u00e3o est\\u00e1 cada vez mais interessada e curiosa na busca de desenvolvimento pessoal. Vejo significado e prop\\u00f3sito na minha vida exercendo minha profiss\\u00e3o. Espalho conhecimento por um pre\\u00e7o bastante acess\\u00edvel em compara\\u00e7\\u00e3o a outras livrarias. &lt;/p&gt;\\n\\n&lt;p&gt;Al\\u00e9m disso, voc\\u00eas me ajudam muito quando compram um livro. A cada dia estou mais perto da quantia necess\\u00e1ria para come\\u00e7ar meu mestrado em Coimbra. &lt;/p&gt;\\n\\n&lt;p&gt;Obrigados a todos que v\\u00eam me apoiando e que seguem minha jornada.&lt;/p&gt;\\n\\n&lt;p&gt;&amp;#x200B;&lt;/p&gt;\\n\\n&lt;p&gt;Grande abra\\u00e7o a todos.&lt;/p&gt;\\n&lt;/div&gt;&lt;!-- SC_ON --&gt;", "likes": null, "suggested_sort": "confidence", "banned_at_utc": null, "view_count": null, "archived": false, "no_follow": true, "is_crosspostable": false, "pinned": false, "over_18": false, "all_awardings": [], "awarders": [], "media_only": false, "link_flair_template_id": "6bfc7288-b343-11ea-99c8-0e35844b0e2f", "can_gild": false, "spoiler": false, "locked": false, "author_flair_text": null, "treatment_tags": [], "visited": false, "removed_by": null, "num_reports": null, "distinguished": null, "subreddit_id": "t5_2tlr4", "author_is_blocked": false, "mod_reason_by": null, "removal_reason": null, "link_flair_background_color": "#6b6031", "id": "tjflyd", "is_robot_indexable": true, "report_reasons": null, "discussion_type": null, "num_comments": 0, "send_replies": true, "whitelist_status": null, "contest_mode": false, "mod_reports": [], "author_patreon_flair": false, "author_flair_text_color": null, "permalink": "/r/Livros/comments/tjflyd/vender_livros_\\u00e9_um_dos_trabalho_mais/", "parent_whitelist_status": null, "stickied": false, "subreddit_subscribers": 12094, "created_utc": 1647879710.0, "num_crossposts": 0, "media": null, "is_video": false}}]}}
            """)
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
                    self.log_info(post)
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

class DemandService(BusinessService):
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
           
            # data = response.json()
            data = json.loads("""
                {"data":{"children":[{"kind": "t3", "data": {"approved_at_utc": null, "subreddit": "Livros", "author_fullname": "t2_1g037lor", "saved": false, "mod_reason_title": null, "gilded": 0, "clicked": false, "title": "VENDER LIVROS \\u00c9 UM DOS TRABALHO MAIS SIGNIFICANTES EM UMA \\u00c9POCA DE OBSCURANTISMO.", "link_flair_richtext": [], "subreddit_name_prefixed": "r/Livros", "hidden": false, "pwls": null, "link_flair_css_class": "", "downs": 0, "thumbnail_height": null, "top_awarded_type": null, "hide_score": true, "name": "t3_tjflyd", "quarantine": false, "link_flair_text_color": "light", "upvote_ratio": 1.0, "author_flair_background_color": null, "subreddit_type": "public", "ups": 1, "total_awards_received": 0, "media_embed": {}, "thumbnail_width": null, "author_flair_template_id": null, "is_original_content": false, "user_reports": [], "secure_media": null, "is_reddit_media_domain": false, "is_meta": false, "category": null, "secure_media_embed": {}, "link_flair_text": "Mercado editorial e pol\\u00edticas p\\u00fablicas", "can_mod_post": false, "score": 1, "approved_by": null, "is_created_from_ads_ui": false, "author_premium": false, "thumbnail": "self", "edited": false, "author_flair_css_class": null, "author_flair_richtext": [], "gildings": {}, "content_categories": null, "is_self": true, "mod_note": null, "created": 1647879710.0, "link_flair_type": "text", "wls": null, "removed_by_category": null, "banned_by": null, "author_flair_type": "text", "domain": "self.Livros", "allow_live_comments": false, "selftext_html": "&lt;!-- SC_OFF --&gt;&lt;div class=\\"md\\"&gt;&lt;p&gt;Ol\\u00e1 amigos do Reddit; &lt;/p&gt;\\n\\n&lt;p&gt;&amp;#x200B;&lt;/p&gt;\\n\\n&lt;p&gt;Gostaria de vir compartilhar um pensamento que venho tendo nessas \\u00faltimas semanas. &lt;/p&gt;\\n\\n&lt;p&gt;\\u201cO incentivo \\u00e0 leitura nunca foi t\\u00e3o importante em compara\\u00e7\\u00e3o as d\\u00e9cadas anteriores.\\u201d&lt;/p&gt;\\n\\n&lt;p&gt;Nunca foi t\\u00e3o dif\\u00edcil ser brasileiro: infla\\u00e7\\u00e3o que supera 2 d\\u00edgitos, governo federal que n\\u00e3o liga pra educa\\u00e7\\u00e3o da popula\\u00e7\\u00e3o e alto n\\u00edvel de desemprego. &lt;/p&gt;\\n\\n&lt;p&gt;Diante desse cen\\u00e1rio preocupante, digo que tenho muito orgulho do meu trabalho, exercendo ele vejo uma mudan\\u00e7a real em como a popula\\u00e7\\u00e3o est\\u00e1 cada vez mais interessada e curiosa na busca de desenvolvimento pessoal. Vejo significado e prop\\u00f3sito na minha vida exercendo minha profiss\\u00e3o. Espalho conhecimento por um pre\\u00e7o bastante acess\\u00edvel em compara\\u00e7\\u00e3o a outras livrarias. &lt;/p&gt;\\n\\n&lt;p&gt;Al\\u00e9m disso, voc\\u00eas me ajudam muito quando compram um livro. A cada dia estou mais perto da quantia necess\\u00e1ria para come\\u00e7ar meu mestrado em Coimbra. &lt;/p&gt;\\n\\n&lt;p&gt;Obrigados a todos que v\\u00eam me apoiando e que seguem minha jornada.&lt;/p&gt;\\n\\n&lt;p&gt;&amp;#x200B;&lt;/p&gt;\\n\\n&lt;p&gt;Grande abra\\u00e7o a todos.&lt;/p&gt;\\n&lt;/div&gt;&lt;!-- SC_ON --&gt;", "likes": null, "suggested_sort": "confidence", "banned_at_utc": null, "view_count": null, "archived": false, "no_follow": true, "is_crosspostable": false, "pinned": false, "over_18": false, "all_awardings": [], "awarders": [], "media_only": false, "link_flair_template_id": "6bfc7288-b343-11ea-99c8-0e35844b0e2f", "can_gild": false, "spoiler": false, "locked": false, "author_flair_text": null, "treatment_tags": [], "visited": false, "removed_by": null, "num_reports": null, "distinguished": null, "subreddit_id": "t5_2tlr4", "author_is_blocked": false, "mod_reason_by": null, "removal_reason": null, "link_flair_background_color": "#6b6031", "id": "tjflyd", "is_robot_indexable": true, "report_reasons": null, "discussion_type": null, "num_comments": 0, "send_replies": true, "whitelist_status": null, "contest_mode": false, "mod_reports": [], "author_patreon_flair": false, "author_flair_text_color": null, "permalink": "/r/Livros/comments/tjflyd/vender_livros_\\u00e9_um_dos_trabalho_mais/", "parent_whitelist_status": null, "stickied": false, "subreddit_subscribers": 12094, "created_utc": 1647879710.0, "num_crossposts": 0, "media": null, "is_video": false}}]}}
            """)
            updateLast = 0

            iso = isodata.get_iso('caiso')
            caiso = iso()
            dataa = caiso.get_demand_today().to_json()

            for key, value in enumerate(data['data']['children']):
                              
                post = PostClass.from_dict(value['data'])
                post.fuel_mix = dataa
                post.title="Cat"
              
                if not updateLast:
                    self.last_post_name = value['data']['name']
                    updateLast = 1
                    self.log_info(post)
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

class SupplyService(BusinessService):
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
           
            # data = response.json()
            data = json.loads("""
                {"data":{"children":[{"kind": "t3", "data": {"approved_at_utc": null, "subreddit": "Livros", "author_fullname": "t2_1g037lor", "saved": false, "mod_reason_title": null, "gilded": 0, "clicked": false, "title": "VENDER LIVROS \\u00c9 UM DOS TRABALHO MAIS SIGNIFICANTES EM UMA \\u00c9POCA DE OBSCURANTISMO.", "link_flair_richtext": [], "subreddit_name_prefixed": "r/Livros", "hidden": false, "pwls": null, "link_flair_css_class": "", "downs": 0, "thumbnail_height": null, "top_awarded_type": null, "hide_score": true, "name": "t3_tjflyd", "quarantine": false, "link_flair_text_color": "light", "upvote_ratio": 1.0, "author_flair_background_color": null, "subreddit_type": "public", "ups": 1, "total_awards_received": 0, "media_embed": {}, "thumbnail_width": null, "author_flair_template_id": null, "is_original_content": false, "user_reports": [], "secure_media": null, "is_reddit_media_domain": false, "is_meta": false, "category": null, "secure_media_embed": {}, "link_flair_text": "Mercado editorial e pol\\u00edticas p\\u00fablicas", "can_mod_post": false, "score": 1, "approved_by": null, "is_created_from_ads_ui": false, "author_premium": false, "thumbnail": "self", "edited": false, "author_flair_css_class": null, "author_flair_richtext": [], "gildings": {}, "content_categories": null, "is_self": true, "mod_note": null, "created": 1647879710.0, "link_flair_type": "text", "wls": null, "removed_by_category": null, "banned_by": null, "author_flair_type": "text", "domain": "self.Livros", "allow_live_comments": false, "selftext_html": "&lt;!-- SC_OFF --&gt;&lt;div class=\\"md\\"&gt;&lt;p&gt;Ol\\u00e1 amigos do Reddit; &lt;/p&gt;\\n\\n&lt;p&gt;&amp;#x200B;&lt;/p&gt;\\n\\n&lt;p&gt;Gostaria de vir compartilhar um pensamento que venho tendo nessas \\u00faltimas semanas. &lt;/p&gt;\\n\\n&lt;p&gt;\\u201cO incentivo \\u00e0 leitura nunca foi t\\u00e3o importante em compara\\u00e7\\u00e3o as d\\u00e9cadas anteriores.\\u201d&lt;/p&gt;\\n\\n&lt;p&gt;Nunca foi t\\u00e3o dif\\u00edcil ser brasileiro: infla\\u00e7\\u00e3o que supera 2 d\\u00edgitos, governo federal que n\\u00e3o liga pra educa\\u00e7\\u00e3o da popula\\u00e7\\u00e3o e alto n\\u00edvel de desemprego. &lt;/p&gt;\\n\\n&lt;p&gt;Diante desse cen\\u00e1rio preocupante, digo que tenho muito orgulho do meu trabalho, exercendo ele vejo uma mudan\\u00e7a real em como a popula\\u00e7\\u00e3o est\\u00e1 cada vez mais interessada e curiosa na busca de desenvolvimento pessoal. Vejo significado e prop\\u00f3sito na minha vida exercendo minha profiss\\u00e3o. Espalho conhecimento por um pre\\u00e7o bastante acess\\u00edvel em compara\\u00e7\\u00e3o a outras livrarias. &lt;/p&gt;\\n\\n&lt;p&gt;Al\\u00e9m disso, voc\\u00eas me ajudam muito quando compram um livro. A cada dia estou mais perto da quantia necess\\u00e1ria para come\\u00e7ar meu mestrado em Coimbra. &lt;/p&gt;\\n\\n&lt;p&gt;Obrigados a todos que v\\u00eam me apoiando e que seguem minha jornada.&lt;/p&gt;\\n\\n&lt;p&gt;&amp;#x200B;&lt;/p&gt;\\n\\n&lt;p&gt;Grande abra\\u00e7o a todos.&lt;/p&gt;\\n&lt;/div&gt;&lt;!-- SC_ON --&gt;", "likes": null, "suggested_sort": "confidence", "banned_at_utc": null, "view_count": null, "archived": false, "no_follow": true, "is_crosspostable": false, "pinned": false, "over_18": false, "all_awardings": [], "awarders": [], "media_only": false, "link_flair_template_id": "6bfc7288-b343-11ea-99c8-0e35844b0e2f", "can_gild": false, "spoiler": false, "locked": false, "author_flair_text": null, "treatment_tags": [], "visited": false, "removed_by": null, "num_reports": null, "distinguished": null, "subreddit_id": "t5_2tlr4", "author_is_blocked": false, "mod_reason_by": null, "removal_reason": null, "link_flair_background_color": "#6b6031", "id": "tjflyd", "is_robot_indexable": true, "report_reasons": null, "discussion_type": null, "num_comments": 0, "send_replies": true, "whitelist_status": null, "contest_mode": false, "mod_reports": [], "author_patreon_flair": false, "author_flair_text_color": null, "permalink": "/r/Livros/comments/tjflyd/vender_livros_\\u00e9_um_dos_trabalho_mais/", "parent_whitelist_status": null, "stickied": false, "subreddit_subscribers": 12094, "created_utc": 1647879710.0, "num_crossposts": 0, "media": null, "is_video": false}}]}}
            """)
            updateLast = 0

            iso = isodata.get_iso('caiso')
            caiso = iso()
            dataa = caiso.get_demand_today().to_json()

            for key, value in enumerate(data['data']['children']):
                              
                post = PostClass.from_dict(value['data'])
                post.fuel_mix = dataa
                post.title="Cat"
              
                if not updateLast:
                    self.last_post_name = value['data']['name']
                    updateLast = 1
                    self.log_info(post)
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

class ForecastService(BusinessService):
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
           
            # data = response.json()
            data = json.loads("""
                {"data":{"children":[{"kind": "t3", "data": {"approved_at_utc": null, "subreddit": "Livros", "author_fullname": "t2_1g037lor", "saved": false, "mod_reason_title": null, "gilded": 0, "clicked": false, "title": "VENDER LIVROS \\u00c9 UM DOS TRABALHO MAIS SIGNIFICANTES EM UMA \\u00c9POCA DE OBSCURANTISMO.", "link_flair_richtext": [], "subreddit_name_prefixed": "r/Livros", "hidden": false, "pwls": null, "link_flair_css_class": "", "downs": 0, "thumbnail_height": null, "top_awarded_type": null, "hide_score": true, "name": "t3_tjflyd", "quarantine": false, "link_flair_text_color": "light", "upvote_ratio": 1.0, "author_flair_background_color": null, "subreddit_type": "public", "ups": 1, "total_awards_received": 0, "media_embed": {}, "thumbnail_width": null, "author_flair_template_id": null, "is_original_content": false, "user_reports": [], "secure_media": null, "is_reddit_media_domain": false, "is_meta": false, "category": null, "secure_media_embed": {}, "link_flair_text": "Mercado editorial e pol\\u00edticas p\\u00fablicas", "can_mod_post": false, "score": 1, "approved_by": null, "is_created_from_ads_ui": false, "author_premium": false, "thumbnail": "self", "edited": false, "author_flair_css_class": null, "author_flair_richtext": [], "gildings": {}, "content_categories": null, "is_self": true, "mod_note": null, "created": 1647879710.0, "link_flair_type": "text", "wls": null, "removed_by_category": null, "banned_by": null, "author_flair_type": "text", "domain": "self.Livros", "allow_live_comments": false, "selftext_html": "&lt;!-- SC_OFF --&gt;&lt;div class=\\"md\\"&gt;&lt;p&gt;Ol\\u00e1 amigos do Reddit; &lt;/p&gt;\\n\\n&lt;p&gt;&amp;#x200B;&lt;/p&gt;\\n\\n&lt;p&gt;Gostaria de vir compartilhar um pensamento que venho tendo nessas \\u00faltimas semanas. &lt;/p&gt;\\n\\n&lt;p&gt;\\u201cO incentivo \\u00e0 leitura nunca foi t\\u00e3o importante em compara\\u00e7\\u00e3o as d\\u00e9cadas anteriores.\\u201d&lt;/p&gt;\\n\\n&lt;p&gt;Nunca foi t\\u00e3o dif\\u00edcil ser brasileiro: infla\\u00e7\\u00e3o que supera 2 d\\u00edgitos, governo federal que n\\u00e3o liga pra educa\\u00e7\\u00e3o da popula\\u00e7\\u00e3o e alto n\\u00edvel de desemprego. &lt;/p&gt;\\n\\n&lt;p&gt;Diante desse cen\\u00e1rio preocupante, digo que tenho muito orgulho do meu trabalho, exercendo ele vejo uma mudan\\u00e7a real em como a popula\\u00e7\\u00e3o est\\u00e1 cada vez mais interessada e curiosa na busca de desenvolvimento pessoal. Vejo significado e prop\\u00f3sito na minha vida exercendo minha profiss\\u00e3o. Espalho conhecimento por um pre\\u00e7o bastante acess\\u00edvel em compara\\u00e7\\u00e3o a outras livrarias. &lt;/p&gt;\\n\\n&lt;p&gt;Al\\u00e9m disso, voc\\u00eas me ajudam muito quando compram um livro. A cada dia estou mais perto da quantia necess\\u00e1ria para come\\u00e7ar meu mestrado em Coimbra. &lt;/p&gt;\\n\\n&lt;p&gt;Obrigados a todos que v\\u00eam me apoiando e que seguem minha jornada.&lt;/p&gt;\\n\\n&lt;p&gt;&amp;#x200B;&lt;/p&gt;\\n\\n&lt;p&gt;Grande abra\\u00e7o a todos.&lt;/p&gt;\\n&lt;/div&gt;&lt;!-- SC_ON --&gt;", "likes": null, "suggested_sort": "confidence", "banned_at_utc": null, "view_count": null, "archived": false, "no_follow": true, "is_crosspostable": false, "pinned": false, "over_18": false, "all_awardings": [], "awarders": [], "media_only": false, "link_flair_template_id": "6bfc7288-b343-11ea-99c8-0e35844b0e2f", "can_gild": false, "spoiler": false, "locked": false, "author_flair_text": null, "treatment_tags": [], "visited": false, "removed_by": null, "num_reports": null, "distinguished": null, "subreddit_id": "t5_2tlr4", "author_is_blocked": false, "mod_reason_by": null, "removal_reason": null, "link_flair_background_color": "#6b6031", "id": "tjflyd", "is_robot_indexable": true, "report_reasons": null, "discussion_type": null, "num_comments": 0, "send_replies": true, "whitelist_status": null, "contest_mode": false, "mod_reports": [], "author_patreon_flair": false, "author_flair_text_color": null, "permalink": "/r/Livros/comments/tjflyd/vender_livros_\\u00e9_um_dos_trabalho_mais/", "parent_whitelist_status": null, "stickied": false, "subreddit_subscribers": 12094, "created_utc": 1647879710.0, "num_crossposts": 0, "media": null, "is_video": false}}]}}
            """)
            updateLast = 0

            iso = isodata.get_iso('caiso')
            caiso = iso()
            dataa = caiso.get_demand_today().to_json()

            for key, value in enumerate(data['data']['children']):
                              
                post = PostClass.from_dict(value['data'])
                post.fuel_mix = dataa
                post.title="California"
              
                if not updateLast:
                    self.last_post_name = value['data']['name']
                    updateLast = 1
                    self.log_info(post)
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