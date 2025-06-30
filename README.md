# HTML5 Picture Element Sample

This repository demonstrates the use of the HTML5 `<picture>` element to serve responsive images in multiple formats (AVIF, WebP, JPEG) across different screen resolutions and .

🔗 **Live Demo**: [https://luzfcb.github.io/html5\_picture\_element\_sample](https://luzfcb.github.io/html5_picture_element_sample)


### Example of use of `<picture>` element with responsive images via media query and multiple formats and multiple DPR (Device pixel ratio)<

Ordering absolutely matters. Always list your `<source>` elements from most specific (highest resolution and preferred formats) to least specific (fallbacks).

The browser walks through the `<source>` elements in document order and picks the first one where both the media condition (if present)
matches and the type is supported. If you flip the order of your sources, you risk e.g. matching the “small” fallback
before your “verylarge” or “large” queries, so even on a 1440px‐wide viewport the browser might pick your smaller image.


```html

  <picture>
    <!-- Very large images for extra-wide viewports -->
    <source
      media="(min-width: 1440px)"
      type="image/avif"
      srcset="images/image-verylarge.avif 1x, images/image-verylarge@2x.avif 2x">
    <source
      media="(min-width: 1440px)"
      type="image/webp"
      srcset="images/image-verylarge.webp 1x, images/image-verylarge@2x.webp 2x">
    <source
      media="(min-width: 1440px)"
      type="image/jpeg"
      srcset="images/image-verylarge.jpg 1x, images/image-verylarge@2x.jpg 2x">

    <!-- High-resolution images for wide viewports -->
    <source
      media="(min-width: 800px)"
      type="image/avif"
      srcset="images/image-large.avif 1x, images/image-large@2x.avif 2x">
    <source
      media="(min-width: 800px)"
      type="image/webp"
      srcset="images/image-large.webp 1x, images/image-large@2x.webp 2x">
    <source
      media="(min-width: 800px)"
      type="image/jpeg"
      srcset="images/image-large.jpg 1x, images/image-large@2x.jpg 2x">

    <!-- Medium-resolution images for mid-sized viewports -->
    <source
      media="(min-width: 400px) and (max-width: 799px)"
      type="image/avif"
      srcset="images/image-medium.avif 1x, images/image-medium@2x.avif 2x">
    <source
      media="(min-width: 400px) and (max-width: 799px)"
      type="image/webp"
      srcset="images/image-medium.webp 1x, images/image-medium@2x.webp 2x">
    <source
      media="(min-width: 400px) and (max-width: 799px)"
      type="image/jpeg"
      srcset="images/image-medium.jpg 1x, images/image-medium@2x.jpg 2x">

    <!-- Low-resolution images as default fallback -->
    <source
      type="image/avif"
      srcset="images/image-small.avif 1x, images/image-small@2x.avif 2x">
    <source
      type="image/webp"
      srcset="images/image-small.webp 1x, images/image-small@2x.webp 2x">
    <source
      type="image/jpeg"
      srcset="images/image-small.jpg 1x, images/image-small@2x.jpg 2x">

    <!-- fallback image -->
    <img
      src="images/image-small.jpg"
      srcset="images/image-small.jpg 1x, images/image-small@2x.jpg 2x"
      sizes="(max-width: 400px) 100vw, (max-width: 800px) 50vw, (max-width: 1440px) 33vw, 1440px"
      alt="Example of use of picture element with responsive images via media query and multiple formats and multiple Device pixel ratio (DPR)">
  </picture>


```



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
