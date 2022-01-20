# binary-star-evolution-search

27/11/2020

Astrophysics III homework

I know the name isn't the best, but it tells what the codes do. They look for the input that would generate a desired outcome. Search was done for 3 specific conditions:
- 2 White Dwarfs with total mass over 1.4 solar masses and period below 1 day
- 2 Black Holes on orbit below 3 days
- 2 Neutron Stars with period below 8 hours (Hulse-Taylor Pulsar)

Search was done similiarily to my other project: https://github.com/piotr-trzcionkowski/binary-star-evolution-outcomes
A loop was set up that generated BSE input parameters from a defined parameter space. After each BSE calculation the script was looking for specific desired values in the output files of BSE and breaking the loop if it found them. After a wide spread search for last case and a few email exchanges with the professor, we've determined that it's unlikely for BSE to generate a Hulse-Taylor Pulsar at some point of it's calculations.

.py files have to be launched in folder with compiled BSE and the specific cases are given in names of the python executables.
