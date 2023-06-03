FROM python:3.10

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libsm6 \
    libxext6 \
    libxrender-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Build and install dlib from source
RUN git clone https://github.com/davisking/dlib.git
WORKDIR /app/dlib
RUN mkdir build
WORKDIR /app/dlib/build
RUN cmake ..
RUN cmake --build . --config Release
RUN make install
RUN ldconfig

# Reset working directory
WORKDIR /app

COPY . .

CMD [ "python", "app.py" ]
