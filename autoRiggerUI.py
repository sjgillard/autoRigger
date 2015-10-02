import maya.cmds as cmds

def makeUI():
	if cmds.window('autoRigger', exists=True):
		cmds.deleteUI('autoRigger', window=True)

	panelWindow = cmds.window('autoRigger', title="SJG Auto Rigger Window", sizeable=True)
	form = cmds.formLayout()

	butLocators = cmds.button(label='Layout Locators', width=110, height=30, backgroundColor=(0.616, 0.682, 0.722))
	butMaekRig = cmds.button(label='Make Rig', width=110, height=30, backgroundColor=(0.616, 0.682, 0.722))
	rigCollection = cmds.radioCollection()
	rButIK = cmds.radioButton(label='IK Handles', collection=rigCollection)
	rButStretch = cmds.radioButton(label='Stretchy Rig', collection=rigCollection)

	info = cmds.text(label='This is an auto rigger tool to help you create rigs quickly.\nLayout locators in your scene, then you can make your rig.')

	cmds.formLayout(form, edit=True,
			attachForm=[
			(info, 'left', 5), (info, 'top', 5),
			(butLocators, 'left', 50),
			(butMaekRig, 'left', 50),
			(rButIK, 'left', 60),
			(rButStretch, 'left', 60)
			],
			attachControl=[
			(butLocators, 'top', 15, info),
			(butMaekRig, 'top', 10, butLocators),
			(rButIK, 'top', 5, butMaekRig),
			(rButStretch, 'left', 5, rButIK), (rButStretch, 'top', 5, butMaekRig)
			]
		)

	cmds.showWindow(panelWindow)
	cmds.window (panelWindow, edit=True, width=250, height=200)
