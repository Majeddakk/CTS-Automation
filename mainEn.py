import subprocess
import os
 

 # Execute incoming save script
subprocess.run(["python", os.path.join(os.getcwd(), 'incomingEn.py')])

# Execute outgoing internal script
subprocess.run(["python", os.path.join(os.getcwd(), 'outgoing-internalEn.py')])

# Execute outgoing external script
subprocess.run(["python", os.path.join(os.getcwd(), 'outgoing-externalEn.py')])

# Execute circular save script
subprocess.run(["python", os.path.join(os.getcwd(), 'circularEn.py')])
 
# Execute circular sign script
subprocess.run(["python", os.path.join(os.getcwd(), 'circular-signEn.py')])

# Execute decree save script
subprocess.run(["python", os.path.join(os.getcwd(), 'decreeEn.py')])

# Execute decree sign script
subprocess.run(["python", os.path.join(os.getcwd(), 'decree-signEn.py')])

# Execute viewer excel script
subprocess.run(["python", os.path.join(os.getcwd(), 'viewer-excelEn.py')])

# Execute viewer pdf script
subprocess.run(["python", os.path.join(os.getcwd(), 'viewer-pdfEn.py')])

# Execute viewer word script
subprocess.run(["python", os.path.join(os.getcwd(), 'viewer-wordEn.py')])

# Execute search script
subprocess.run(["python", os.path.join(os.getcwd(), 'SearchEn.py')])

# Execute add delegation script
subprocess.run(["python", os.path.join(os.getcwd(), 'AddDelegationEn.py')])
 
# Execute admin Correspondence Management script
subprocess.run(["python", os.path.join(os.getcwd(), 'Admin-Correspondence-ManagementEn.py')])
 
# Execute admin external entities script
subprocess.run(["python", os.path.join(os.getcwd(), 'Admin-ExternalEntitiesEn.py')])
 
# Execute Admin Organization Management script
subprocess.run(["python", os.path.join(os.getcwd(), 'Admin-Organization-ManagementEn.py')])
 
# Execute circular archive script
# subprocess.run(["python", os.path.join(os.getcwd(), 'circular-archive.py')])

 


# Execute decree archive script
# subprocess.run(["python", os.path.join(os.getcwd(), 'decree-archive.py')])












print('English Test script finished')