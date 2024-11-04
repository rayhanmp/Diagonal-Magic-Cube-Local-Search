# Diagonal Magic Cube Local Search

Inspired by the 5x5x5 diagonal magic cube proposed by Walter Trump, we made an attempt to solve it using various local search algorithms: hill climbing, simulated annealing, and genetic algorithm. Our approach is primarily based on the algorithms presented in the book Artificial Intelligence: A Modern Approach by Stuart Russell and Peter Norvig.

<p align="center">
  <a href ="https://www.gnu.org/licenses/gpl-3.0"><img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License - GPLv3"></a>
  <img src="https://img.shields.io/badge/status-on_progress-orange" alt="Status - On Progress"></a>
</p>


## How to Use
Clone this repository by using this command:

    git clone https://github.com/rayhanmp/Diagonal-Magic-Cube-Local-Search.git

Go to the repository location:

    cd Diagonal-Magic-Cube-Local-Search

Install all the dependencies:

    pip install numpy plotly

After that, you can run the program on `main.py` and custome the parameters and algorithm used to perform local search.

    best_cube, best_state_value, states = hc_stochastic(cube, mc, 1000)


For example, you can change hc_stochastic to hc_steepest_ascent and modify the parameters accordingly.

## Technologies Used
Python 3 with Numpy and Plotly.



  ## Contributors
| NIM | Name | Contributions |
|:---:|:----:|:----:|
|13221011| Jazila Faza A. N. | visualiser, report document|
|13221055| Ahmad Hafidz A. | genetic algorithm|
|13221065| Caitleen Devina | visualiser, report document|
|18221130| Rayhan Maheswara P. | hill climbing algorithms, video player, objective function, report document (minor)|
|18321008| Jasmine Callista A. I. | simulated annealing algorithm, objective function|

## License
<a name="license"></a>
Licensed under the [GNU General Public License version 3](https://www.gnu.org/licenses/gpl-3.0) (GPLv3).


> Made for the IF3170 Artificial Intelligence course @ITB.
