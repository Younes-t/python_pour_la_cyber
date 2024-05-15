#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>
#include <arpa/inet.h>

#define PORT 8080

bool verifier_credentials(const char *username, const char *password) {
    return strcmp(username, "admin") == 0 && strcmp(password, "password123") == 0;
}

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[1024] = {0};
    char username[256];
    char password[256];

    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("La création du socket a échoué");
        exit(EXIT_FAILURE);
    }

    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt))) {
        perror("setsockopt a échoué");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address))<0) {
        perror("Le bind a échoué");
        exit(EXIT_FAILURE);
    }

    if (listen(server_fd, 3) < 0) {
        perror("L'écoute a échoué");
        exit(EXIT_FAILURE);
    }

    printf("En attente de connexions...\n");

    while (1) {
        if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen))<0) {
            perror("L'acceptation a échoué");
            exit(EXIT_FAILURE);
        }

        read(new_socket, buffer, 1024);
        sscanf(buffer, "%s %s", username, password);

        if (verifier_credentials(username, password)) {
            send(new_socket, "Accès autorisé.\n", strlen("Accès autorisé.\n"), 0);
        } else {
            send(new_socket, "Accès refusé.\n", strlen("Accès refusé.\n"), 0);
        }

        close(new_socket);
    }

    return 0;
}