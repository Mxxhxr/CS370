### HW1:
> This code addresses a surgical video analysis problem by generating multivariate data and demonstrating various statistical analyses. It covers the generation of random variables, multivariate Gaussian distribution, probability integral transform, inverse transform sampling, and correlation visualization. Additionally, it extends the analysis to an online learning setting, estimating the sample correlation matrix recursively.

### HW2:
> This assignment involves training a convolutional neural network (CNN) on a small dataset of cat and dog images using PyTorch. The baseline model's performance is evaluated with ROC curves, Recall-Precision curves, and a confusion matrix. Hyperparameter optimization is done using Optuna. The dataset is then modified to create a rare event scenario, and the model is re-trained and evaluated. Finally, improvements to the rare event performance are implemented using techniques outlined in a specified paper. The entire process is documented in a Jupyter notebook, with results and observations included.

### Midterm:
> Train a ResNet-50 CNN on CIFAR-10 (excluding "ship"). Create visualizations for the first, middle, and last blocks. Explore intermediate activations, convnet filters, and class activation heatmaps. The code, implemented in TensorFlow and Keras, offers insights into how the model learns and processes images. An additional section covers transfer learning, comparing visualizations before and after fine-tuning for the "ship" class.

### UAV Tracking:
> This assignment focuses on Multi-Object Tracking (MOT) using Kalman Filters, specifically applied to drone tracking. The tasks include setting up the development environment, conducting drone object detection using deep learning models on test videos, and implementing a Kalman filter using the filterpy library to track the detected drones. The results are presented through short videos showcasing the drone's 2D trajectory and bounding box superposition using ffmpeg and OpenCV. The assignment provides hands-on experience in applying probabilistic reasoning for physical security applications.

### Final
> Explore Variational Autoencoders (VAEs) in generative modeling. Tasks include studying VAEs, implementing a 2D VAE for MNIST, and replicating key figures. The provided code showcases VAE creation, training, and evaluation with visualizations of the latent variable space and generated digit images. The final lays the groundwork for comprehending advanced generative models and their applications in various learning paradigms.
 
### Foreign Whispers Final Project
> **Multimodal Language Processing Project**
> Developed a Python API for a comprehensive language processing pipeline:
> - ***Source Videos and Closed Captions:*** Created a Python API to download videos and their closed captions from the "60 minutes" channel, focusing on the Interviews playlist.
>   
> - ***Speech to Text:*** Implemented an API to extract and transcribe audio from videos using the openai/whisper library, supporting multilingual speech recognition.
>   
> - ***Source Text to Target Text:*** Designed an API to translate English subtitles to French using non-commercial translation libraries.
>   
> - ***Target Text to Speech:*** Developed an API to convert translated text into speech, utilizing non-commercial text-to-speech libraries.
> - ***Stitching it all together***
>   
> - ***Build UI:*** Created a user-friendly UI using Hugging Face Spaces and Streamlit Spaces, accepting a YouTube video as input and producing subtitles in French.
>   
> - ***Create Project Pitch:*** Generated a 30-second video pitch, and uploaded it to YouTube.
>
> 
> **To run project:**
```
docker-compose up
```
> The captions and videos will download after execution of Python file inside Docker environment
> 
> I have stored the execution output in `docker-output.txt`
