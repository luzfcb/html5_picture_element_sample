# HTML5 Picture Element Sample

This repository demonstrates the use of the HTML5 `<picture>` element to serve responsive images in multiple formats (AVIF, WebP, JPEG) across different screen resolutions and .

🔗 **Live Demo**: [https://luzfcb.github.io/html5\_picture\_element\_sample](https://luzfcb.github.io/html5_picture_element_sample)


Learn more:

https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture

https://www.w3schools.com/html/html_images_picture.asp

https://caniuse.com/picture

https://www.caniemail.com/features/html-picture/

https://dev.to/technoph1le/the-html-element-explained-48o8

## Files

* `index.html`
  Comprehensive example of `<picture>` with breakpoints for **verylarge** (1440px+), **large**, **medium**, and **small** screens.

* `images/`
  Auto-generated sample images at 1× and 2× densities in AVIF, WebP, and JPEG formats.

* `gen.py`
  Python script (using `pillow-avif-plugin` and Roboto Bold) to regenerate the `images/` folder with correctly sized and labeled placeholders.

## Getting Started

1. Clone this repo:

   ```bash
   git clone https://github.com/luzfcb/html5_picture_element_sample.git
   cd html5_picture_element_sample
   ```

2. Generate images:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install Pillow pillow-avif-plugin
   python3 gen.py
   ```

3. Open `index.html` in your browser or serve with any static file server:

   ```bash
   # Example: using Python's built-in server
   python3 -m http.server 8000
   open http://localhost:8000/index.html
   ```

## License

[MIT](LICENSE)
