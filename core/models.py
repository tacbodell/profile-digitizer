class Pvi:
    def __init__(self, station, elevation):
        self.station = station
        self.elevation = elevation
    
    def pixel_to_station(self, pixel):
        pass

    def pixel_to_elevation(self, elevation):
        pass

    def get_report(self):
        return str(self.station) + "," + str(self.elevation) + "," + "0.000000,"