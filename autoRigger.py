#autoRigger plus GUI
import maya.cmds as cmds

class SJG_AutoRiggerOptionsWindow(object):
    @classmethod
    def showUI(cls):
        win=cls()
        win.create()
        return win
        
    def __init__(self):
        self.window = 'sjg_autoRiggerOptionsWindow'
        self.title = 'Auto Rigger Options Window'
        self.size = (546, 350)
        self.supportsToolAction = False
        self.actionName = 'Apply and Close'
        
    def create(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)
        self.window = cmds.window(
            self.window,
            title=self.title,
            widthHeight=self.size,
            menuBar=True
        )
        self.mainForm = cmds.formLayout(nd=100)
        self.commonMenu()
        self.commonButtons()
        self.optionsBorder = cmds.tabLayout(
            scrollable=True,
            tabsVisible=False,
            height=1
        )
        cmds.formLayout(
            self.mainForm, e=True,
            attachForm=(
                [self.optionsBorder,'top',0],
                [self.optionsBorder,'left',2],
                [self.optionsBorder,'right',2]
            ),
            attachControl=(
                [self.optionsBorder,'bottom',5,self.applyBtn]
            )
        )
        self.displayOptions()
        cmds.showWindow()
        
    def commonMenu(self):
        self.editMenu = cmds.menu(label='Edit')
        self.editNenuSave = cmds.menuItem(label='Save Settings')
        self.editMenuReset = cmds.menuItem(label='Reset Settings')
        self.editMenuDiv = cmds.menuItem(d=True)
        self.editMenuRadiio = cmds.radioMenuItemCollection()
        self.editMenuTool = cmds.menuItem(label='As Tool', radioButton=True, enable=self.supportsToolAction)
        self.editMenuAction =cmds.menuItem(label='As Action', radioButton=True, enable=self.supportsToolAction)
        self.helpMenu = cmds.menu(label='Help')
        self.helpMenuItem = cmds.menuItem(label='Help on %s'%self.title, command=self.helpMenuCmd)
        
    def helpMenuCmd(self, *args):
        cmds.launch(web='http://lmgtfy.com/')
        
    def editMenuSaveCmd(self, *args):
        pass
        
    def editMenuResetCmd(self, *args):
        pass
        
    def editMenuToolCmd(self, *args):
        pass
        
    def editMenuActionCmd(self, *args):
        pass
        
    def actionBtnCmd(self, *args):
        self.applyBtn()
        self.closeBtn()
        
    def applyBtnCmd(self, *args):
        pass
        
    def closeBtnCmd(self, *args):
        cmds.deleteUI(self.window, window=True)
        
    def commonButtons(self):
        self.commonBtnSize = ((self.size[0]-18)/3, 26)
        self.actionBtn = cmds.button(
            label=self.actionName,
            height=self.commonBtnSize[1],
            command=self.applyBtnCmd
        )
        self.applyBtn = cmds.button(
            label='Apply',
            height=self.commonBtnSize[1],
            command=self.applyBtnCmd
        )
        self.closeBtn = cmds.button(
            label='Close',
            height=self.commonBtnSize[1],
            command=self.closeBtnCmd
        )
        cmds.formLayout(
            self.mainForm, e=True,
            attachForm=(
                [self.actionBtn,'left',5],
                [self.actionBtn,'bottom',5],
                [self.applyBtn,'bottom',5],
                [self.closeBtn,'bottom',5],
                [self.closeBtn,'right',5]
            ),
            attachPosition=(
                [self.actionBtn,'right',1,33],
                [self.closeBtn,'left',0,67]
            ),
            attachControl=(
                [self.applyBtn,'left',4,self.actionBtn],
                [self.applyBtn,'right',4,self.closeBtn]
            ),
            attachNone=(
                [self.actionBtn,'top'],
                [self.applyBtn,'top'],
                [self.closeBtn,'top']
            )
        )
        
    def displayOptions(self):
        pass

class SJG_CreateJoints(object):

    charName = ''
    prefix = ''
    def __init__(self):
        self.charName = 'nameMe'
        self.prefix = 'rig'

    #Organization of file
    def makeGroups():
        cmds.group(em=True, name=charName)
        cmds.group(em=True, name='geometry')
        cmds.parent('geometry', charName)
        cmds.group(em=True, name='globalControl')
        cmds.parent('globalControl', charName)
        cmds.group(em=True, name='globalScale')
        cmds.parent('globalScale', 'globalControl')
        cmds.group(em=True, name='grpJoint')
        cmds.parent('grpJoint', 'globalScale')
        cmds.group(em=True, name='controlCurves')
        cmds.parent('controlCurves', 'globalScale')
        cmds.group(em=True, name='influenceObjects')
        cmds.parent('influenceObjects', 'globalScale')
        cmds.group(em=True, name='clusterHandles')
        cmds.parent('clusterHandles', 'globalScale')
        cmds.group(em=True, name='extraNodes')
        cmds.parent('extraNodes', 'globalScale')

    #first to be called
    def makeLocators():
        #Torso and Head Locators
        cmds.spaceLocator(p=(0, 22.112, 0.007), n='loc_pelvis01')
        cmds.spaceLocator(p=(0, 24.778, 0.348), n='loc_spine01')
        cmds.spaceLocator(p=(0, 27.658, 0.198), n='loc_spine02')
        cmds.spaceLocator(p=(0, 31.028, -0.441), n='loc_spine03')
        cmds.spaceLocator(p=(-0.004, 31.99, -0.441), n='loc_neckBase01')
        cmds.spaceLocator(p=(0.004, 33.027, -0.441), n='loc_neck01')
        cmds.spaceLocator(p=(0, 33.866, -0.527), n='loc_headBase01')
        cmds.spaceLocator(p=(0.004, 36.395, -0.703), n='loc_head01')
        cmds.spaceLocator(p=(0.004, 35.427, 0.157), n='loc_jaw01')
        cmds.spaceLocator(p=(0.004, 34.575, 1.952), n='loc_jawTip')
        cmds.spaceLocator(p=(0, 39.01, 0.903), n='loc_headTip')
        cmds.spaceLocator(p=(0.727, 37.622, 2.126), n='loc_l_eye01')
    
        #Left Clavicle to Hand Locators
        cmds.spaceLocator(p=(0.897, 30.941, 1.076), n='loc_l_clavicle01')
        cmds.spaceLocator(p=(2.379, 31.043, -0.047), n='loc_l_shoulder01')
        cmds.spaceLocator(p=(7.228, 30.912, -0.766), n='loc_l_elbow01')
        cmds.spaceLocator(p=(13.035, 30.932, 0.088), n='loc_l_wrist01')
        cmds.spaceLocator(p=(15.067, 30.968, 0), n='loc_l_palm01')
        cmds.spaceLocator(p=(17.093, 30.968, 1.551), n='loc_l_index01')
        cmds.spaceLocator(p=(18.749, 30.968, 1.551), n='loc_l_index02')
        cmds.spaceLocator(p=(20.158, 30.926, 1.551), n='loc_l_index03')
        cmds.spaceLocator(p=(21.771, 30.885, 1.551), n='loc_l_indexTip')
        cmds.spaceLocator(p=(17.093, 30.968, 0.204), n='loc_l_middle01')
        cmds.spaceLocator(p=(18.953, 30.968, 0.204), n='loc_l_middle02')
        cmds.spaceLocator(p=(20.648, 30.926, 0.204), n='loc_l_middle03')
        cmds.spaceLocator(p=(22.384, 30.885, 0.204), n='loc_l_middleTip')
        cmds.spaceLocator(p=(17.093, 30.968, -1.021), n='loc_l_ring01')
        cmds.spaceLocator(p=(18.708, 30.968, -1.021), n='loc_l_ring02')
        cmds.spaceLocator(p=(20.198, 30.926, -1.021), n='loc_l_ring03')
        cmds.spaceLocator(p=(21.771, 30.885, -1.021), n='loc_l_ringTip')
        cmds.spaceLocator(p=(17.093, 30.968, -2.409), n='loc_l_pinky01')
        cmds.spaceLocator(p=(18.504, 30.968, -2.409), n='loc_l_pinky02')
        cmds.spaceLocator(p=(19.668, 30.926, -2.409), n='loc_l_pinky03')
        cmds.spaceLocator(p=(20.914, 30.885, -2.409), n='loc_l_pinkyTip')
        cmds.spaceLocator(p=(14.034, 30.885, 0.817), n='loc_l_thumb01')
        cmds.spaceLocator(p=(14.654, 29.769, 1.511), n='loc_l_thumb02')
        cmds.spaceLocator(p=(15.935, 28.818, 2.531), n='loc_l_thumb03')
        cmds.spaceLocator(p=(16.969, 28.033, 3.062), n='loc_l_thumbTip')
        
        #Left Leg and Foot Locators
        cmds.spaceLocator(p=(1.894, 20.457, 0), n='loc_l_hip01')
        cmds.spaceLocator(p=(1.996, 12.753, 1.338), n='loc_l_knee01')
        cmds.spaceLocator(p=(2.139, 2.495, 0), n='loc_l_ankle01')
        cmds.spaceLocator(p=(2.139, 0.826, 2.957), n='loc_l_ball01')
        cmds.spaceLocator(p=(2.139, 0.826, 5.751), n='loc_l_toeTip')

    #To be used after joint creation
    def deleteLocators():
        cmds.select('loc*')
        cmds.delete(cmds.ls(selection=True))

    #To be used after first half of locators are in position
    def mirrorLocators():
        cmds.group(cmds.ls(selection=True), n='temp1')
        cmds.duplicate('temp1')
        cmds.setAttr('temp2.scalePivot', 0,0,0)
        cmds.setAttr('temp2.rotatePivot', 0,0,0)
        cmds.setAttr('temp2.scaleX', -1)
        cmds.select( 'temp2')
        cmds.makeIdentity(apply=True)
    
        children = cmds.listRelatives('temp2', children=True, type='transform', fullPath=True)
        prefixL = 'loc_l_'
        prefixR = 'loc_r_'
        newName = ''
        substring = []
        for i in children:
            substring = i.split('_')
            if prefixL in i:
                newName = prefixR + substring[2]
                cmds.rename(i, newName)
            else:
                newName = prefixL + substring[2]
                cmds.rename(i, newName)

        cmds.select('loc*')
        locators = [cmds.ls(selection=True)]
        for i in locators:
            cmds.parent(i, world=True)
        
        cmds.delete('temp1')
        cmds.delete('temp2')

   
    #Joint creation after locators are in place

    #Locator positions
    def getLocPos(locators):
        positions = []
    
        for l in locators:
            positions.append(cmds.pointPosition(l))
        return positions
        
    #Generic joint creation method, takes position from locators and creates joints
    def makeJoints(positions):
        length = len(positions)
        num = 0
    
        cmds.select( d=True )
        for p in positions:
            cmds.joint(p=positions[num])
        
            if num<len:
                num+=1
    
        cmds.select('joint*')
        joints = cmds.ls(selection=True)
    
        return joints

    #Creates both the right and left arms using makeJoints() and getLocPos()
    def runItArm():
        #make a right and left locators available
        cmds.select('loc_l_clavicle01', 'loc_l_shoulder01', 'loc_l_elbow01', 'loc_l_wrist01')
        locatorsL = cmds.ls(selection=True)
        cmds.select('loc_r_clavicle01', 'loc_r_shoulder01', 'loc_r_elbow01', 'loc_r_wrist01')
        locatorsR = cmds.ls(selection=True)    
    
        positionL=getLocPos(locatorsL)
        positionR=getLocPos(locatorsR)
    
        #left arm joints, this way we don't have to worry about things getting messed up in mirroring
        armJointsL = makeJoints(positionL)
        #prefix = 'rig_'
        newName = ''
        suffix = []
        num = 0
    
        for a in armJointsL:
            suffix = locatorsL[num].split('_')
            if 'wrist' in suffix[2]:
                newName = 'jnt_'+suffix[1]+'_wrist01'
            else:
                newName = prefix + suffix[1] + '_' + suffix[2]

            cmds.rename(a, newName)
            if num<2:
                num += 1
    
        #right arm joints, this way we don't have to worry about things getting messed up in mirroring
        armJointsR = makeJoints(positionR)
        num = 0
        #prefix = 'rig_'
        newName = ''
        suffix = []
        num = 0
    
        for a in armJointsR:
            suffix = locatorsR[num].split('_')
            if 'wrist' in suffix[2]:
                newName = 'jnt_'+suffix[1]+'_wrist01'
            else:
                newName = prefix + suffix[1] + '_' + suffix[2]
            
            cmds.rename(a, newName)
            if num<2:
                num += 1
            
        cmds.parent('rig_*_clavicle01', 'grpJoint')
    
    
    #Creates both the right and left feet using makeJoints() and getLocPos()
    def runItFeet():
        #make a right and left locators available
        cmds.select('loc_l_ankle01', 'loc_l_ball01', 'loc_l_toeTip')
        locatorsL = cmds.ls(selection=True)
        cmds.select('loc_r_ankle01', 'loc_r_ball01', 'loc_r_toeTip')
        locatorsR = cmds.ls(selection=True)    
    
        positionL=getLocPos(locatorsL)
        positionR=getLocPos(locatorsR)
    
        #left foot joints, this way we don't have to worry about things getting messed up in mirroring
        footJointsL = makeJoints(positionL)
        #prefix = 'rig_'
        newName = ''
        suffix = []
        num = 0
    
        for f in footJointsL:
            suffix = locatorsL[num].split('_')
            if 'Tip' in suffix[2]:
                newName = 'jnt_'+suffix[1]+'_toeTip'
            else:
                newName = prefix + suffix[1] + '_' + suffix[2]
            cmds.rename(f, newName)
            if num<2:
                num += 1
    
        #right foot joints, this way we don't have to worry about things getting messed up in mirroring
        armJointsR = makeJoints(positionR)
        num = 0
        #prefix = 'rig_'
        newName = ''
        suffix = []
        num = 0
    
        for f in footJointsL:
            suffix = locatorsR[num].split('_')
            if 'Tip' in suffix[2]:
            newName = 'jnt_'+suffix[1]+'_toeTip'
            else:
                newName = prefix + suffix[1] + '_' + suffix[2]
            cmds.rename(f, newName)
            if num<2:
                num += 1
            
        cmds.parent('rig_*_ankle01', 'grpJoint')
    
    #Creates both the right and left legs using makeJoints() and getLocPos()
    def runItLeg():
        #make a right and left locators available
        cmds.select('loc_l_hip01', 'loc_l_knee01', 'loc_l_ankle01')
        locatorsL = cmds.ls(selection=True)
        cmds.select('loc_r_hip01', 'loc_r_knee01', 'loc_r_ankle01')
        locatorsR = cmds.ls(selection=True)    
    
        positionL=getLocPos(locatorsL)
        positionR=getLocPos(locatorsR)
    
        #left leg joints, this way we don't have to worry about things getting messed up in mirroring
        legJointsL = makeJoints(positionL)
        #prefix = 'rig_'
        newName = ''
        suffix = []
        num = 0
    
        for l in legJointsL:
            suffix = locatorsL[num].split('_')
            if 'ankle' in suffix[2]:
                newName = 'jnt_' + suffix[1] + '_' + suffix[2]
            else:
                newName = prefix + suffix[1] + '_' + suffix[2]
            cmds.rename(l, newName)
            if num<3:
                num += 1
    
        #right leg joints, this way we don't have to worry about things getting messed up in mirroring
        legJointsR = makeJoints(positionR)
        #prefix = 'rig_'
        newName = ''
        suffix = []
        num = 0
    
        for l in legJointsR:
            suffix = locatorsR[num].split('_')
            if 'ankle' in suffix[2]:
                newName = 'jnt_' + suffix[1] + '_' + suffix[2]
            else:
                newName = prefix + suffix[1] + '_' + suffix[2]
            cmds.rename(l, newName)
            if num<3:
                num += 1
            
        cmds.parent('rig_*_hip01', 'grpJoint')

    #Make Center Joints with makeJoints() and getLocPos()
    def runItCenter():
        cmds.select('loc_pelvis01', 'loc_spine01', 'loc_spine02', 'loc_spine03', 'loc_neckBase01', 'loc_neck01', 'loc_headBase01', 'loc_head01', 'loc_headTip', 'loc_jaw01', 'loc_jawTip')
        locators = cmds.ls(selection=True)
    
        positions=getLocPos(locators)
    
        centerJoints = makeJoints(positions)
    
        newName = ''
        suffix = []
        num = 0
        length = len(locators)
    
        for c in centerJoints:
            suffix = locators[num].split('_')
            if 'Tip' in suffix[1]:
                newName = 'jnt_' + suffix[1]
            else:
                newName = 'rig_' + suffix[1]
            cmds.rename(c, newName)
            if num < length:
                num+=1
            
    
        cmds.parent('rig_jaw01', 'rig_head01')
        cmds.parent('rig_pelvis01', 'grpJoint')
    
    
    #Make Hand Joints using makeJoints() and getLocPos()
    def runItHand():
        cmds.select('loc_l_wrist01', 'loc_l_palm01', 'loc_l_thumb01', 'loc_l_thumb02', 'loc_l_thumb03', 'loc_l_thumbTip', 'loc_l_index01', 'loc_l_index02', 'loc_l_index03', 'loc_l_indexTip', 'loc_l_middle01', 'loc_l_middle02', 'loc_l_middle03', 'loc_l_middleTip', 'loc_l_ring01', 'loc_l_ring02', 'loc_l_ring03', 'loc_l_ringTip', 'loc_l_pinky01', 'loc_l_pinky02', 'loc_l_pinky03', 'loc_l_pinkyTip', 'loc_r_wrist01', 'loc_r_palm01', 'loc_r_thumb01', 'loc_r_thumb02', 'loc_r_thumb03', 'loc_r_thumbTip', 'loc_r_index01', 'loc_r_index02', 'loc_r_index03', 'loc_r_indexTip', 'loc_r_middle01', 'loc_r_middle02', 'loc_r_middle03', 'loc_r_middleTip', 'loc_r_ring01', 'loc_r_ring02', 'loc_r_ring03', 'loc_r_ringTip', 'loc_r_pinky01', 'loc_r_pinky02', 'loc_r_pinky03', 'loc_r_pinkyTip')
        locators = cmds.ls(selection=True)
    
        positions = getLocPos(locators)

        handJoints = makeJoints(positions)
    
        newName = ''
        suffix = []
        num = 0
        length = len(locators)
    
        for h in handJoints:
            suffix = locators[num].split('_')
            if 'Tip' in suffix[2]:
                newName = 'jnt_' + suffix[1] + '_' + suffix[2]
            else:
                newName = prefix + suffix[1] + '_' + suffix[2]
            cmds.rename(h, newName)
            if num < length:
                num+=1
            
            

        cmds.parent('rig_l_index01', 'rig_l_palm01')
        cmds.parent('rig_r_index01', 'rig_r_palm01')
        cmds.parent('rig_l_middle01', 'rig_l_palm01')
        cmds.parent('rig_r_middle01', 'rig_r_palm01')
        cmds.parent('rig_l_ring01', 'rig_l_palm01')
        cmds.parent('rig_r_ring01', 'rig_r_palm01')
        cmds.parent('rig_l_pinky01', 'rig_l_palm01')
        cmds.parent('rig_r_pinky01', 'rig_r_palm01')
        cmds.parent('rig_*_wrist01', 'grpJoint')
    

#Controls as well as constraints and IK handles
class SJG_CreateControls(object):

    def __init__(self):

    def makeCircle(name):
        cmds.circle(n='cc_temp')
        cmds.setAttr('cc_temp.rotateZ', 90)
        cmds.select('cc_temp')
        cmds.makeIdentity(apply=True)
        cmds.group(cmds.ls(selection=True), n='grp_cc_temp')
        newName = 'cc_'+name
        cmds.rename('cc_temp', newName)
        newName = 'grp_cc_'+name
        cmds.rename('grp_cc_temp',newName)
    

    def makeCurves():
        #globalControl and globalScale
        cmds.curve(d=1, p=[(3,0,1),(3,0,4),(5,0,4),(0,0,9),(-5,0,4),(-3,0,4),(-3,0,1),(-6,0,1),(-6,0,3),(-10,0,0),(-6,0,-3),(-6,0,-1),(-3,0,-1),(-3,0,-4),(-5,0,-4),(0,0,-9),(5,0,-4),(3,0,-4),(3,0,-1),(6,0,-1),(6,0,-3),(10,0,0),(6,0,3),(6,0,1),(3,0,1)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
        cmds.parent('curveShape1', 'globalControl', shape=True, relative=True)
        cmds.textCurves( f='Times-Roman', t='S', n='gScale')
        cmds.setAttr('gScaleShape.rotateX', 90)
        cmds.setAttr('gScaleShape.translateX', -1.23)
        cmds.setAttr('gScaleShape.translateZ', 3.859)
        cmds.select('gScaleShape')
        cmds.makeIdentity(apply=True)
        cmds.parent('curveShape2', 'globalScale', shape=True, relative=True)

        #pelvis and torso controls
        makeCircle('pelvis')
        cmds.parentConstraint('rig_pelvis01','grp_cc_pelvis')
        cmds.delete('grp_cc_pelvis_parentConstraint1')
        cmds.setAttr('grp_cc_pelvis.rotateX', 90)
        cmds.select('cc_pelvis')
        cmds.scale(2.13742, 2.13742, 2.13742, cmds.ls(selection=True))
        cmds.makeIdentity(apply=True)
        cmds.parent('grp_cc_pelvis', 'controlCurves')
    
        makeCircle('abs')
        cmds.parentConstraint('rig_spine01','grp_cc_abs')
        cmds.delete('grp_cc_abs_parentConstraint1')
        cmds.setAttr('grp_cc_abs.rotateX', 90)
        cmds.select('cc_abs')
        cmds.scale(2.13742, 2.13742, 2.13742, cmds.ls(selection=True))
        cmds.makeIdentity(apply=True)
        cmds.parent('grp_cc_abs', 'cc_pelvis')
    
        makeCircle('chest')
        cmds.parentConstraint('rig_spine02','rig_spine03','grp_cc_chest')
        cmds.delete('grp_cc_chest_parentConstraint1')
        cmds.setAttr('grp_cc_chest.rotateX', 90)
        cmds.select('cc_chest')
        cmds.scale(2.13742, 2.13742, 2.13742, cmds.ls(selection=True))
        cmds.makeIdentity(apply=True)
        cmds.parent('grp_cc_chest', 'cc_abs')
    
        #left arm and hand
        cmds.curve(d=1, p=[(-0.295804, 0.372902, 2.231799), (1.712118, 0.372902, 1.816883), (1.375825, 0.372902, 1.105016), (-0.632098, 0.372902, 1.519932), (-0.295804, 0.372902, 2.231799), (-0.295804, -0.372902, 2.231799), (-0.632098, -0.372902, 1.519932), (-0.632098, 0.372902, 1.519932), (1.375825, 0.372902, 1.105016), (1.375825, -0.372902, 1.105016), (-0.632098, -0.372902, 1.519932), (-0.295804, -0.372902, 2.231799), (1.712118, -0.372902, 1.816883), (1.375825, -0.372902, 1.105016), (1.375825, 0.372902, 1.105016), (1.712118, 0.372902, 1.816883), (1.712118, -0.372902, 1.816883)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], n='cc_l_clavicle')
        cmds.select('cc_l_clavicle')
        cmds.group(cmds.ls(selection=True), n='grp_cc_l_clavicle')
        cmds.xform('grp_cc_l_clavicle', cp=1)
        cmds.xform('cc_l_clavicle', cp=1)
        cmds.parentConstraint('rig_l_clavicle01', 'grp_cc_l_clavicle')
        cmds.delete('grp_cc_l_clavicle_parentConstraint1')
        cmds.parent('grp_cc_l_clavicle', 'controlCurves')

        makeCircle('l_shoulder')
        cmds.parentConstraint('rig_l_shoulder01', 'grp_cc_l_shoulder')
        cmds.delete('grp_cc_l_shoulder_parentConstraint1')
        cmds.setAttr('grp_cc_l_shoulder.rotateX', 90)
        cmds.parent('grp_cc_l_shoulder', 'grp_cc_l_clavicle')

        makeCircle('l_elbow')
        cmds.parentConstraint('rig_l_elbow01', 'grp_cc_l_elbow')
        cmds.delete('grp_cc_l_elbow_parentConstraint1')
        cmds.setAttr('grp_cc_l_elbow.rotateX', 90)
        cmds.parent('grp_cc_l_elbow', 'grp_cc_l_shoulder')

        makeCircle('l_wrist')
        cmds.parentConstraint('rig_l_wrist01', 'grp_cc_l_wrist')
        cmds.delete('grp_cc_l_wrist_parentConstraint1')
        cmds.setAttr('grp_cc_l_wrist.rotateX', 90)
        cmds.parent('grp_cc_l_wrist', 'grp_cc_l_elbow')

        makeCircle('l_arm')
        cmds.parentConstraint('rig_l_wrist01', 'grp_cc_l_arm')
        cmds.delete('grp_cc_l_arm_parentConstraint1')
        cmds.setAttr('grp_cc_l_arm.rotateX', 90)
        cmds.parent('grp_cc_l_elbow', 'grp_cc_l_clavicle')

        #A group to make the fingers follow the wrist while giving a level of separation
        cmds.group(em=True, name='grp_l_fingers')
        cmds.parentConstraint('grp_l_fingers', 'rig_l_wrist01')

        makeCircle('l_index01')
        cmds.parentConstraint('rig_l_index01', 'grp_cc_l_index01')
        cmds.delete('grp_cc_l_index01_parentConstraint1')
        cmds.setAttr('grp_cc_l_index01.rotateX', 90)
        cmds.parent('grp_cc_l_index01', 'grp_l_fingers')

        makeCircle('l_index02')
        cmds.parentConstraint('rig_l_index02', 'grp_cc_l_index02')
        cmds.delete('grp_cc_l_index02_parentConstraint1')
        cmds.setAttr('grp_cc_l_index02.rotateX', 90)
        cmds.parent('grp_cc_l_index02', 'cc_l_index01')

        makeCircle('l_index03')
        cmds.parentConstraint('rig_l_index03', 'grp_cc_l_index03')
        cmds.delete('grp_cc_l_index03_parentConstraint1')
        cmds.setAttr('grp_cc_l_index03.rotateX', 90)
        cmds.parent('grp_cc_l_index03', 'cc_l_index02')

        makeCircle('l_middle01')
        cmds.parentConstraint('rig_l_middle01', 'grp_cc_l_middle01')
        cmds.delete('grp_cc_l_middle01_parentConstraint1')
        cmds.setAttr('grp_cc_l_middle01.rotateX', 90)
        cmds.parent('grp_cc_l_middle01', 'grp_l_fingers')

        makeCircle('l_middle02')
        cmds.parentConstraint('rig_l_middle02', 'grp_cc_l_middle02')
        cmds.delete('grp_cc_l_middle02_parentConstraint1')
        cmds.setAttr('grp_cc_l_middle02.rotateX', 90)
        cmds.parent('grp_cc_l_middle02', 'cc_l_middle01')

        makeCircle('l_middle03')
        cmds.parentConstraint('rig_l_middle03', 'grp_cc_l_middle03')
        cmds.delete('grp_cc_l_middle03_parentConstraint1')
        cmds.setAttr('grp_cc_l_middle03.rotateX', 90)
        cmds.parent('grp_cc_l_middle03', 'cc_l_middle02')

        makeCircle('l_ring01')
        cmds.parentConstraint('rig_l_ring01', 'grp_cc_l_ring01')
        cmds.delete('grp_cc_l_ring01_parentConstraint1')
        cmds.setAttr('grp_cc_l_ring01.rotateX', 90)
        cmds.parent('grp_cc_l_ring01', 'grp_l_fingers')

        makeCircle('l_ring02')
        cmds.parentConstraint('rig_l_ring02', 'grp_cc_l_ring02')
        cmds.delete('grp_cc_l_ring02_parentConstraint1')
        cmds.setAttr('grp_cc_l_ring02.rotateX', 90)
        cmds.parent('grp_cc_l_ring02', 'cc_l_ring01')

        makeCircle('l_ring03')
        cmds.parentConstraint('rig_l_ring03', 'grp_cc_l_ring03')
        cmds.delete('grp_cc_l_ring03_parentConstraint1')
        cmds.setAttr('grp_cc_l_ring03.rotateX', 90)
        cmds.parent('grp_cc_l_ring03', 'cc_l_ring02')

        makeCircle('l_pinky01')
        cmds.parentConstraint('rig_l_pinky01', 'grp_cc_l_pinky01')
        cmds.delete('grp_cc_l_pinky01_parentConstraint1')
        cmds.setAttr('grp_cc_l_pinky01.rotateX', 90)
        cmds.parent('grp_cc_l_pinky01', 'grp_l_fingers')

        makeCircle('l_pinky02')
        cmds.parentConstraint('rig_l_pinky02', 'grp_cc_l_pinky02')
        cmds.delete('grp_cc_l_pinky02_parentConstraint1')
        cmds.setAttr('grp_cc_l_pinky02.rotateX', 90)
        cmds.parent('grp_cc_l_pinky02', 'cc_l_pinky01')

        makeCircle('l_pinky03')
        cmds.parentConstraint('rig_l_pinky03', 'grp_cc_l_pinky03')
        cmds.delete('grp_cc_l_pinky03_parentConstraint1')
        cmds.setAttr('grp_cc_l_pinky03.rotateX', 90)
        cmds.parent('grp_cc_l_pinky03', 'cc_l_pinky02')

        #legs and feet

        #mirror left controls to right
        cmds.select('grp_cc_l*')
        cmds.group(cmds.ls(selection=True), name='temp1')
        cmds.duplicate('temp1')
        cmds.setAttr('temp2.scalePivot', 0,0,0)
        cmds.setAttr('temp2.rotatePivot', 0,0,0)
        cmds.setAttr('temp2.scaleX', -1)
        cmds.select( 'temp2')
        cmds.makeIdentity(apply=True)
    
        children = cmds.listRelatives('temp2', children=True, type='transform', fullPath=True)
        newName = ''
        substring = []
        for i in children:
            substring = i.split('_')
            for s in substring:
                if 'l' in s:
                    newName = newName + 'r'
                else:
                    newName = newName + s
            cmds.rename(i, newName)

        cmds.select('*cc*')
        locators = [cmds.ls(selection=True)]
        for i in locators:
            cmds.parent(i, world=True)
        
        cmds.delete('temp1')
        cmds.delete('temp2')

    def makeFKConstraints(self):
        #first duplicate arm joints
        cmds.duplicate('rig_l_clavicle01')
        cmds.rename('rig_l_clavicle02', 'jnt_l_clavicleFK')
        children = cmds.listRelatives('jnt_l_clavicleFK', children=True, type='transform', fullPath=True)
        cmds.rename(children[0], 'jnt_l_shoulderFK')
        cmds.rename(children[1], 'jnt_l_elbowFK')
        cmds.rename(children[2], 'jnt_l_wristFK')
        cmds.parentConstraint('rig_l_clavicle01', 'jnt_l_clavicleFK')

        cmds.duplicate('rig_r_clavicle01')
        cmds.rename('rig_r_clavicle02', 'jnt_r_clavicleFK')
        children = cmds.listRelatives('jnt_r_clavicleFK', children=True, type='transform', fullPath=True)
        cmds.rename(children[0], 'jnt_r_shoulderFK')
        cmds.rename(children[1], 'jnt_r_elbowFK')
        cmds.rename(children[2], 'jnt_r_wristFK')
        cmds.parentConstraint('rig_r_clavicle01', 'jnt_r_clavicleFK')

        #next hook up controls to FK chain
        cmds.parentConstraint('cc_l_shoulder', 'jnt_l_shoulderFK')
        cmds.parentConstraint('cc_l_elbow', 'jnt_l_elbowFK')
        cmds.parentConstraint('cc_l_wrist', 'jnt_l_wristFK')

        cmds.parentConstraint('cc_r_shoulder', 'jnt_r_shoulderFK')
        cmds.parentConstraint('cc_r_elbow', 'jnt_r_elbowFK')
        cmds.parentConstraint('cc_r_wrist', 'jnt_r_wristFK')

        #next hook up the FK chain to the rig chain
        cmds.parentConstraint('jnt_l_shoulderFK','rig_l_shoulder01')
        cmds.parentConstraint('jnt_l_eblowFK','rig_l_elbow01')
        cmds.parentConstraint('jnt_l_wristFK','jnt_l_wrist01')

        cmds.parentConstraint('jnt_r_shoulderFK','rig_r_shoulder01')
        cmds.parentConstraint('jnt_r_elbowFK','rig_r_elbow01')
        cmds.parentConstraint('jnt_r_wristFK','jnt_r_wrist01')

        #first duplicate leg joints
        cmds.duplicate('rig_l_hip01')
        cmds.rename('rig_l_hip02', 'jnt_l_hipFK')
        children = cmds.listRelatives('jnt_l_hipFK', children=True, type='transform', fullPath=True)
        cmds.rename(children[0], 'jnt_l_kneeFK')
        cmds.rename(children[1], 'jnt_l_ankleFK')

        cmds.duplicate('rig_r_hip01')
        cmds.rename('rig_r_hip02', 'jnt_r_hipFK')
        children = cmds.listRelatives('jnt_r_hipFK', children=True, type='transform', fullPath=True)
        cmds.rename(children[0], 'jnt_r_kneeFK')
        cmds.rename(children[1], 'jnt_r_ankleFK') 
