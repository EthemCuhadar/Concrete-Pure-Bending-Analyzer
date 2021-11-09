from BeamGeometry import Area

characteristicStrengthOfConcrete = int(input("characteristic strength of concrete(MPa): "))
characteristicStrengthOfSteel = int(input("characteristic strength of steel reinforcement(MPa): "))
webLengthOfSection = int(input("web length of the section(mm): "))
effectiveDepth = int(input("effective depth(mm): "))
clearCover = int(input("clear cover(mm):"))
diameterOfTensionSteel = int(input("diameter of the tension steel reinforcement(mm): "))
diameterOfCompressionSteel = int(input("diameter of the compression steel reinforcement(mm): "))
numberOfTensionSteel = int(input("number of tension steel reinforcement bars: "))
numberOfCompressionSteel = int(input("number of compression steel reinforcement bars: "))

tensionSteelArea = Area(diameterOfTensionSteel, numberOfCompressionSteel)
