#HHA504 - Assignment 3: Multi‑Cloud Serverless Function (Fasting Glucose)
The purpose of this assignment is to implement the same HTTP serverless function in at least two cloud platforms, which I have chosen Google Cloud (Cloud Run Functions) and Microsoft Azure (Azure Functions). My function will accept JSON input describing one laboratory value that I choose, fasting glucose. I will be implementing a binary classifier that returns normal or abnormal based on a published reference range or clinical cut-point cited.

##Lab Rules for fasting glucose:
- < 100: normal
- >= 100 & <= 125: prediabetes
- >= 126: diabetes

###Plain English:
- Less than 100 mg/dL: This is a normal fasting blood sugar level.
- 100 to 125 mg/dL: Fasting blood sugar in this range indicates prediabetes which means your blood sugar levels are higher than normal but not high enough to be classified as diabetes.
- 126 mg/dL or above: This indicates high blood sugar and enough to be classified as diabetes.

Citation: https://my.clevelandclinic.org/health/diagnostics/21952-fasting-blood-sugar

##Zoom Recordings:
- GCP:
- Azure:

##GCP:
Endpoint URLs: https://python-fg-504-382156928436.europe-west1.run.app

##Azure:
Endpoint URLs: https://python-test-fg-cpeacta4ftfwgefu.canadacentral-01.azurewebsites.net 

##Compare: