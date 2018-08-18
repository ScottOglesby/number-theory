"""
Runs a particular coin-flip experiment and collects results.

Flip a coin up to N times in a row.
Heads is a "win"; tails is a "loss".
You can keep going until N flips _or_ you have more losses than wins.
What is your expected value of wins?
(meaning, the probability-weighted average of all possible outcomes)

As it turns out, the solution relates to a number sequence
listed at https://oeis.org/A189391: "The minimum possible value
for the apex of a triangle of numbers whose base consists of
a permutation of the numbers 0 to n, and each number in a higher row
is the sum of the two numbers directly below it."

I believe the complexity of this algorithm is, unfortunately, O(2^n).
"""

debug = True
run_count = 16  # how many runs (and max length of last run)
results = []    # track results of each run


def win_count(record):
    return record.count('W')


def loss_count(record):
    return record.count('L')


def win_percentage(record):
    wins = win_count(record)
    losses = loss_count(record)
    return wins / (wins + losses)


def printable_record(record):
    return "{}-{}".format(win_count(record), loss_count(record))


def print_debug(message, record):
    print("{}: {} {}".format(message,
                             ''.join(record),
                             printable_record(record)))


def make_a_flip(max_length):
    """
    Creates a flip function limited to max_length coin flips.
    Fortunately, recursion works fine with closures.
    :param max_length: stop if you've flipped this many times
    """
    def flip(record):
        """
        Clone the current sequence and extend it twice: once with
        a win, and once with a loss.
        Operates on global results list.
        :param record: current sequence of wins and losses
        """
        if len(record) > 0 and win_percentage(record) < 0.5:
            if debug:
                print_debug("lost", record)
            results.append(record)
            return
        if len(record) >= max_length:
            if debug:
                print_debug("ended", record)
            results.append(record)
            return
        flip(record + ['W'])
        flip(record + ['L'])
        
    return flip


# run simulation ("season") multiple times, incrementing length after each
for length in range(1, run_count+1):
    season = make_a_flip(length)
    results = []
    season([])
    win_probability = 0
    for result in results:
        win_probability += win_count(result) / (2**len(result))

    # express win probability as a fraction (shows A189391 series)
    denom = pow(2, length)
    numer = int(win_probability * denom)
    print("max flips: {:2d}; expected wins: {:.4f} ({} / {})".format(
        length, win_probability, numer, denom))

