  
# BSD 2-Clause License
#
# Copyright (c) 2022, Social Cognition in Human-Robot Interaction,
#                     Istituto Italiano di Tecnologia, Genova
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from pyicub.helper import iCub, JointPose, JointsTrajectoryCheckpoint, LimbMotion, ICUB_PARTS, iCubFullbodyAction, iCubFullbodyStep

def my_action():
    action = iCubFullbodyAction()

    pose_up   = JointPose(target_joints=[-65.00], joints_list=[0])
    pose_down = JointPose(target_joints=[-30.00], joints_list=[0])
    
    up   = JointsTrajectoryCheckpoint(pose_up  )
    down = JointsTrajectoryCheckpoint(pose_down)
    
    mLX = LimbMotion(ICUB_PARTS.LEFT_ARM)
    mLX.addCheckpoint(up)
    mLX.addCheckpoint(down)
    
    step1 = iCubFullbodyStep()
    
    step1.setLimbMotion(mLX)

    action.addStep(step1)
    

    return action

icub = iCub()

action = my_action()
icub.play(action)
action.exportJSONFile('json/upLeft.json')
