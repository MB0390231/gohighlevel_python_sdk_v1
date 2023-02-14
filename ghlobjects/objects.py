from gohighlevel_python_sdk.ghlobjects.abstractobject import AbstractObject


class Agency(AbstractObject):
    def __init__(self, agency_token=None):
        assert agency_token != None, "Must Provide Agency Token"
        self.token = agency_token
        super().__init__()

    def get_locations(self):
        route = "locations/"
        query = self.api.get(route=route, headers=self.api.construct_headers(self.token))
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
        calenders = []
        query = self.api.get(route=route, headers=self.api.construct_headers(token=self["apiKey"]))
        return query

    def get_calendar_services(self):
        route = "calendars/services"
        query = self.api.get(route=route, headers=self.api.construct_headers(token=self["apiKey"]))
        calendars = [AbstractObject.create_object(cal, target_class=Calender) for cal in query["services"]]
        # manually inject api key
        for cals in calendars:
            cals["apiKey"] = self["apiKey"]
        return calendars


class Calender(AbstractObject):
    def __init__(self):
        super().__init__()

    def get_appointments(self, params):
        if not all(["startDate" in params.keys(), "endDate" in params.keys()]):
            raise ValueError("Startdate and Enddate are required.")
        params["calendarId"] = self["id"]
        route = "appointments/"
        query = self.api.get(route=route, headers=self.api.construct_headers(token=self["apiKey"]), params=params)
        return [AbstractObject.create_object(appt, target_class=Appointments) for appt in query["appointments"]]


class Appointments(AbstractObject):
    def __init__(self):
        super().__init__()


class Submission(AbstractObject):
    def __init__(self):
        super().__init__()
