SpriteBatchRender
=================

A spritesheet rendering plugin for Blender.

![Blender addon GUI](http://i.imgur.com/CtjAuz2.png)

## What it does

Renders the scene from multiple directions and saves the results in separate files.
The "front" direction is the same as Blender's front view, in other words your model
should face to the negative y direction.

Multiple frames can be rendered. The animation frame range is read from the regular
`Start Frame` and `End Frame` rendering properties.

### Example output
![Rotating bear animation](http://i.imgur.com/M4dFeMv.gif)

## Usage

Set your camera (called `Camera`) to track an object placed at the origo. 
Place your camera to the distance and height you'd like it to render the object from.

See `Sprite Batch Rendering` section of the `Render`-tab for controls.

Note: the rendering process can't be canceled once started, so make sure your `Frame Range` and image resolution are correct.

### Path format

Output path must be of format

    C:/some/path/sprite%s%d.png

where `%s` and `%d` will be replaced by frame name and rotation angle respectively.

## License
MIT License, see `COPYING` for details.


