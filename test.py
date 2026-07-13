
#Test to draw Confusion Matrix


# from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
# import matplotlib.pyplot as plt

# # Your data:
# y_true = [0, 1, 0, 1, 1, 0] # Actual Labels
# y_pred = [0, 1, 1, 1, 0, 0] # Predicted Labels

# cm = confusion_matrix(y_true, y_pred)
# disp = ConfusionMatrixDisplay(confusion_matrix=cm)
# disp.plot(cmap=plt.cm.Blues) # Change colormap as needed
# plt.show()



# 1. Import the library
from inference_sdk import InferenceHTTPClient

# 2. Connect to your workflow
client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="9Z1SEkwXAzXfEhziRp4E"
)

# 3. Run your workflow on an image
result = client.run_workflow(
    workspace_name="weapon-b3vyl",
    workflow_id="weapon_detection_for_final",
    images={
        "image": "YOUR_IMAGE.jpg" # Path to your image file
    },
    use_cache=True # Speeds up repeated requests
)

# 4. Get your results
print(result)
