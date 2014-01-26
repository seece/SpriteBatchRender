SpriteBatchRender
=================

A spritesheet rendering plugin for Blender.

![Blender addon GUI](http://i.imgur.com/mTThmPK.png)

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

### Example .blend file
[http://www.lofibucket.com/blender/monkeeh.blend](monkeeh.blend) is an example how to set up the scene for sprite rendering.

The setup is the following:
* Camera is set to track the Suzanne mesh
* Camera projection is set to projection mode
* Scene render size is set to 128x128
* Frame range has been set to 1-1

### Path format

Output path must be of format

	C:/some/path/sprite%s%s.png

where `%s` and `%s` will be replaced by frame name and rotation step respectively.

## Installation
Place [sprite_batch_render.py](https://raw.github.com/seece/SpriteBatchRender/master/sprite_batch_render.py) in `Blender/$VERSION/scripts/addons` or in `%APPDATA%/Roaming/Blender Foundation/Blender/$VERSION/scripts/addons` where `$VERSION` is your version number.

See [Installation of an Add-On](http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Add-Ons#Installation_of_an_Add-On) for more help.

## License
MIT License, see `COPYING` for details.


