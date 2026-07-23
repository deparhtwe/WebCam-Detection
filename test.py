
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


# 1. Import the library
from inference_sdk import InferenceHTTPClient

# 2. Connect to your workflow


#Cloud Hosted Api

# client = InferenceHTTPClient(
#     api_url="https://serverless.roboflow.com",
#     api_key="9Z1SEkwXAzXfEhziRp4E"
# )

# result = client.run_workflow(
#     workspace_name="weapon-b3vyl",
#     workflow_id="weapon-detector-gtpsh-4rur5",
#     images={
#         "image": "h1.jpg" # Path to your image file
#     },
#     use_cache=True # Speeds up repeated requests
# )

# print(result)

# import cv2
# from inference_sdk import InferenceHTTPClient
# from inference_sdk.webrtc import WebcamSource, StreamConfig, VideoMetadata

# # Initialize client
# client = InferenceHTTPClient.init(
#     api_url="https://serverless.roboflow.com",
#     api_key="9Z1SEkwXAzXfEhziRp4E"
# )

# # Configure video source (webcam)
# source = WebcamSource(resolution=(1280, 720))

# # Configure streaming options
# config = StreamConfig(
#     # stream_output=["my_stream_output"], # Uncomment and check your stream output name
#     # data_output=["predictions"], # Uncomment and check your data output name
#     processing_timeout=3600,             # 60 minutes
#     requested_plan="webrtc-gpu-medium",  # Options: webrtc-gpu-small, webrtc-gpu-medium, webrtc-gpu-large
#     requested_region="us"                # Options: us, eu, ap
# )

# session = client.webrtc.stream(
#     source=source,
#     workflow="weapon-detector-gtpsh-4rur5",
#     workspace="weapon-b3vyl",
#     image_input="image",
#     config=config
# )

# #
# @session.on_frame
# def show_frame(frame, metadata):
#     cv2.imshow("Workflow Output", frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         session.close()

# @session.on_data()
# def on_data(data: dict, metadata: VideoMetadata):
#     print(f"Frame {metadata.frame_id}: {data}")
# session.run()





import cv2
from inference_sdk import InferenceHTTPClient
from inference_sdk.webrtc import WebcamSource, StreamConfig, VideoMetadata

# Initialize client
client = InferenceHTTPClient.init(
    api_url="https://serverless.roboflow.com",
    api_key="bYIa18HrONksHqiBvdgu"
)

# Configure video source (webcam)
source = WebcamSource(resolution=(1280, 720))

# Configure streaming options
config = StreamConfig(
    # stream_output=["my_stream_output"], # Uncomment and check your stream output name
    # data_output=["predictions"], # Uncomment and check your data output name
    processing_timeout=3600,             # 60 minutes
    requested_plan="webrtc-gpu-medium",  # Options: webrtc-gpu-small, webrtc-gpu-medium, webrtc-gpu-large
    requested_region="us"                # Options: us, eu, ap
)

# Create streaming session
session = client.webrtc.stream(
    source=source,
    workflow="fight-detection-cdebd-det6d",
    workspace="depars-workspace",
    image_input="image",
    config=config
)

# Handle incoming video frames
@session.on_frame
def show_frame(frame, metadata):
    cv2.imshow("Workflow Output", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        session.close()

# Handle prediction data via datachannel
@session.on_data()
def on_data(data: dict, metadata: VideoMetadata):
    print(f"Frame {metadata.frame_id}: {data}")

# Run the session (blocks until closed)
session.run()
