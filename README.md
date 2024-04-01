# The drunk guy on a bride problem

Matthieu Hanania

## The problem
A drunk guy is on the 17th meter of a 100m bridge, every step he has a 1/2 probability of going left, and 1/2 of going right. If he reaches 0m or 100m he falls off the bridge and dies.

## Questions
1) What's the probability of him reaching 100m and falling?
2) How long will it take him to fall off the bridge, on average? 


## Simulation

To respond the question, we process to experimental simulation of 100.000 drunked with 2.000, 3.000, 5.000, 8.000,10.000 and 20.000 max steps per person.
The greater the maximum number of steps is, the number of survivors will be important and so the probability of reaching 100m and falling.

### Results
| max steps per drunked | % of falling at 100 meters  | % of falling at 0 meters | sum of falling percents | time (s) | mean steps to fall |
|-----------------------|---------------------------------|------------------------------------|------------------|----------|-------|
| 2000                  | 5.4                             | 70.53                              | 75.93            | 45.5     |966    |
| 3000                  | 9.66                            | 75.73                              | 85.4             | 56.9     |1253   |
| 5000                  | 14.29                           | 80.33                              | 94.62            | 63.6     |1665   |
| 8000                  | 16.35                           | 82.36                              | 98.71            | 67.4     |1970   |
| 10000                 | 16.83                           | 82.69                              | 99.52            | 70.7     |2068   |
| 15000                 | 16.85                           | 83.15                              | 99.95            | 66.9     |2128   |
| 20000                 | 17.26                           | 82.74                              | 100.00           | 69.6     |2136   |

For repondong to the questions, we take our results of the 20.000 steps simulation
1) The probability of falling at 100m is 17.26%
2) With a maximal number of steps per drunks, the average number of steps leading to the fall is 2136 steps

### Graphical representation
![A graphical representation of %chance of falling to the left per max steps](figure.png)


## Mathematical approach

With a propriety of the markov's chains, we can describe this problem as a numerical serie:
$$P_n = \frac{1}{2}P_{n-1} + \frac{1}{2}P_{n+1}$$
$$<=>$$
$$0 = -\frac{1}{2} P_{n-1} + 0 \cdot P_n + \frac{1}{2} P_{n+1}$$
This simplies to
$$P_{n+1} - 2P_n + P_{n-1} =0 $$

This forms has a characteristic equation:
$$x^2 - 2x + 1 = 0$$

The discriminant of this quadratic equation is:
$$\Delta = 2^2 - 4 \cdot 1 \cdot 1 = 4 - 4 = 0$$
Thus, $$x = \frac{2}{2} - 1 = 1$$

It follows that the general solution is of the form:
$$u_n = (\lambda + \mu \cdot x^n) \cdot x^n$$

The probability at the position 0 to then fall at the position 100 is null, because 0 is also a end position.  
We use  $$u_0 = 0$$ and $$u_{100} = 1$$

Then, If `n = 0`:
$$u_0 = (\lambda + \mu \cdot 0) \cdot 1^0 \Rightarrow \lambda = 0$$

If `n = 100`, then:
$$u_{100} = (\lambda + \mu \cdot 100) \cdot 1^{100} \Rightarrow 100\mu = 1 <=> \mu = \frac{1}{100}$$

Finally,  the probability of falling at position 100 if we are at position `n` is:
$$u_n = \frac{n}{100}$$








