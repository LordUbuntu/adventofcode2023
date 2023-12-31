# Advent of Code 2023

My solutions to this year's Advent of Code

## Day 1

### Part 1

The goal is to read the first and last digit of each string, add them together, and return the total.

To do this, we:
* read each `string` in from the specified `filename`
* starting on `index` 0, we iterate over the length of `string`
  * each iteration, we get the character at the current `index`
  * if the character is a digit we record that as the 10s digit
  * otherwise we record the current digit as the 1s digit
* Thus we get the first and last digit, which we join together to make a single `number`
* Finally, we convert that string representation to an integer and add it to the `total`
* return `total`

### Part 2

This time we operate by the same principle but with a sliding window to match against substrings (number words) in addition to matching single digits. 

To do this we:
* utilize `index` to point to the start of the window
  * check if the character in `string` at `index` is a digit
    * if it is
      * record the digit like in part one and continue
    * otherwise
      * iterate over the dictionary of number words greedily (from shortest)
        * if all characters match, record the equivalent digit as in part 1
* finally, join the number, add its value to `total`, and return `total`

### Comments

Interestingly both of these solutions are single-pass.

The implementation(s) can be found in [Day 1]().



## Day 2

### Part 1

This one is trivial. We only need to check if the limits of red, green, or blue cubes
was violated at any one time (if there were any occurrences of them exceeding 12, 13,
and 14 respectively). Then we just tally the total of the id's of all games which did
not.

To do this we:
* read each line, parsing red, green, and blue `counts` along with the `id` number
  * if any `count` for any `color` exceeds its maximum
    * continue to next game
  * otherwise
    * add game `id` to `total`
* return `total`

### Part 2

This one is even easier! To find the minimum possible number of red, green, and blue
cubes in the bag, we just need to find the maximum occurrences of each. Then to
calculate the power we just do a multiply-reduce to get the product of the three, then
add that to the total!

To do this we:
* read each line and parse into
  `counts` and `id` as before
  * if any `count` for any `color` exceeds its previous maximum, update its maximum
  * calculate the power of the set of cubes using a reduce with the multiply function
  * add that to the `total`
* return `total`



## Day 3

### Part 1

This problem reminds me of the toboggan slope one! To do that we can essentially use the same logic of modulo and multiplication to represent the 2D grid as a 1D array.
One potential way to accomplish this is with a BFS of depth 1 around any digit characters. This solution might be more elegant, requiring less repeat checks than the next idea down. But its time complexity of O(V + E) may not be optimal.
Another may be to do a simple sweep, whenever we encounter a digit we add it to a queue. We use some clever 1D "matrix" maths to check the tiles directly above, below, left, and right of the current digit for any non-digit non-'.' characters. If we reach the end of a number (string of digits) without encountering any we empty the queue. If we do, then we join the digits together in the correct order (thus the queue), add that to the total, and continue with our now empty queue to the next one. This may be simpler that a BFS and be done in O(n).

The principle is basic: find all "islands" of digits, then check adjacent "tiles" for any "non-'.'" characters. Add those together. Return.

I'll take a nap and think about it...

Plan:
* sweep once across the "grid" as a string from top left to bottom right
  * if the current char is '.'
    * if the number was flagged as a part number (adjacent symbols)
      * convert queue of digits to int and add it to total
    * part number flag is false
    * empty digit queue
    * continue
  * if the current char is a digit
    * add digit to queue
  * if the current char is not a digit or '.'
    * part number flag is true
  * check adjacent tiles for current char for non-digit non-'.' char
    * if so, part number flag is true
