#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool verifier_credentials(const char *username, const char *password) {
    // Ici, pour l'exemple, les credentials sont codés en dur.
    // Dans une application réelle, ces informations seraient sécurisées et stockées différemment.
    return strcmp(username, "admin") == 0 && strcmp(password, "password123") == 0;
}

int main() {
    char username[256];
    char password[256];

    printf("Nom d'utilisateur: ");
    scanf("%255s", username);
    printf("Mot de passe: ");
    scanf("%255s", password);

    if (verifier_credentials(username, password)) {
        printf("Accès autorisé.\n");
    } else {
        printf("Accès refusé.\n");
    }

    return 0;
}