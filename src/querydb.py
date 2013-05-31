
import roslib
roslib.load_manifest('mongo_query_msgs')


import rospy
import pymongo
from turtlesim.msg import Velocity



class QClient():
    """ Mongodb querying client
    """

    def __init__(self, host, port, pool_size):
        """initialize the query client """
        self.mongo_client = pymongo.MongoClient(host, port, max_pool_size=pool_size)
        rospy.loginfo('client connection status', self.mongo_client.alive())


    def query_service_callback(self, query):
        """callback to handle querries"""
        if query.topic == '~/command_velocity':
            mq = self.mongo_client.find({"time": {$gte: query.start, $lte: query.stop}})
            print mq # for debug




def main():
    """entry to the main program"""
    pass

if __name__ == '__main__':
    main()
    rospy.spin()
