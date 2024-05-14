#include <stdio.h>
#include <string.h>

void fonction_vulnerable(char *input) {
    char tampon[50];
    strcpy(tampon, input); // Copie sans vérification de la longueur
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Utilisation: %s <input>\n", argv[0]);
        return 1;
    }
    fonction_vulnerable(argv[1]);
    printf("Terminé\n");
    return 0;
}
