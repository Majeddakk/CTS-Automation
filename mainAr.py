import subprocess
import os
 

 # Execute incoming save script
subprocess.run(["python", os.path.join(os.getcwd(), 'incomingAr.py')])

# Execute outgoing internal script
subprocess.run(["python", os.path.join(os.getcwd(), 'outgoing-internalAr.py')])

# Execute outgoing external script
subprocess.run(["python", os.path.join(os.getcwd(), 'outgoing-externalAr.py')])

# Execute circular save script
subprocess.run(["python", os.path.join(os.getcwd(), 'circularAr.py')])
 
# Execute circular sign script
subprocess.run(["python", os.path.join(os.getcwd(), 'circular-signAr.py')])

# Execute decree save script
subprocess.run(["python", os.path.join(os.getcwd(), 'decreeAr.py')])

# Execute decree sign script
subprocess.run(["python", os.path.join(os.getcwd(), 'decree-signAr.py')])

# Execute viewer excel script
subprocess.run(["python", os.path.join(os.getcwd(), 'viewer-excelAr.py')])

# Execute viewer pdf script
subprocess.run(["python", os.path.join(os.getcwd(), 'viewer-pdfAr.py')])

# Execute viewer word script
subprocess.run(["python", os.path.join(os.getcwd(), 'viewer-wordAr.py')])

# Execute search script
subprocess.run(["python", os.path.join(os.getcwd(), 'SearchAr.py')])

# Execute add delegation script
subprocess.run(["python", os.path.join(os.getcwd(), 'AddDelegationAr.py')])
 
# Execute admin Correspondence Management script
subprocess.run(["python", os.path.join(os.getcwd(), 'Admin-Correspondence-ManagementAr.py')])
 
# Execute admin external entities script
subprocess.run(["python", os.path.join(os.getcwd(), 'Admin-ExternalEntitiesAr.py')])
 
# Execute Admin Organization Management script
subprocess.run(["python", os.path.join(os.getcwd(), 'Admin-Organization-ManagementAr.py')])
 
# Execute circular archive script
# subprocess.run(["python", os.path.join(os.getcwd(), 'circular-archive.py')])

 


# Execute decree archive script
# subprocess.run(["python", os.path.join(os.getcwd(), 'decree-archive.py')])












print('Arabic Test script finished')