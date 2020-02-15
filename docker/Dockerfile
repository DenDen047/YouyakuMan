FROM pytorch/pytorch

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -U pip
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y \
    wget \
    libboost-all-dev \
    google-perftools \
    libgoogle-perftools-dev \
    cmake

# Juman++
# https://github.com/ku-nlp/jumanpp
# WORKDIR /tmp
# RUN wget https://github.com/ku-nlp/jumanpp/releases/download/v2.0.0-rc3/jumanpp-2.0.0-rc3.tar.xz
# RUN tar xf jumanpp-2.0.0-rc3.tar.xz
# WORKDIR /tmp/jumanpp-2.0.0-rc3
# RUN mkdir build
# WORKDIR ./build
# RUN cmake .. -DCMAKE_BUILD_TYPE=Release
# RUN make install -j8
