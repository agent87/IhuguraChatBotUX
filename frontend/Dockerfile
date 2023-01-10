# This file is used to build the docker image for the frontend
FROM PYTHON:3.7

#Set the working directory
WORKDIR /home

#Install the requirements
COPY requirements.txt .

#Install the requirements
RUN pip install -r requirements.txt

#Copy the app.py file
COPY . .

#Start the streamlit app
CMD ["streamlit", "run","app.py"]