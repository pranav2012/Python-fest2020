# Barnsley Fern

From Wikipedia:
 > The Barnsley fern is a fractal named after the British mathematician Michael Barnsley<sup>[1][1]</sup>

## Usage

`python fern.py`

It is recommended to call the program with the `--tofile` option. Without it matplotlib will attempt to
plot the fern, but this can take a decently long time to do. With `--tofile` a data file is created that
can then be opened with `gnuplot`. To do this run `python fern.py --tofile` and then open that file with
`plot 'path/to/b-fern-py.data'`

Your output will look similar to this:
![Barnsley Fern](./b-fern.png)
This image was made with gnuplot, using 10,000 coordinates.


[1]: https://en.wikipedia.org/wiki/Barnsley_fern
