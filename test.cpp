#include <graphics.h>
#include <conio.h>

int main() {
    // Initialize graphics mode
    int gd = DETECT, gm;
    initgraph(&gd, &gm, NULL);  // Adjust path if necessary

    // Get the center of the screen
    int centerX = getmaxx() / 2;
    int centerY = getmaxy() / 2;

    // Set color and draw concentric circles
    setcolor(WHITE);
    
    // Draw concentric circles with the center at the screen's center
    for(int radius = 50; radius <= 200; radius += 25) {
        circle(centerX, centerY, radius);  // Use the dynamic center
    }

    // Pause screen
    getch();

    // Close graphics mode
    closegraph();
    
    return 0;
}
