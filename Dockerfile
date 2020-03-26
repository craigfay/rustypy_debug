FROM rust:latest

# Update Package Manager
RUN apt update

# Install Python
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install python3.7 -y

# Install Pip
RUN apt install python3-pip -y

# Install Rustypy
RUN pip3 install rustypy

