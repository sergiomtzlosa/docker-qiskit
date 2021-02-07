# QISKIT 0.23.0 release on Docker

<p align="center">
<img src="https://github.com/sergiomtzlosa/docker-qiskit/blob/master/qubits.png?raw=true">
</p>

Qiskit is an open-source framework for quantum computing. It provides tools for creating and manipulating quantum programs and running them on prototype quantum devices on IBM Q Experience or on simulators on a local computer.

This is a docker image with Qiskit 0.23.0 including:

- Qiskit Terra 0.16.0
- Qiskit Aer 0.7.0
- Qiskit Ignis 0.5.0
- Qiskit Aqua 0.8.0
- Qiskit IBMQ Provider 0.11.0
- Qiskit Textbook

It also has keras, matplotlib, pandas, seaborn, scikit-learn, opencv-python, tqdm, pillow, image, scipy, regex and kaleidoscope.

There are two environments: development and production (default)

You can change the Dockerfile on the docker-compose.yml file to switch between those environments.

The folder *qiskit-offline-docker* leads an offline installation of docker images, so you can build them on your own, but in that case you must create a Debian Buster subsystem with *debootstrap*.

```
sudo apt-get install debootstrap
sudo debootstrap buster buster http://deb.debian.org/debian && sudo tar -f rootfs-debian-buster.tar.xz -C buster -c .
```

On both Dockerfiles (dev and prod), you can set your QISKIT IBM API Key on QISKIT_API_TOKEN variable (OPTIONAL).

Run the image with docker-compose command:

```
docker-compose up
```

Inspect logs from service to get the jupyter token:

```
docker-compose logs -f qiskit-service
```

**This image exposes the jupyter notebook on port 8889: http://YOUR_IP:8889**

Default image on docker hub is production environment:

https://hub.docker.com/r/sergiomtzlosa/qiskit

Pull the image from docker hub:

```
docker pull sergiomtzlosa/qiskit:qiskit-0.23.0
```

The Dockerfile_dev file compiles QISKIT from source code, then it can be used to deploy future releases.

Use the docker-compose-yml file to start the image:

```
version: "2"
services:
  qiskit-service-0.23.0:
    image: sergiomtzlosa/qiskit:latest
    container_name: qiskit-container-0.23.0
    environment:
#      - QISKIT_API_TOKEN=
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - JUPYTER_ENABLE_LAB=yes
    volumes:
      - ./qiskit-jupyter:/home/qiskit/qiskit-jupyter
    ports:
      - 8889:8889
    restart: unless-stopped
```

From your terminal use the docker-compose.yml file:

```
docker-compose up -d
```
