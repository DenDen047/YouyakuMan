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
RUN mkdir build
WORKDIR ./build
RUN cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr/local
RUN make
RUN make install

# for Japanese
RUN apt-get install -y locales \
    && locale-gen ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
