# This file is used to build the docker image for the frontend
FROM python:3.9

#Set the working directory
WORKDIR /home

#Install the requirements
COPY requirements.txt .

#Upgrade pip
RUN pip3 install --upgrade pip

#Install the requirements
RUN pip install -r requirements.txt

#Expose
EXPOSE 8080

#Copy the app.py file
COPY . .

#Start the streamlit app
CMD ["uvicorn", "haystack_api:app","--host 0.0.0.0","--port 8080"]