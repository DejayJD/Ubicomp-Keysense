import io, time, random, json
import config
from collections import namedtuple

SensorData = namedtuple("SensorData", "value time stressed")

data_file = open(config.FILE_NAME, "w")

test_data = {}
for sensor in config.SENSORS:
    test_data[sensor] = []

def generateRandomSensorData(data, sensors, stressed):
    for sensor in sensors:
        data[sensor].append(SensorData(random.randint(1,1000), time.time(), stressed))

def iterateRandomSensorData(iterations, sensors, data):
    start = time.time()
    i = 0
    while i < iterations:
        generateRandomSensorData(data, sensors, 0)
        i += 1
    end = time.time()
    sample_rate = iterations/(end-start)
    print "Finished with Sample Rate: " + str(sample_rate) + " values/second for " + str(len(sensors)) + " sensors"
    print "Iterations: " + str(iterations) + " seconds"
    print "Time Elapsed: " + str(end-start)

iterateRandomSensorData(1000000, config.SENSORS, test_data)

start = time.time()
if config.WRITE:
    json.dump(test_data, data_file)
end = time.time()

write_time = end-start
print "Write Time: " + str(write_time)