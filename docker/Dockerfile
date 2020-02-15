FROM pytorch/pytorch

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -U pip
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y \
    wget \
    build-essential \
    cmake

# Juman++
# https://github.com/ku-nlp/jumanpp
ENV JUMANPP_VERSION 2.0.0-rc3
WORKDIR /tmp
RUN wget https://github.com/ku-nlp/jumanpp/releases/download/v${JUMANPP_VERSION}/jumanpp-${JUMANPP_VERSION}.tar.xz
RUN tar xf jumanpp-${JUMANPP_VERSION}.tar.xz
WORKDIR /tmp/jumanpp-${JUMANPP_VERSION}
RUN mkdir bld
WORKDIR ./bld
RUN cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/opt
RUN make
RUN make install -j8
