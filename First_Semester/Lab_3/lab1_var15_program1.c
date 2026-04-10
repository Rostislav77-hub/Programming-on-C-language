#include <stdio.h>
#include <unistd.h>

#define WIDTH 80
#define DELAY 20000 
#define TOP_ROW 4
#define BOT_ROW 21
#define BODY_CHAR "#"
#define BACK_CHAR "*"

void gotoxy(int x, int y) {
    printf("\033[%d;%dH", y, x);
}

void fill_background() {
    for (int y = TOP_ROW; y <= BOT_ROW; y++) {
        for (int x = 1; x <= WIDTH; x++) {
            gotoxy(x, y);
            printf("%s", BACK_CHAR);
        }
    }
    fflush(stdout);
}

void draw_step(int x, int top, int bot) {
    gotoxy(x, top);
    printf("\033[7m \033[0m");

    fflush(stdout);
    usleep(DELAY);

    gotoxy(x, top);
    printf("%s", BODY_CHAR);

    gotoxy(x, bot);
    printf("%s", BODY_CHAR);

    fflush(stdout);
}

int main() {
    printf("\033[2J");
    printf("\033[?25l");

    fill_background();

    int top = TOP_ROW;
    int bot = BOT_ROW;

    while (top < bot) {
        for (int x = WIDTH; x >= 1; x--) {
            draw_step(x, top, bot);
        }

        top++;
        bot--;
        if (top > bot) break;

        draw_step(1, top, bot);

        for (int x = 2; x <= WIDTH; x++) {
            draw_step(x, top, bot);
        }

        top++;
        bot--;
        if (top > bot) break;

        draw_step(WIDTH, top, bot);
    }

    printf("\033[?25h");
    gotoxy(1, 23);
    printf("\n");

    return 0;
}