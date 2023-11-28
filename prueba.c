#include <stdio.h>

int main() {
    char firstString[50];
    char secondString[50];

    // Read the first string
    printf("Enter the first string: ");
    scanf("%s", firstString);

    // Read the second string
    printf("Enter the second string: ");
    scanf("%s", secondString);

    // Display the entered strings
    printf("You entered:\n");
    printf("First string: %s\n", firstString);
    printf("Second string: %s\n", secondString);

    return 0;
}

