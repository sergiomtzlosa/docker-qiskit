from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, execute
from qiskit.quantum_info import Statevector
import numpy as np

def get_quantum_simulator_backend(str_backend):
  
    return Aer.get_backend(str_backend)

def create_base_circuit(num_qubits):

    cr = ClassicalRegister(num_qubits, "c0")
    qr = QuantumRegister(num_qubits, "q0")

    base_circuit = QuantumCircuit(qr, cr)

    base_circuit.initialize(Statevector.from_label('1'*num_qubits).data, range(num_qubits));

    #[base_circuit.initialize([0, 1], i) for i in range(num_qubits)];
    
    return base_circuit

def splitting_chunks(n_cols, num_qubits):

    chunk_split = num_qubits

    num_splitting = int(n_cols / chunk_split) + (1 if int(n_cols % chunk_split) > 0 else 0)
    
    return num_splitting

def create_circuits(n_circuits, num_qubits):
    
    circuits = []

    for i in range(n_circuits):
        circuits.append(create_base_circuit(num_qubits))
        
    return circuits

def split_str(s):
    
    array = [ch for ch in s]
    
    return array

def rework_result_count(counts):

    result_value = [key for key, val in sorted(counts.items(), key = lambda ele: ele[1], reverse = True)]

    reverse_val = result_value[0][::-1]
    
    return reverse_val
    
def apply_gate(circuit, row, num_qubits):
    
    zeros = np.where(row == 0)
    zeros = zeros[0]

    circuit.barrier()
    
    if np.size(zeros) > 0:
        circuit.x(zeros.tolist())
    else:
        circuit.id(list(range(num_qubits)))
        
    circuit.measure(range(num_qubits), range(num_qubits))
    
    return circuit

def rebuild_image_quantum(binary_data, cols_items, splitting, num_qubits, backend, num_shots=1):
    
    final_array = []

    for item in binary_data:

        row_value = ''

        step = 0

        circ_copy = create_circuits(splitting, num_qubits)

        for circuit in circ_copy: 

            temp_step = step + num_qubits
            long_step = temp_step

            if long_step >= cols_items:

                long_step = cols_items

            chunk = item[step:long_step]

            apply_circuit = apply_gate(circuit, chunk, num_qubits)

            sim_counts = execute(circuit, backend=backend, shots=num_shots).result().get_counts()

            row_value = row_value + rework_result_count(sim_counts)

            if temp_step >= cols_items:

                diff = temp_step - cols_items

                row_value = row_value[:-diff]

            else:

                step = step + num_qubits

        array_row = split_str(row_value)

        final_array.append(array_row)

    rework_data = np.array(final_array, dtype='uint8')
    
    return rework_data