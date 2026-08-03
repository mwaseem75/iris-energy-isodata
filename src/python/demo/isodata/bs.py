from grongier.pex import BusinessService
import json
import requests
import gridstatus
from message import PostMessage
from obj import PostClass


def get_supply_from_fuel_mix(fuel_df):
    """Calculate total supply by summing numeric columns in fuel mix DataFrame."""
    numeric_cols = fuel_df.select_dtypes(include='number').columns
    return str(round(fuel_df[numeric_cols].iloc[0].sum(), 2))


def get_demand_from_load(load_df):
    """Get demand value from load DataFrame, finding the numeric column dynamically."""
    skip = ['Time', 'Interval Start', 'Interval End', 'interval_start', 'interval_end']
    numeric_cols = [c for c in load_df.columns if c not in skip and load_df[c].dtype in ['float64', 'int64']]
    col = numeric_cols[0] if numeric_cols else load_df.select_dtypes(include='number').columns[0]
    return str(round(load_df[col].iloc[0], 2))


class CaliforniaService(BusinessService):
    """
    This service use an Ens.InboundAdapter to, on_process_input every 5
    seconds, use gridstatus to fetch CAISO energy data before calling
    the FilterPostRoutingRule process.
    """
    def get_adapter_type():
        return "Ens.InboundAdapter"

    def on_init(self):
        if not hasattr(self, 'limit'):
            raise TypeError('no limit field')
        if not hasattr(self, 'target'):
            self.target = "Isodata.FilterRoutingRule"
        self.last_post_name = ""
        return 1

    def on_process_input(self, request):
        post = self.on_task()
        if post is not None:
            msg = PostMessage()
            msg.post = post
            self.send_request_sync(self.target, msg)

    def on_task(self) -> PostClass:
        try:
            data = json.loads("""{"data":{"children":[{"kind": "t3", "data": {"title": "", "name": "", "created_utc": 1647879710.0}}]}}""")
            updateLast = 0

            caiso = gridstatus.CAISO()
            fuel_df = caiso.get_fuel_mix(date="latest")
            getdata = str(fuel_df)
            demand = get_demand_from_load(caiso.get_load(date="latest"))
            supply = get_supply_from_fuel_mix(fuel_df)

            for key, value in enumerate(data['data']['children']):
                post = PostClass.from_dict(value['data'])
                post.fuel_mix = getdata
                post.title = "caiso"
                post.demand = demand + " NW"
                post.supply = supply + " NW"

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


class PjmService(BusinessService):
    """
    This service use an Ens.InboundAdapter to, on_process_input every 5
    seconds, use gridstatus to fetch PJM energy data before calling
    the FilterPostRoutingRule process.
    """
    def get_adapter_type():
        return "Ens.InboundAdapter"

    def on_init(self):
        if not hasattr(self, 'limit'):
            raise TypeError('no limit field')
        if not hasattr(self, 'target'):
            self.target = "Isodata.FilterRoutingRule"
        self.last_post_name = ""
        return 1

    def on_process_input(self, request):
        post = self.on_task()
        if post is not None:
            msg = PostMessage()
            msg.post = post
            self.send_request_sync(self.target, msg)

    def on_task(self) -> PostClass:
        try:
            data = json.loads("""{"data":{"children":[{"kind": "t3", "data": {"title": "", "name": "", "created_utc": 1647879710.0}}]}}""")
            updateLast = 0

            pjm = gridstatus.PJM()
            fuel_df = pjm.get_fuel_mix(date="latest")
            getdata = str(fuel_df)
            demand = get_demand_from_load(pjm.get_load(date="latest"))
            supply = get_supply_from_fuel_mix(fuel_df)

            for key, value in enumerate(data['data']['children']):
                post = PostClass.from_dict(value['data'])
                post.fuel_mix = getdata
                post.title = "pjm"
                post.demand = demand + " NW"
                post.supply = supply + " NW"

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


class IsoneService(BusinessService):
    """
    This service use an Ens.InboundAdapter to, on_process_input every 5
    seconds, use gridstatus to fetch ISONE energy data before calling
    the FilterPostRoutingRule process.
    """
    def get_adapter_type():
        return "Ens.InboundAdapter"

    def on_init(self):
        if not hasattr(self, 'limit'):
            raise TypeError('no limit field')
        if not hasattr(self, 'target'):
            self.target = "Isodata.FilterRoutingRule"
        self.last_post_name = ""
        return 1

    def on_process_input(self, request):
        post = self.on_task()
        if post is not None:
            msg = PostMessage()
            msg.post = post
            self.send_request_sync(self.target, msg)

    def on_task(self) -> PostClass:
        try:
            data = json.loads("""{"data":{"children":[{"kind": "t3", "data": {"title": "", "name": "", "created_utc": 1647879710.0}}]}}""")
            updateLast = 0

            isone = gridstatus.ISONE()
            fuel_df = isone.get_fuel_mix(date="latest")
            getdata = str(fuel_df)
            demand = get_demand_from_load(isone.get_load(date="latest"))
            supply = get_supply_from_fuel_mix(fuel_df)

            for key, value in enumerate(data['data']['children']):
                post = PostClass.from_dict(value['data'])
                post.fuel_mix = getdata
                post.title = "isone"
                post.demand = demand + " NW"
                post.supply = supply + " NW"

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