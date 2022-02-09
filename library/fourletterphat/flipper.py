def flipbitmask(bitmask):
    """Flips the given bitmask:
    If the screen looks like _
                            |_|
                            | |

    Then this will create a bitmask that shows:
                            |_|
                            |_|
    
    Arguments:
        bitmask {int} -- the bitmask to flip
    """
    flippedmasks = [
        0b0000000000001001, # top and bottom LED                         *
        0b0000000000110000, # top and bottom left LED                    *
        0b0000000000000110, # top and bottom right LED                   *
        0b0000000000100010, # top left and right LED                     *
        0b0000000000010100, # bottom left and right LED                  *
        0b0000000011000000, # middle horizontal left and right LED       *
        0b0000110000000000, # top right and bottom left diagonal LED     *
        0b0010000100000000, # top left and bottom right diagonal LED     *
        0b0001001000000000, # vertical top and bottom LED                *
    ]

    for flippedmask in flippedmasks:
        bitmask = flipped(bitmask, flippedmask)

    return bitmask

def flipped(bitmask, flipmask):
    """
    This function takes a flipmask, determines whether to apply it to a
    given bitmask, and determines if the resulting flipped letter is
    correct.

    Let's walk through an example with the letter "A":

    We start by XORing "A" with the flipmask passed to the function. In
    this case it's 0b0000000000001001, the flipmask for the top and
    bottom LED.

    0b0000000011110111 < "A"
    XOR
    0b0000000000001001 < " ͞_ " (flipmask for top and bottom)
    ------------------
    0b0000000011111110 < "∀" We have successfully flipped the top and
            |                bottom LEDs.
            |
            |
            V                Now we apply the next flipmask to the
    0b0000000011111110 < "∀" result from above.
    XOR
    0b0000000000110000 < "| |" (flipmask for top left and right)
    ------------------
    0b0000000011001110 < Error, we've lost those 2 bits. We need to
                         check first if we lose any information.

    How do we check if we lose any information? And! By "and"ing the
    resulting flipped bitmask with the flipmask we can see if we lost
    our original bits. If the "&" result is 0, we know our resulting
    flipped bitmask has nothing in common with the flipmask, meaning
    we've erased some data.

    0b0000000011001110 (result) & 0b0000000000110000 (flipmask) = 0

    0b0000000011111110 < "∀" Now let's apply the next flipmask
    XOR                
    0b0000110000000000 < "/" (top right and bottom left diagonal)
    ------------------
    0b0000110011111110 < Error, we've added 2 bits. We need a way to
                         check if we're adding any data.

    How do we check if we're adding data? And! By "and"ing the bitmask
    with its flipmask we can see exactly how much data we're adding.
    If the flipmask is valid for a given letter, "and"ing it with that
    letter will create a bitmask that is greater than 0. If it's equal
    to 0 we've got a flipmask that has nothing in common with our
    bitmask.

    0b0000000011111110 < "∀"
    AND
    0b0000110000000000 < "/"
    ------------------
    0b0                < We know we shouldn't apply this flipmask. Leave
                         our bitmask alone.

    So the final algorithm to check if a given flipmask is valid is:

    if (bitmask & flipmask != 0) and (flipped_result & flipmask != 0)

    Args:
        bitmask (int): The bitmask to apply the flipmask
        flipmask (int): The flipmask to apply against the bitmask

    Returns:
        int: The "flipped" result
    """
    flipped_result = bitmask ^ flipmask

    if (bitmask & flipmask != 0) and (flipped_result & flipmask != 0):
        return flipped_result
    return bitmask
