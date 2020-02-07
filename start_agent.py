from __future__ import print_function
from __future__ import division
# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

# Tutorial sample #3: Drawing

from builtins import range
from past.utils import old_div
import MalmoPython
import os
import sys
import time

if sys.version_info[0] == 2:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)  # flush print output immediately
else:
    import functools
    print = functools.partial(print, flush=True)

def Menger(xorg, yorg, zorg, size, blocktype, holetype):
    #draw solid chunk
    genstring = GenCuboid(xorg,yorg,zorg,xorg+size-1,yorg+size-1,zorg+size-1,blocktype) + "\n"
    #now remove holes
    unit = size
    while (unit >= 3):
        w=old_div(unit,3)
        for i in range(0, size, unit):
            for j in range(0, size, unit):
                x=xorg+i
                y=yorg+j
                genstring += GenCuboid(x+w,y+w,zorg,(x+2*w)-1,(y+2*w)-1,zorg+size-1,holetype) + "\n"
                y=yorg+i
                z=zorg+j
                genstring += GenCuboid(xorg,y+w,z+w,xorg+size-1, (y+2*w)-1,(z+2*w)-1,holetype) + "\n"
                genstring += GenCuboid(x+w,yorg,z+w,(x+2*w)-1,yorg+size-1,(z+2*w)-1,holetype) + "\n"
        unit = w
    return genstring

def GenCuboid(x1, y1, z1, x2, y2, z2, blocktype):
    return '<DrawCuboid x1="' + str(x1) + '" y1="' + str(y1) + '" z1="' + str(z1) + '" x2="' + str(x2) + '" y2="' + str(y2) + '" z2="' + str(z2) + '" type="' + blocktype + '"/>'
    
missionXML='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
              <About>
                <Summary>Hello world!</Summary>
              </About>
              
            <ServerSection>
              <ServerInitialConditions>
                <Time>
                    <StartTime>12000</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                </Time>
                <Weather>clear</Weather>
              </ServerInitialConditions>
              <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;7,44*49,73,35:1,159:4,95:13,35:13,159:11,95:10,159:14,159:6,35:6,95:6;12;"/>
                  <ServerQuitFromTimeUp timeLimitMs="60000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Survival">
                <Name>MalmoTutorialBot</Name>
                <AgentStart>
                    <Placement x="0.5" y="56.0" z="0.5" yaw="180"/>
					<Inventory>
						<InventoryItem slot="0" type="diamond_pickaxe"/>
                        <InventoryBlock slot="1" type="end_portal_frame" quantity="64"/>
                        <InventoryItem slot="2" type="ender_eye" quantity="64"/>
                        <InventoryItem slot="3" type="ender_pearl" quantity="64"/>
					</Inventory>
                </AgentStart>
                <AgentHandlers>
                  <ObservationFromFullStats/>
                  <AbsoluteMovementCommands/>
                  <ContinuousMovementCommands turnSpeedDegs="180">
                    <ModifierList type="allow-list">
                        <command>use</command>
                    </ModifierList>
                  </ContinuousMovementCommands>
                  <DiscreteMovementCommands/>
                  <InventoryCommands/>
                  <ChatCommands/>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

'''
<DrawingDecorator>
    <DrawBlock x="0" y="9" z="1" type="end_portal_frame"/>
    <DrawBlock x="0" y="9" z="2" type="end_portal_frame"/>
    <DrawBlock x="0" y="9" z="3" type="end_portal_frame"/>
</DrawingDecorator>
'''
# missionXML='''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
#             <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            
#               <About>
#                 <Summary>Hello world!</Summary>
#               </About>
              
#             <ServerSection>
#               <ServerInitialConditions>
#                 <Time>
#                     <StartTime>12000</StartTime>
#                     <AllowPassageOfTime>false</AllowPassageOfTime>
#                 </Time>
#                 <Weather>clear</Weather>
#               </ServerInitialConditions>
#               <ServerHandlers>
#                     <FlatWorldGenerator generatorString="3;1*minecraft:bedrock,7*minecraft:dirt,1*minecraft:grass;9;"/>
#                     <ServerQuitFromTimeUp timeLimitMs="300000"/>
#                     <ServerQuitWhenAnyAgentFinishes/>
#                 </ServerHandlers>
#               </ServerSection>
              
#               <AgentSection mode="Survival">
#                 <Name>MalmoTutorialBot</Name>
#                 <AgentStart>
#                     <Placement x="0.5" y="9" z="0.5" yaw="180"/>
# 					<Inventory>
# 						<InventoryItem slot="0" type="diamond_pickaxe"/>
#                         <InventoryBlock slot="1" type="end_portal_frame" quantity="64"/>
#                         <InventoryItem slot="2" type="ender_eye" quantity="64"/>
#                         <InventoryItem slot="3" type="ender_pearl" quantity="64"/>
# 					</Inventory>
#                 </AgentStart>
#                 <AgentHandlers>
#                   <ObservationFromFullStats/>
#                   <ContinuousMovementCommands turnSpeedDegs="180">
#                     <ModifierList type="deny-list">
#                         <command>move</command>
#                         <command>pitch</command>
#                     </ModifierList>
#                   </ContinuousMovementCommands>
#                   <DiscreteMovementCommands>
#                     <ModifierList type="allow-list">
#                         <command>movenorth</command>
#                     </ModifierList>
#                     <ModifierList type="deny-list">
#                         <command>look</command>
#                     </ModifierList>
#                   </DiscreteMovementCommands>
#                   <AbsoluteMovementCommands/>
#                   <InventoryCommands/>
#                 </AgentHandlers>
#               </AgentSection>
#             </Mission>'''

# Create default Malmo objects:

def place(agent_host, num = 0.15):
    agent_host.sendCommand('use 1')
    time.sleep(num)
    agent_host.sendCommand('use 0')

def move_left(agent_host, num = 0.15):
    agent_host.sendCommand('strafe -1')
    time.sleep(num)
    agent_host.sendCommand('strafe 0')

def move_right(agent_host, num = 0.15):
    agent_host.sendCommand('strafe 1')
    time.sleep(num)
    agent_host.sendCommand('strafe 0')

def turn_left(agent_host, num = 0.5):
    agent_host.sendCommand('turn -1')
    time.sleep(num)
    agent_host.sendCommand('turn 0')

def turn_right(agent_host, num = 0.5):
    agent_host.sendCommand('turn 1')
    time.sleep(num)
    agent_host.sendCommand('turn 0')

agent_host = MalmoPython.AgentHost()
try:
    agent_host.parse( sys.argv )
except RuntimeError as e:
    print('ERROR:',e)
    print(agent_host.getUsage())
    exit(1)
if agent_host.receivedArgument("help"):
    print(agent_host.getUsage())
    exit(0)

my_mission = MalmoPython.MissionSpec(missionXML, True)
my_mission_record = MalmoPython.MissionRecordSpec()

# Attempt to start a mission:
max_retries = 3
for retry in range(max_retries):
    try:
        agent_host.startMission( my_mission, my_mission_record )
        break
    except RuntimeError as e:
        if retry == max_retries - 1:
            print("Error starting mission:",e)
            exit(1)
        else:
            time.sleep(2)

# Loop until mission starts:
print("Waiting for the mission to start ", end=' ')
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)

print()
print("Mission running ", end=' ')

time.sleep(4)

# for i in range(10):

#     agent_host.sendCommand('discardCurrentItem 4')
#     time.sleep(1)
#     agent_host.sendCommand('use 1')
#     time.sleep(0.2)

#     agent_host.sendCommand('chat Thrown a pearl?')
#     time.sleep(0.5)

#     agent_host.sendCommand('use 0')
#     time.sleep(0.2)

#Look down to look at the ground
agent_host.sendCommand('setPitch 50')
time.sleep(0.5)

#Select ender box
agent_host.sendCommand('hotbar.2 1')
agent_host.sendCommand('hotbar.2 0')
time.sleep(0.5)

agent_host.sendCommand('use 1')
agent_host.sendCommand('use 0')
time.sleep(0.1)

#Select ender eye
agent_host.sendCommand('hotbar.3 1')
agent_host.sendCommand('hotbar.3 0')
time.sleep(1)

agent_host.sendCommand('use 1')
time.sleep(0.1)

agent_host.sendCommand('use 0')
time.sleep(0.2)

for i in range(2):
    agent_host.sendCommand('movewest 1')
    time.sleep(0.1)

    #Select ender box
    agent_host.sendCommand('hotbar.2 1')
    agent_host.sendCommand('hotbar.2 0')
    time.sleep(0.1)

    agent_host.sendCommand('use 1')
    agent_host.sendCommand('use 0')
    time.sleep(0.1)

    #Select ender eye
    agent_host.sendCommand('hotbar.3 1')
    agent_host.sendCommand('hotbar.3 0')
    time.sleep(0.1)

    agent_host.sendCommand('use 1')
    agent_host.sendCommand('use 0')
    time.sleep(0.1)

#-----------------------------------------------------------
agent_host.sendCommand('setYaw 90')
time.sleep(0.2)

#Select ender box
agent_host.sendCommand('hotbar.2 1')
agent_host.sendCommand('hotbar.2 0')

agent_host.sendCommand('use 1')
agent_host.sendCommand('use 0')
time.sleep(0.1)

#Select ender eye
agent_host.sendCommand('hotbar.3 1')
agent_host.sendCommand('hotbar.3 0')
time.sleep(0.1)

agent_host.sendCommand('use 1')
agent_host.sendCommand('use 0')
time.sleep(0.1)


for i in range(2):
    agent_host.sendCommand('movesouth 1')
    time.sleep(0.1)

    #Select ender box
    agent_host.sendCommand('hotbar.2 1')
    agent_host.sendCommand('hotbar.2 0')
    time.sleep(0.1)

    agent_host.sendCommand('use 1')
    agent_host.sendCommand('use 0')
    time.sleep(0.1)

    #Select ender eye
    agent_host.sendCommand('hotbar.3 1')
    agent_host.sendCommand('hotbar.3 0')
    time.sleep(0.1)

    agent_host.sendCommand('use 1')
    agent_host.sendCommand('use 0')
    time.sleep(0.1)

#-----------------------------------------------------------
agent_host.sendCommand('setYaw 0')
time.sleep(0.2)

#Select ender box
agent_host.sendCommand('hotbar.2 1')
agent_host.sendCommand('hotbar.2 0')

agent_host.sendCommand('use 1')
agent_host.sendCommand('use 0')
time.sleep(0.1)

#Select ender eye
agent_host.sendCommand('hotbar.3 1')
agent_host.sendCommand('hotbar.3 0')
time.sleep(0.1)

agent_host.sendCommand('use 1')
agent_host.sendCommand('use 0')
time.sleep(0.1)

for i in range(2):
    agent_host.sendCommand('moveeast 1')
    time.sleep(0.1)

    #Select ender box
    agent_host.sendCommand('hotbar.2 1')
    agent_host.sendCommand('hotbar.2 0')
    time.sleep(0.1)

    agent_host.sendCommand('use 1')
    agent_host.sendCommand('use 0')
    time.sleep(0.1)

    #Select ender eye
    agent_host.sendCommand('hotbar.3 1')
    agent_host.sendCommand('hotbar.3 0')
    time.sleep(0.1)

    agent_host.sendCommand('use 1')
    agent_host.sendCommand('use 0')
    time.sleep(0.1)

#-----------------------------------------------------------
agent_host.sendCommand('setYaw -90')
time.sleep(0.2)

#Select ender box
agent_host.sendCommand('hotbar.2 1')
agent_host.sendCommand('hotbar.2 0')

agent_host.sendCommand('use 1')
agent_host.sendCommand('use 0')
time.sleep(0.1)

#Select ender eye
agent_host.sendCommand('hotbar.3 1')
agent_host.sendCommand('hotbar.3 0')
time.sleep(0.1)

agent_host.sendCommand('use 1')
agent_host.sendCommand('use 0')
time.sleep(0.1)

for i in range(2):
    agent_host.sendCommand('movenorth 1')
    time.sleep(0.1)

    #Select ender box
    agent_host.sendCommand('hotbar.2 1')
    agent_host.sendCommand('hotbar.2 0')
    time.sleep(0.1)

    agent_host.sendCommand('use 1')
    agent_host.sendCommand('use 0')
    time.sleep(0.1)

    #Select ender eye
    agent_host.sendCommand('hotbar.3 1')
    agent_host.sendCommand('hotbar.3 0')
    time.sleep(0.1)

    agent_host.sendCommand('use 1')
    agent_host.sendCommand('use 0')
    time.sleep(0.1)

time.sleep(5)

agent_host.sendCommand('setYaw 68')
time.sleep(0.1)
agent_host.sendCommand('setPitch -47')

agent_host.sendCommand('hotbar.4 1')
agent_host.sendCommand('hotbar.4 0')
time.sleep(0.1)

agent_host.sendCommand('use 1')
time.sleep(0.1)

agent_host.sendCommand('use 0')
time.sleep(0.1)

agent_host.sendCommand('chat WOOHOOOOOOOOOO')


# print('LAMO')

# Loop until mission ends:
while world_state.is_mission_running:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)

print()
print("Mission ended")
# Mission has ended.
