# fciqstreamer

After creating dovesnapsdr network:

$ docker build -f Dockerfile.fcm_iq_streamer . -t anarkiwi/fciqstreamer
$ docker run --privileged --net=dovesnapsdr -t anarkiwi/fciqstreamer

Get IP address of container from docker inspect.

Start gqrx, connect to RTL IQ server <IP>:1234, 192k sample rate.
