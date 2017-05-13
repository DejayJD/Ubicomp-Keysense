import io, time, random, json
import config
from collections import namedtuple

SensorData = namedtuple("SensorData", "value time stressed")

class DummyInputGenerator:

    def __init__(self, file_name, sensors):
        self.data_file = open(file_name, "w")

        #Initialize the dictionary data
        self.data = {}
        self.sensors = sensors
        for sensor in self.sensors:
            self.data[sensor] = []

    def generateRandomSensorData(self, stressed):
        for sensor in self.sensors:
            self.data[sensor].append(SensorData(random.randint(1,1000), time.time(), stressed))

    def iterateRandomSensorData(self, iterations, stressed, record_time=True):
        if (record_time):
            start = time.time()
        i = 0
        while i < iterations:
            self.generateRandomSensorData(stressed)
            i += 1
        end = time.time()
        sample_rate = iterations/(end-start)
        print "Finished with Sample Rate: " + str(sample_rate) + " values/second for " + str(len(self.sensors)) + " sensors"
        print "Iterations: " + str(iterations) + " seconds"
        print "Time Elapsed: " + str(end-start)

    def outputSensorData(self, record_time=True):

        if (record_time):
            start = time.time()
        #dump data to a json file
        json.dump(self.data, self.data_file)

        if (record_time):
            end = time.time()
            write_time = end-start
            print "Write Time: " + str(write_time)

generator = DummyInputGenerator(config.FILE_NAME, config.SENSORS)
generator.iterateRandomSensorData(1000, 0)
generator.outputSensorData()