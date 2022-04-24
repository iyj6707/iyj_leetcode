class UndergroundSystem:

    arrival_times = defaultdict(lambda: defaultdict(list))
    customer_info = defaultdict(tuple)
    
    def __init__(self):
        pass

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer_info[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        departure, departure_time = self.customer_info[id]
        self.arrival_times[departure][stationName].append(t - departure_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        average_times = self.arrival_times[startStation][endStation]
        return sum(average_times) / len(average_times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)