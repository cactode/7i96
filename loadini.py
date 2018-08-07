def iniList():
	# Section, Item, Object Name
	iniList = []
	iniList.append(['EMC', 'VERSION', 'version'])
	iniList.append(['EMC', 'MACHINE', 'configName'])
	iniList.append(['EMC', 'DEBUG', 'debugCombo'])

	iniList.append(['HOSTMOT2', 'DRIVER', 'driverCB'])
	iniList.append(['HOSTMOT2', 'IPADDRESS', 'ipAddressCB'])
	iniList.append(['HOSTMOT2', 'BOARD', 'boardCB'])
	iniList.append(['HOSTMOT2', 'STEPGENS', 'stepgensSB'])
	iniList.append(['HOSTMOT2', 'ENCODERS', 'encodersSB'])
	iniList.append(['HOSTMOT2', 'SSERIAL_PORT', 'sserialSB'])

	iniList.append(['DISPLAY', 'DISPLAY', 'guiCB'])
	iniList.append(['DISPLAY', 'POSITION_OFFSET', 'positionOffsetCB'])
	iniList.append(['DISPLAY', 'POSITION_FEEDBACK', 'positionFeedbackCB'])

	iniList.append(['TRAJ', 'LINEAR_UNITS', 'linearUnitsCB'])
	iniList.append(['TRAJ', 'COORDINATES', 'coordinatesL'])
	iniList.append(['TRAJ', 'MAX_LINEAR_VELOCITY', 'maxLinearVelocity'])

	iniList.append(['JOINT_0', 'AXIS', 'axisCB_0'])
	iniList.append(['JOINT_0', 'STEPLEN', 'stepTime_0'])
	iniList.append(['JOINT_0', 'STEPSPACE', 'stepSpace_0'])
	iniList.append(['JOINT_0', 'DIRSETUP', 'dirSetup_0'])
	iniList.append(['JOINT_0', 'DIRHOLD', 'dirHold_0'])
	iniList.append(['JOINT_0', 'MIN_LIMIT', 'minLimit_0'])
	iniList.append(['JOINT_0', 'MAX_LIMIT', 'maxLimit_0'])
	iniList.append(['JOINT_0', 'MAX_VELOCITY', 'maxVelocity_0'])
	iniList.append(['JOINT_0', 'MAX_ACCELERATION', 'maxAccel_0'])
	iniList.append(['JOINT_0', 'SCALE', 'scale_0'])
	iniList.append(['JOINT_0', 'HOME', 'home_0'])
	iniList.append(['JOINT_0', 'HOME_OFFSET', 'homeOffset_0'])
	iniList.append(['JOINT_0', 'HOME_SEARCH_VEL', 'homeSearchVel_0'])
	iniList.append(['JOINT_0', 'HOME_LATCH_VEL', 'homeLatchVel_0'])
	iniList.append(['JOINT_0', 'HOME_USE_INDEX', 'homeUseIndex_0'])
	iniList.append(['JOINT_0', 'HOME_IGNORE_LIMITS', 'homeIgnoreLimits_0'])
	iniList.append(['JOINT_0', 'HOME_SEQUENCE', 'homeSequence_0'])
	iniList.append(['JOINT_0', 'P', 'p_0'])
	iniList.append(['JOINT_0', 'I', 'i_0'])
	iniList.append(['JOINT_0', 'D', 'd_0'])
	iniList.append(['JOINT_0', 'FF0', 'ff0_0'])
	iniList.append(['JOINT_0', 'FF1', 'ff1_0'])
	iniList.append(['JOINT_0', 'FF2', 'ff2_0'])
	iniList.append(['JOINT_0', 'DEADBAND', 'deadband_0'])
	iniList.append(['JOINT_0', 'BIAS', 'bias_0'])
	iniList.append(['JOINT_0', 'MAX_OUTPUT', 'maxOutput_0'])
	iniList.append(['JOINT_0', 'MAX_ERROR', 'maxError_0'])

	iniList.append(['JOINT_1', 'AXIS', 'axisCB_1'])
	iniList.append(['JOINT_1', 'STEPLEN', 'stepTime_1'])
	iniList.append(['JOINT_1', 'STEPSPACE', 'stepSpace_1'])
	iniList.append(['JOINT_1', 'DIRSETUP', 'dirSetup_1'])
	iniList.append(['JOINT_1', 'DIRHOLD', 'dirHold_1'])
	iniList.append(['JOINT_1', 'MIN_LIMIT', 'minLimit_1'])
	iniList.append(['JOINT_1', 'MAX_LIMIT', 'maxLimit_1'])
	iniList.append(['JOINT_1', 'MAX_VELOCITY', 'maxVelocity_1'])
	iniList.append(['JOINT_1', 'MAX_ACCELERATION', 'maxAccel_1'])
	iniList.append(['JOINT_1', 'SCALE', 'scale_1'])
	iniList.append(['JOINT_1', 'HOME', 'home_1'])
	iniList.append(['JOINT_1', 'HOME_OFFSET', 'homeOffset_1'])
	iniList.append(['JOINT_1', 'HOME_SEARCH_VEL', 'homeSearchVel_1'])
	iniList.append(['JOINT_1', 'HOME_LATCH_VEL', 'homeLatchVel_1'])
	iniList.append(['JOINT_1', 'HOME_USE_INDEX', 'homeUseIndex_1'])
	iniList.append(['JOINT_1', 'HOME_IGNORE_LIMITS', 'homeIgnoreLimits_1'])
	iniList.append(['JOINT_1', 'HOME_SEQUENCE', 'homeSequence_1'])
	iniList.append(['JOINT_1', 'P', 'p_1'])
	iniList.append(['JOINT_1', 'I', 'i_1'])
	iniList.append(['JOINT_1', 'D', 'd_1'])
	iniList.append(['JOINT_1', 'FF0', 'ff0_1'])
	iniList.append(['JOINT_1', 'FF1', 'ff1_1'])
	iniList.append(['JOINT_1', 'FF2', 'ff2_1'])
	iniList.append(['JOINT_1', 'DEADBAND', 'deadband_1'])
	iniList.append(['JOINT_1', 'BIAS', 'bias_1'])
	iniList.append(['JOINT_1', 'MAX_OUTPUT', 'maxOutput_1'])
	iniList.append(['JOINT_1', 'MAX_ERROR', 'maxError_1'])

	iniList.append(['JOINT_2', 'AXIS', 'axisCB_2'])
	iniList.append(['JOINT_2', 'STEPLEN', 'stepTime_2'])
	iniList.append(['JOINT_2', 'STEPSPACE', 'stepSpace_2'])
	iniList.append(['JOINT_2', 'DIRSETUP', 'dirSetup_2'])
	iniList.append(['JOINT_2', 'DIRHOLD', 'dirHold_2'])
	iniList.append(['JOINT_2', 'MIN_LIMIT', 'minLimit_2'])
	iniList.append(['JOINT_2', 'MAX_LIMIT', 'maxLimit_2'])
	iniList.append(['JOINT_2', 'MAX_VELOCITY', 'maxVelocity_2'])
	iniList.append(['JOINT_2', 'MAX_ACCELERATION', 'maxAccel_2'])
	iniList.append(['JOINT_2', 'SCALE', 'scale_2'])
	iniList.append(['JOINT_2', 'HOME', 'home_2'])
	iniList.append(['JOINT_2', 'HOME_OFFSET', 'homeOffset_2'])
	iniList.append(['JOINT_2', 'HOME_SEARCH_VEL', 'homeSearchVel_2'])
	iniList.append(['JOINT_2', 'HOME_LATCH_VEL', 'homeLatchVel_2'])
	iniList.append(['JOINT_2', 'HOME_USE_INDEX', 'homeUseIndex_2'])
	iniList.append(['JOINT_2', 'HOME_IGNORE_LIMITS', 'homeIgnoreLimits_2'])
	iniList.append(['JOINT_2', 'HOME_SEQUENCE', 'homeSequence_2'])
	iniList.append(['JOINT_2', 'P', 'p_2'])
	iniList.append(['JOINT_2', 'I', 'i_2'])
	iniList.append(['JOINT_2', 'D', 'd_2'])
	iniList.append(['JOINT_2', 'FF0', 'ff0_2'])
	iniList.append(['JOINT_2', 'FF1', 'ff1_2'])
	iniList.append(['JOINT_2', 'FF2', 'ff2_2'])
	iniList.append(['JOINT_2', 'DEADBAND', 'deadband_2'])
	iniList.append(['JOINT_2', 'BIAS', 'bias_2'])
	iniList.append(['JOINT_2', 'MAX_OUTPUT', 'maxOutput_2'])
	iniList.append(['JOINT_2', 'MAX_ERROR', 'maxError_2'])

	iniList.append(['JOINT_3', 'AXIS', 'axisCB_3'])
	iniList.append(['JOINT_3', 'STEPLEN', 'stepTime_3'])
	iniList.append(['JOINT_3', 'STEPSPACE', 'stepSpace_3'])
	iniList.append(['JOINT_3', 'DIRSETUP', 'dirSetup_3'])
	iniList.append(['JOINT_3', 'DIRHOLD', 'dirHold_3'])
	iniList.append(['JOINT_3', 'MIN_LIMIT', 'minLimit_3'])
	iniList.append(['JOINT_3', 'MAX_LIMIT', 'maxLimit_3'])
	iniList.append(['JOINT_3', 'MAX_VELOCITY', 'maxVelocity_3'])
	iniList.append(['JOINT_3', 'MAX_ACCELERATION', 'maxAccel_3'])
	iniList.append(['JOINT_3', 'SCALE', 'scale_3'])
	iniList.append(['JOINT_3', 'HOME', 'home_3'])
	iniList.append(['JOINT_3', 'HOME_OFFSET', 'homeOffset_3'])
	iniList.append(['JOINT_3', 'HOME_SEARCH_VEL', 'homeSearchVel_3'])
	iniList.append(['JOINT_3', 'HOME_LATCH_VEL', 'homeLatchVel_3'])
	iniList.append(['JOINT_3', 'HOME_USE_INDEX', 'homeUseIndex_3'])
	iniList.append(['JOINT_3', 'HOME_IGNORE_LIMITS', 'homeIgnoreLimits_3'])
	iniList.append(['JOINT_3', 'HOME_SEQUENCE', 'homeSequence_3'])
	iniList.append(['JOINT_3', 'P', 'p_3'])
	iniList.append(['JOINT_3', 'I', 'i_3'])
	iniList.append(['JOINT_3', 'D', 'd_3'])
	iniList.append(['JOINT_3', 'FF0', 'ff0_3'])
	iniList.append(['JOINT_3', 'FF1', 'ff1_3'])
	iniList.append(['JOINT_3', 'FF2', 'ff2_3'])
	iniList.append(['JOINT_3', 'DEADBAND', 'deadband_3'])
	iniList.append(['JOINT_3', 'BIAS', 'bias_3'])
	iniList.append(['JOINT_3', 'MAX_OUTPUT', 'maxOutput_3'])
	iniList.append(['JOINT_3', 'MAX_ERROR', 'maxError_3'])

	iniList.append(['JOINT_4', 'AXIS', 'axisCB_4'])
	iniList.append(['JOINT_4', 'STEPLEN', 'stepTime_4'])
	iniList.append(['JOINT_4', 'STEPSPACE', 'stepSpace_4'])
	iniList.append(['JOINT_4', 'DIRSETUP', 'dirSetup_4'])
	iniList.append(['JOINT_4', 'DIRHOLD', 'dirHold_4'])
	iniList.append(['JOINT_4', 'MIN_LIMIT', 'minLimit_4'])
	iniList.append(['JOINT_4', 'MAX_LIMIT', 'maxLimit_4'])
	iniList.append(['JOINT_4', 'MAX_VELOCITY', 'maxVelocity_4'])
	iniList.append(['JOINT_4', 'MAX_ACCELERATION', 'maxAccel_4'])
	iniList.append(['JOINT_4', 'SCALE', 'scale_4'])
	iniList.append(['JOINT_4', 'HOME', 'home_4'])
	iniList.append(['JOINT_4', 'HOME_OFFSET', 'homeOffset_4'])
	iniList.append(['JOINT_4', 'HOME_SEARCH_VEL', 'homeSearchVel_4'])
	iniList.append(['JOINT_4', 'HOME_LATCH_VEL', 'homeLatchVel_4'])
	iniList.append(['JOINT_4', 'HOME_USE_INDEX', 'homeUseIndex_4'])
	iniList.append(['JOINT_4', 'HOME_IGNORE_LIMITS', 'homeIgnoreLimits_40'])
	iniList.append(['JOINT_4', 'HOME_SEQUENCE', 'homeSequence_4'])
	iniList.append(['JOINT_4', 'P', 'p_4'])
	iniList.append(['JOINT_4', 'I', 'i_4'])
	iniList.append(['JOINT_4', 'D', 'd_4'])
	iniList.append(['JOINT_4', 'FF0', 'ff0_4'])
	iniList.append(['JOINT_4', 'FF1', 'ff1_4'])
	iniList.append(['JOINT_4', 'FF2', 'ff2_40'])
	iniList.append(['JOINT_4', 'DEADBAND', 'deadband_4'])
	iniList.append(['JOINT_4', 'BIAS', 'bias_4'])
	iniList.append(['JOINT_4', 'MAX_OUTPUT', 'maxOutput_4'])
	iniList.append(['JOINT_4', 'MAX_ERROR', 'maxError_4'])

	iniList.append(['INPUTS', 'INPUT_0', 'input_0'])
	iniList.append(['INPUTS', 'INPUT_1', 'input_1'])
	iniList.append(['INPUTS', 'INPUT_2', 'input_2'])
	iniList.append(['INPUTS', 'INPUT_3', 'input_3'])
	iniList.append(['INPUTS', 'INPUT_4', 'input_4'])
	iniList.append(['INPUTS', 'INPUT_5', 'input_5'])
	iniList.append(['INPUTS', 'INPUT_6', 'input_6'])
	iniList.append(['INPUTS', 'INPUT_7', 'input_7'])
	iniList.append(['INPUTS', 'INPUT_8', 'input_8'])
	iniList.append(['INPUTS', 'INPUT_9', 'input_9'])
	iniList.append(['INPUTS', 'INPUT_10', 'input_10'])

	iniList.append(['INPUTS', 'INPUT_JOINT_0', 'inputJoint_0'])
	iniList.append(['INPUTS', 'INPUT_JOINT_1', 'inputJoint_1'])
	iniList.append(['INPUTS', 'INPUT_JOINT_2', 'inputJoint_2'])
	iniList.append(['INPUTS', 'INPUT_JOINT_3', 'inputJoint_3'])
	iniList.append(['INPUTS', 'INPUT_JOINT_4', 'inputJoint_4'])
	iniList.append(['INPUTS', 'INPUT_JOINT_5', 'inputJoint_5'])
	iniList.append(['INPUTS', 'INPUT_JOINT_6', 'inputJoint_6'])
	iniList.append(['INPUTS', 'INPUT_JOINT_7', 'inputJoint_7'])
	iniList.append(['INPUTS', 'INPUT_JOINT_8', 'inputJoint_8'])
	iniList.append(['INPUTS', 'INPUT_JOINT_9', 'inputJoint_9'])
	iniList.append(['INPUTS', 'INPUT_JOINT_10', 'inputJoint_10'])

	iniList.append(['OUTPUTS', 'OUTPUT_0', 'output_0'])
	iniList.append(['OUTPUTS', 'OUTPUT_1', 'output_1'])
	iniList.append(['OUTPUTS', 'OUTPUT_2', 'output_2'])
	iniList.append(['OUTPUTS', 'OUTPUT_3', 'output_3'])
	iniList.append(['OUTPUTS', 'OUTPUT_4', 'output_4'])

	iniList.append(['OPTIONS', 'MANUAL_TOOL_CHANGE', 'manualToolChangeCB'])
	iniList.append(['OPTIONS', 'HALUI', 'haluiCB'])
	iniList.append(['OPTIONS', 'PYVCP', 'pyvcpCB'])


	return iniList

#iniList.append(['', '', ''])
