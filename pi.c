#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <math.h>

// Función para aproximar pi usando la serie de Leibniz
double leibniz(int n) {
    double pi = 0.0;
    for (int i = 0; i < n; i++) {
        pi += pow(-1.0, i) / (2.0 * i + 1.0);
    }
    pi *= 4.0;
    return pi;
}

// Función para aproximar pi usando la serie de Gregory-Leibniz
double gregory_leibniz(int n) {
    double pi = 0.0;
    for (int i = 0; i < n; i++) {
        pi += pow(-1.0, i) / (2.0 * i + 1.0);
    }
    pi *= 4.0;
    return pi;
}

int main() {
    int N = 100;  // Número de términos a aproximar
    int shmid;
    key_t key = 1234;
    int *shm;
    pid_t pid1, pid2;
    int status;

    // Crea un bloque de memoria compartida de tamaño entero
    shmid = shmget(key, sizeof(int), IPC_CREAT | 0666);
    if (shmid < 0) {
        perror("shmget");
        exit(1);
    }

    // Conecta el bloque de memoria compartida a este proceso
    shm = (int*)shmat(shmid, NULL, 0);
    if (shm == (int*)-1) {
        perror("shmat");
        exit(1);
    }

    // Guarda el número de términos en la memoria compartida
    *shm = N;

    // Crea dos procesos hijos para aproximar pi con dos series distintas
    pid1 = fork();
    if (pid1 == 0) {
        // Proceso hijo 1
        double pi = leibniz(N);
        for (int i = 0; i < N; i++) {
            shm[i+1] = pow(-1.0, i) / (2.0 * i + 1.0) * 4.0;
        }
        exit(0);
    } else if (pid1 < 0) {
        // Error al crear el proceso hijo 1
        perror("fork");
        exit(1);
    } else {
        pid2 = fork();
        if (pid2 == 0) {
            // Proceso hijo 2
            double pi = gregory_leibniz(N);
            for (int i = 0; i < N; i++) {
                shm[i+1] = pow(-1.0, i) / (2.0 * i + 1.0) * 4.0;
            }
            exit(0);
        } else if (pid2 < 0) {
            // Error al crear el proceso hijo 2
            perror("fork");
            exit(1);
        }
    }

       // Esperar a que los dos hijos terminen
    waitpid(pid1, &status, 0);
    waitpid(pid2, &status, 0);

    // Lee los términos de la memoria
    double *shm;
    shm = (double *) shmat(shmid, NULL, 0);
    int N = *shm;

    // Muestra las aproximaciones de pi
    printf("Pi approximation using Gregory-Leibniz series:\n");
    for (int i = 1; i <= N; i++) {
        printf("%f ", shm[i]);
    }
    printf("\n");

    printf("Pi approximation using Nilakantha series:\n");
    for (int i = N + 1; i <= 2 * N + 1; i++) {
        printf("%f ", shm[i]);
    }
    printf("\n");

    // Desasociar la memoria compartida
    shmdt(shm);

    // Eliminar la memoria compartida
    shmctl(shmid, IPC_RMID, NULL);

    return 0;
}
