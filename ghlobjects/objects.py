from GoHighLevelSDK.ghlobjects.abstractobject import AbstractObject


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
        token = self["apiKey"]
        subs = []
        finished_iteration = False
        page = 1
        while not finished_iteration:
            params["page"] = page
            query = self.api.get(route=route, headers=self.api.construct_headers(token=token), params=params)
            page += 1
            subs.extend(
                [AbstractObject.create_object(data=sub, target_class=Submission) for sub in query["submissions"]]
            )
            finished_iteration = query["meta"]["nextPage"] is None
        return subs


class Appointments(AbstractObject):
    def __init__(self):
        super().__init__()


class Submission(AbstractObject):
    def __init__(self):
        super().__init__()
