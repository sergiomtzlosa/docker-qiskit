#!/usr/bin/env python
# coding: utf-8

import re

def write_docker_file(filename, contents):
    with open(filename, 'w') as file:
        file.write(contents)

def open_file(file_path):
    file = open(file_path, "r")
    contents = file.read()
    file.close()

    return contents

def replace_dockerfile_versions(versions, file_contents):

    if len(versions) != 10:
        return file_contents

    file_contents = re.sub(r"(?<=QISKIT_RELEASE=).*", versions[0], file_contents)
    file_contents = re.sub(r"(?<=QISKIT_TERRA_RELEASE=).*", versions[1], file_contents)
    file_contents = re.sub(r"(?<=QISKIT_AER_RELEASE=).*", versions[2], file_contents)
    file_contents = re.sub(r"(?<=QISKIT_IGNIS_RELEASE=).*", versions[3], file_contents)
    file_contents = re.sub(r"(?<=QISKIT_AQUA_RELEASE=).*", versions[4], file_contents)
    file_contents = re.sub(r"(?<=QISKIT_IBMQ_RELEASE=).*", versions[5], file_contents)
    file_contents = re.sub(r"(?<=QISKIT_NATURE_RELEASE=).*", versions[6], file_contents)
    file_contents = re.sub(r"(?<=QISKIT_ML_RELEASE=).*", versions[7], file_contents)
    file_contents = re.sub(r"(?<=QISKIT_OPTIMIZATION_RELEASE=).*", versions[8], file_contents)
    file_contents = re.sub(r"(?<=QISKIT_FINANCE_RELEASE=).*", versions[9], file_contents)

    return file_contents

def replace_compose_versions(new_release, file_contents):

    if not new_release:
        return file_contents

    file_contents = re.sub(r"(?<=qiskit-service-).*", new_release, file_contents)
    file_contents = re.sub(r"(?<=image: qiskit-).*", new_release, file_contents)
    file_contents = re.sub(r"(?<=qiskit-container-).*", new_release, file_contents)

    return file_contents

def get_new_versions():

    versions_replace = open_file("rolling_version.txt")

    qiskit_release = re.findall(r"(?<=QISKIT_RELEASE=).*", versions_replace)[0]
    terra_release = re.findall(r"(?<=QISKIT_TERRA_RELEASE=).*", versions_replace)[0]
    aer_release = re.findall(r"(?<=QISKIT_AER_RELEASE=).*", versions_replace)[0]
    ignis_release = re.findall(r"(?<=QISKIT_IGNIS_RELEASE=).*", versions_replace)[0]
    aqua_release = re.findall(r"(?<=QISKIT_AQUA_RELEASE=).*", versions_replace)[0]
    ibmq_release = re.findall(r"(?<=QISKIT_IBMQ_RELEASE=).*", versions_replace)[0]
    nature_release = re.findall(r"(?<=QISKIT_NATURE_RELEASE=).*", versions_replace)[0]
    ml_release = re.findall(r"(?<=QISKIT_ML_RELEASE=).*", versions_replace)[0]
    optimization_release = re.findall(r"(?<=QISKIT_OPTIMIZATION_RELEASE=).*", versions_replace)[0]
    finance_release = re.findall(r"(?<=QISKIT_FINANCE_RELEASE=).*", versions_replace)[0]

    versions_array = [qiskit_release, terra_release, aer_release,
                      ignis_release, aqua_release, ibmq_release,
                      nature_release, ml_release, optimization_release, finance_release]

    return versions_array

def replace_version_docker_file(file_name):

    main_contents = open_file(file_name)
    new_versions = get_new_versions()
    new_contens = replace_dockerfile_versions(new_versions, main_contents)

    return new_contens

def replace_version_composer_file(file_name):

    compose_contents = open_file(file_name)
    new_versions = get_new_versions()
    new_contens = replace_compose_versions(new_versions[0], compose_contents)

    return new_contens

replace_file = "Dockerfile_prod"
new_contents = replace_version_docker_file(replace_file)

replace_file_offine = "./qiskit-offline-docker/prod/Dockerfile_prod"
new_contents_offline = replace_version_docker_file(replace_file_offine)

replace_compose = "docker-compose.yml"
new_composer = replace_version_composer_file(replace_compose)

#print(new_composer)

write_docker_file(replace_file, new_contents)
write_docker_file(replace_file_offine, new_contents_offline)
write_docker_file(replace_compose, new_composer)

print("Dockerfile QISKIT release files updated!")
