import rospy
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose
import os

def spawn_fruitlet():
    rospy.init_node('spawn_fruitlet_node')

    # Set GAZEBO_MODEL_PATH to your models directory
    os.environ['GAZEBO_MODEL_PATH'] = '/path/to/micebot_launch/models'

    # Load the model file (model.sdf)
    model_path = '/path/to/micebot_launch/models/fruitlet/model.sdf'
    with open(model_path, 'r') as model_file:
        model_xml = model_file.read()

    # Wait for the spawn model service to be available
    rospy.wait_for_service('/gazebo/spawn_sdf_model')
    try:
        spawn_model = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
        pose = Pose()
        # Optionally set position (x, y, z) and orientation (quaternion)
        pose.position.x = 0.5
        pose.position.y = 0
        pose.position.z = 1.0  # Height above ground

        # Spawn the model
        spawn_model('fruitlet', model_xml, '', pose, 'world')
        rospy.loginfo("Fruitlet spawned successfully!")
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

if __name__ == '__main__':
    spawn_fruitlet()