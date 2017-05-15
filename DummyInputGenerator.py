import io, time, random, json
import config
import numpy as np
from collections import namedtuple
from tempfile import TemporaryFile

SensorData = namedtuple("SensorData", "value time stressed")

class DummyInputGenerator:

    def __init__(self, file_name, sensors):
        self.file_name = file_name
        #Initialize the dictionary data
        self.data_dict = {}
        self.data_np = []
        self.target_np = []
        self.sensors = sensors
        for sensor in self.sensors:
            self.data_dict[sensor] = []

    def generateJsonData(self, min, max):
        for sensor in self.sensors:
            self.data_dict[sensor].append(SensorData(random.randint(min, max), time.time(), self.stressed))

    def generateNumpyData(self, min, max):

        randomVals = []
        for i in range(len(self.sensors)):
            randomVals.append(random.randint(min, max))
        self.data_np.append(randomVals)
        self.target_np.append(self.stressed)

    def iterateRandomSensorData(self, iterations, stressed, min, max, data_type, record_time=True):
        self.stressed=stressed
        if (record_time):
            start = time.time()


        for i in range(iterations):
            if (data_type == "json"):
                self.generateJsonData(min, max)
            elif (data_type == "np"):
                self.generateNumpyData(min, max)

        self.data_np = np.array(self.data_np)

        if (record_time):
            end = time.time()
            sample_rate = iterations/(end-start)
            print "Finished with Sample Rate: " + str(sample_rate) + " values/second for " + str(len(self.sensors)) + " sensors"
            print "Iterations: " + str(iterations) + " seconds"
            print "Time Elapsed: " + str(end-start)

    def outputJsonData(self, record_time=True):
        self.data_file = open(self.file_name, "w")
        if (record_time):
            start = time.time()
        #dump data to a json file
        json.dump(self.data_dict, self.data_file)

        if (record_time):
            end = time.time()
            write_time = end-start
            print "Write Time: " + str(write_time)

    def outputNumpyData(self, record_time=True):
        print self.data_np
        np.save(self.file_name + ".npy", self.data_np)

filename = "unstressed_data"
generator = DummyInputGenerator(filename, config.SENSORS)
generator.iterateRandomSensorData(10000, 0, 0, 800, "np")
generator.outputNumpyData()