'''
Problem: Text Alignment
Description: Draw a HackerRank logo
with a given thickness.
Points: 10.

'''


def draw_logo(c, thickness):
    # Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    # Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) +
              (c*thickness).center(thickness*6))

    # Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    # Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2) +
              (c*thickness).center(thickness*6))

    # Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness) +
               c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


if __name__ == "__main__":
    # This must be an odd number
    t = int(input())
    char = 'H'
    draw_logo(char, t)
