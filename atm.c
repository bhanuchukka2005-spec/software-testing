#include <stdio.h>
#include <string.h>

int main() {

    char correctPIN[] = "1234";
    char inputPIN[10];

    int attempts = 0;
    int state = 0;

    // state 0 = Card Inserted
    // state 1 = Transaction Allowed
    // state 2 = Blocked

    while (attempts < 3 && state == 0) {

        printf("Enter PIN: ");
        scanf("%s", inputPIN);

        if (strcmp(inputPIN, correctPIN) == 0) {

            state = 1;
            break;

        } else {

            attempts++;
            printf("Incorrect PIN. Attempt %d of 3.\n",
                   attempts);
        }
    }

    if (state == 1)
        printf("Transaction Allowed.\n");
    else
        printf("Card Blocked due to 3 wrong attempts.\n");

    return 0;
}