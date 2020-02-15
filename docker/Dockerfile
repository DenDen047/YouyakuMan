FROM pytorch/pytorch

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -U pip
RUN pip install -r requirements.txt
