from gohighlevel_python_sdk_v1.ghlobjects.abstractobject import AbstractObject


class Agency(AbstractObject):
    def __init__(self, agency_token=None):
        assert agency_token != None, "Must Provide Agency Token"
        self.token = agency_token
        super().__init__()

    def get_locations(self):
        route = "locations/"
        method = "GET"
        query = self.api.make_request(
            token=self.token,
            route=route,
            method=method,
        )
        locations = []
        for location in query["locations"]:
            locations.append(AbstractObject.create_object(data=location, target_class=Location))
        return locations


class Location(AbstractObject):
    def __init__(self):
        super().__init__()

    def get_survey_submissions(self, params=None):
        route = "surveys/submissions"
        subs = []
        finished_iteration = False
        page = 1
        while not finished_iteration:
            params["page"] = page
            query = self.api.get(route=route, headers=self.api.construct_headers(token=self["apiKey"]), params=params)
            page += 1
            subs.extend(
                [AbstractObject.create_object(data=sub, target_class=Submission) for sub in query["submissions"]]
            )
            finished_iteration = query["meta"]["nextPage"] is None
        return subs

    def get_calendar_teams(self):
        route = "calendars/teams"
        calendars = []
        query = self.api.get(route=route, headers=self.api.construct_headers(token=self["apiKey"]))
        return query

    def get_calendar_services(self):
        route = "calendars/services"
        method = "GET"
        query = self.api.make_request(token=self["apiKey"], route=route, method=method)
        calendars = [AbstractObject.create_object(cal, target_class=Calendar) for cal in query["services"]]
        # manually inject api key
        for cals in calendars:
            cals["apiKey"] = self["apiKey"]
        return calendars

    def get_pipelines(self):
        route = "pipelines/"
        method = "GET"
        query = self.api.make_request(token=self["apiKey"], route=route, method=method)
        pipelines = [AbstractObject.create_object(pipe, target_class=Pipeline) for pipe in query["pipelines"]]
        # manually inject api key
        for pipe in pipelines:
            pipe["apiKey"] = self["apiKey"]
        return pipelines

    def get_contacts(self, limit=100):
        # 'meta': {'total': 13, 'nextPageUrl': 'http://rest.gohighlevel.com/v1/pipelines/MSPxOPSH9489lhzmvxaN/opportunities?startAfter=1674489239791&startAfterId=2IlGEHxT1wUG7q8axJnC', 'startAfterId': '2IlGEHxT1wUG7q8axJnC', 'startAfter': 1674489239791, 'currentPage': 1, 'nextPage': '', 'prevPage': None}
        contacts = []
        route = "contacts/"
        method = "GET"
        url_override = None
        while True:
            query = self.api.make_request(token=self["apiKey"], route=route, method=method, url_override=url_override)
            for opp in query["contacts"]:
                contacts.append(AbstractObject.create_object(data=opp, target_class=Contact))
            if query["meta"]["nextPage"] is None or len(query["contacts"]) == 0:
                break
            else:
                url_override = query["meta"]["nextPageUrl"]
        # manually inject token data
        for contact in contacts:
            contact["apiKey"] = self["apiKey"]
        return contacts


class Calendar(AbstractObject):
    def __init__(self):
        super().__init__()

    def get_appointments(self, params):
        if not all(["startDate" in params.keys(), "endDate" in params.keys()]):
            raise ValueError("Startdate and Enddate are required.")
        params["calendarId"] = self["id"]
        route = "appointments/"
        method = "GET"
        query = self.api.make_request(token=self["apiKey"], route=route, method=method, params=params)
        return [AbstractObject.create_object(appt, target_class=Appointments) for appt in query["appointments"]]


class Appointments(AbstractObject):
    def __init__(self):
        super().__init__()


class Submission(AbstractObject):
    def __init__(self):
        super().__init__()


class Contact(AbstractObject):
    def __init__(self):
        super().__init__()

    def get_appointment(self):
        route = "contacts/" + self["id"] + "/appointments/"
        method = "GET"
        query = self.api.make_request(token=self["apiKey"], route=route, method=method)
        print(query)
        return


class Opportunity(AbstractObject):
    def __init__(self):
        super().__init__()


class Pipeline(AbstractObject):
    def __init__(self):
        super().__init__()

    def get_opportunities(self):
        # 'meta': {'total': 13, 'nextPageUrl': 'http://rest.gohighlevel.com/v1/pipelines/MSPxOPSH9489lhzmvxaN/opportunities?startAfter=1674489239791&startAfterId=2IlGEHxT1wUG7q8axJnC', 'startAfterId': '2IlGEHxT1wUG7q8axJnC', 'startAfter': 1674489239791, 'currentPage': 1, 'nextPage': '', 'prevPage': None}
        opportunities = []
        route = "pipelines/" + self["id"] + "/opportunities"
        method = "GET"
        url_override = None
        while True:
            query = self.api.make_request(token=self["apiKey"], route=route, method=method, url_override=url_override)
            for opp in query["opportunities"]:
                opportunities.append(AbstractObject.create_object(data=opp, target_class=Opportunity))
            if query["meta"]["nextPage"] is None or len(query["opportunities"]) == 0:
                break
            else:
                url_override = query["meta"]["nextPageUrl"]
        # inject token data
        for ops in opportunities:
            ops["apiKey"] = self["apiKey"]
        return opportunities
