# QISKIT 0.26.2 release on Docker

<p align="center">
<img src="https://github.com/sergiomtzlosa/docker-qiskit/blob/master/qubits.png?raw=true">
</p>

Qiskit is an open-source framework for quantum computing. It provides tools for creating and manipulating quantum programs and running them on prototype quantum devices on IBM Q Experience or on simulators on a local computer.

This is a docker image with Qiskit 0.26.2 including:

- Qiskit Terra 0.17.4
- Qiskit Aer 0.8.2
- Qiskit Ignis 0.6.0
- Qiskit Aqua 0.9.1
- Qiskit IBMQ Provider 0.13.1
- Qiskit Textbook
- Qiskit nature 0.1.3
- Qiskit Optimization 0.1.0
- Qiskit Finance 0.1.0
- Qiskit Machine Learning 0.1.0

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
docker-compose logs -f <CONTAINER_ID>
```

**This image exposes the jupyter notebook on port 8889: http://YOUR_IP:8889**

Default image on docker hub is production environment:

https://hub.docker.com/r/sergiomtzlosa/qiskit

Pull the image from docker hub:

```
docker pull sergiomtzlosa/qiskit:qiskit-0.26.2
```

The Dockerfile_dev file compiles QISKIT 0.26.2 releases.

Use the docker-compose.yml file to start the image:

```
version: "2"
services:
  qiskit-service-0.26.2:
    image: sergiomtzlosa/qiskit:qiskit-0.26.2
    container_name: qiskit-container-0.26.2
    environment:
#      - QISKIT_API_TOKEN=
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
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
