import numpy as np
import psutil
import time
def bench(combination):
    # Tamanho da matriz
    n = 6000

    # Obtenha o número de núcleos da CPU
    # num_cores = psutil.cpu_count()

    # Crie uma lista com os IDs dos núcleos
    # cores = list(range(num_cores))

    # Loop infinito para estressar a CPU
    while True:
        # Alterne para o próximo núcleo
        core_ids = combination.pop(0)
        # cores.append(core)
        print(core_ids)
        p = psutil.Process()
        p.cpu_affinity([core_ids])  # Defina o número do núcleo que você deseja estressar aqui

        # Obtenha a carga atual do núcleo
        load = psutil.cpu_percent(interval=0.1, percpu=True)[core_ids]

        # Se a carga for menor que 50%, estresse o núcleo com AVX2
        if load < 50:
            # Crie uma matriz aleatória com valores entre 0 e 1
            a = np.random.rand(n, n)

            # Realize uma operação de matriz usando AVX2
            b = np.dot(a, a.T)

        # Espere um segundo antes de alternar para o próximo núcleo
        time.sleep(0.2)
