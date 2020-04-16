# QISKIT 0.18.0 release on Docker

<p align="center">
<img src="https://github.com/sergiomtzlosa/docker-qiskit/blob/master/qubits.png?raw=true">
</p>

Qiskit is an open-source framework for quantum computing. It provides tools for creating and manipulating quantum programs and running them on prototype quantum devices on IBM Q Experience or on simulators on a local computer.

This is a docker image with Qiskit 0.18.0 including:

- Qiskit Terra 0.13.0
- Qiskit Aer 0.5.0
- Qiskit Ignis 0.3.0
- Qiskit Aqua 0.6.5
- Qiskit IBMQ Provider 0.6.0

It also has keras, matplotlib, pandas, seaborn, scikit-learn, opencv-python, tqdm, pillow, image, scipy and regex.

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

https://hub.docker.com/repository/docker/sergiomtzlosa/qiskit

Pull the image from docker hub:

```
docker pull sergiomtzlosa/qiskit:latest
```
