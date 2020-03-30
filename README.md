# Video Mender
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)  [![Codacy Badge](https://api.codacy.com/project/badge/Grade/f6ee2d6a33054c0c8f8bed556cbfdfe1)](https://www.codacy.com/manual/frgfm/video-mender?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=frgfm/video-mender&amp;utm_campaign=Badge_Grade)  ![Build Status](https://github.com/frgfm/video-mender/workflows/python-package/badge.svg) [![Docs](https://img.shields.io/badge/docs-available-blue.svg)](https://frgfm.github.io/video-mender)  

Implementation of a frame denoising and reordering algorithm for video sequences.

> The **Mending Charm**,[[1\]](https://harrypotter.fandom.com/wiki/Mending_Charm#cite_note-POT-0) also known as the **Repairing Charm**[[2\]](https://harrypotter.fandom.com/wiki/Mending_Charm#cite_note-WON-1) (*Reparo*), is a [charm](https://harrypotter.fandom.com/wiki/Charm) that can be used to seamlessly repair a broken object and works on most materials.

*Source: Harry Potter Wiki*



## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Technical Roadmap](#technical-roadmap)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)



## Getting started

### Prerequisites

- Python 3.6 (or more recent)
- [pip](https://pip.pypa.io/en/stable/)

### Installation

You can install the package as follows:

```shell
git clone https://github.com/frgfm/video-mender.git
pip install -e video-mender/.
```



## Usage

You can find an example below to process a video

```bash
python scripts/restore.py <PATH_TO_YOUR_VIDEO> --outfile <OUTPUT_FILE> --chain-denoise
```



## Technical roadmap

The project is currently under development, here are the objectives for the next releases:

- [x] Frame processing: process the video frames.
- [ ] Audio processing: use the matching performed on frames to write audio to output as well.
- [ ] Benchmark: add a benchmark of multiple methods.



## Documentation

The full package documentation is available [here](https://frgfm.github.io/video-mender/) for detailed specifications. The documentation was built with [Sphinx](sphinx-doc.org) using a [theme](github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](readthedocs.org).



## Contributing

Please refer to `CONTRIBUTING` if you wish to contribute to this project.



## Credits

This project is developed and maintained by the repo owner, but the implementation was based on the following precious papers:

- [Histogram comparison article](https://www.pyimagesearch.com/2014/07/14/3-ways-compare-histograms-using-opencv-python/): ways to compare picture histograms using OpenCV
- [Scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html): scientific computation library for python. 



## License

Distributed under the MIT License. See `LICENSE` for more information.