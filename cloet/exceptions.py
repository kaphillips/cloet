
class BoundsException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class ScenarioException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class RouteException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg