# Simple BSN Network based on ROS
Simple Behavior Selection Network

## Usage
* rosparam initiation & running handler node
```
roslaunch simple_bsn bringup_simple_bsn.launch
```
* rosparam initiation and then running handler node
```
roslaunch simple_bsn bringup_only_param.launch
rosrun simple_bsn bsn_handler.py
```
## Configuration
simple_bsn/config/condition.yaml 

* ref.
```
# condition server of BSN

pre_condition :
  A_on_B : 0
  B_on_C : 0
  A_on_C : 1
  clear_A : 1
  clear_B : 0
  clear_C : 0

goal :
  A_on_B : 0
  B_on_C : 0

behavior_condition :
#  take_A_from_B : [A_on_B, clear_A]
#  take_B_from_C : [B_on_C, clear_B]
  take_A_from_C : [A_on_C, clear_A]
  stack_A_on_B : [clear_A, clear_B]
  stack_B_on_C : [clear_B, clear_C]
#  stack_A_on_C : [clear_A, clear_C]

behavior_rule :
#  take_A_from_B :
#    add_list : []
#    delete_list : []
#  take_B_from_C : 0
#    add_list : []
#    delete_list : []
  take_A_from_C :
    add_list : [clear_C]
    delete_list : [A_on_C]
  stack_A_on_B :
    add_list : [clear_C, A_on_B]
    delete_list : [A_on_C, clear_B]
  stack_B_on_C :
    add_list : [B_on_C, clear_A]
    delete_list : [B_on_A, clear_C]
#  stack_A_on_C :
#    add_list : []
#    delete_list : []
```