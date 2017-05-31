## About
Simple [Gambler's Ruin](https://en.wikipedia.org/wiki/Gambler%27s_ruin) simulator written in our good friend `Python`.

## Installation
```
git clone https://github.com/RagingTiger/GamblersRuin.git && cd GamblersRuin
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```
gamble [-mi] <games> <sets>
gamble [-m] (-i)
```

## Example
### Basic: Instance Mode
The first example shows the use of the `-m` matrix flag to display the
wins/losses matrix for the sets of games:
```
$ python gamble.py -m 10 10

[[ 1.  0.  0.  0.  1.  0.  1.  1.  1.  0.]
 [ 1.  1.  0.  1.  1.  0.  1.  0.  1.  0.]
 [ 1.  0.  0.  0.  0.  0.  0.  1.  0.  0.]
 [ 0.  1.  0.  1.  1.  1.  0.  1.  1.  1.]
 [ 0.  1.  1.  1.  0.  0.  1.  1.  1.  0.]
 [ 1.  0.  1.  1.  0.  0.  0.  0.  0.  1.]
 [ 0.  1.  1.  1.  1.  1.  0.  1.  1.  1.]
 [ 0.  1.  0.  0.  1.  0.  0.  0.  1.  0.]
 [ 0.  0.  1.  1.  1.  0.  1.  1.  0.  0.]
 [ 1.  1.  0.  1.  0.  1.  0.  0.  0.  1.]]

Wins = 51
Losses = 49
Percentage Wins = 51.0%
Percentage Edge = 1.0%
```

To only show the wins/losses information, run without `-m` flag:
```
$ python gamble.py 100 100
Wins = 4944
Losses = 5056
Percentage Wins = 49.44%
Percentage Edge = -0.56%
```

### Advanced: Interactive Mode
Whereas the basic usage is only single instances with no saved state, the
advanced usage drops into an interactive interpreter that saves state between
sets of games. For example:
```
$ python gamble.py -i 10 10
> run
Wins = 38
Losses = 62
Percentage Wins = 38.0%
Percentage Edge = -12.0%

> total
Total Wins = 38
Total Losses = 62
Total Percentage Wins = 38.0%
Total Percentage Edge = -12.0%

> run
Wins = 53
Losses = 47
Percentage Wins = 53.0%
Percentage Edge = 3.0%

> total
Total Wins = 91
Total Losses = 109
Total Percentage Wins = 45.5%
Total Percentage Edge = -4.5%
```

Here we called the program with the `-i` interactive flag, which dropped us
into an interactive session where we typed the commands `run` and `total`. The
`run` command took our previous command line arguments and executed the
simulation using these arguments as inputs. The `total` command just lets us
see the current running totals for wins, losses, percent wins, and precent edge.

The next usage example introduces more features:
```
$ python gamble.py -im
> run 5 1

[[ 0.  1.  0.  0.  1.]]

Wins = 2
Losses = 3
Percentage Wins = 40.0%
Percentage Edge = -10.0%

> run

[[ 0.  0.  0.  0.  0.]]

Wins = 0
Losses = 5
Percentage Wins = 0.0%
Percentage Edge = -50.0%

> total
Total Wins = 2
Total Losses = 8
Total Percentage Wins = 20.0%
Total Percentage Edge = -30.0%

> matrix
> run
Wins = 2
Losses = 3
Percentage Wins = 40.0%
Percentage Edge = -10.0%
```

The `-m` flag at the command line turns on matrix printing, so the wins/losses
matrix will be printed out with the results. Also, no `<games> <sets>`
arguments were passed from the command line, so the `run` command required these
arguments in the first call of `run`, but stores them so subsequent
calls will use the previous arguments by simply typing `run`. Finally, the
`matrix` command will cycle on/off the printing of the matrix.

## ToDo
1. Implement tab completion
2. Finish help entry for 'run'
3. Fix total division by zero
