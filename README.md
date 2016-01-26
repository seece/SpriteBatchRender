SpriteBatchRender
=================

A spritesheet rendering plugin for Blender.

![Blender addon GUI](http://i.imgur.com/mTThmPK.png)

## What it does

Renders the scene from multiple directions and saves the results as separate files.

Multiple frames can be rendered. The animation frame range is read from the regular
`Start Frame` and `End Frame` rendering properties.

## Usage

Set your camera (called `Camera`) to track an object placed at the origo.
The "front" direction is the same as Blender's front view, so in other words your model
should face to the negative y direction.

> To point the camera towards an object, you can select the camera, add a Track To constraint to it (constraints can be added in the Constraints tab), choose the object in the Target field, -Z in the To field, and Y in the Up field.

Place your camera to the distance and height you'd like it to render the object from.

See `Sprite Batch Rendering` section of the `Render`-tab for controls. You can see the rendering status messages in the system console (Window > Toggle System Console). Click **Render Batch** to begin rendering.

Note: **the rendering process can't be canceled** once started, so make sure your `Frame Range` and image resolution are correct.

### Example .blend file
[http://www.lofibucket.com/blender/monkeeh.blend](http://www.lofibucket.com/blender/monkeeh.blend) is an example how to set up the scene for sprite rendering.

The setup is the following:
* Camera is set to track the Suzanne mesh
* Camera projection is set to projection mode
* Scene render size is set to 128x128
* Frame range has been set to 1-1

### Path format

Output path must be of format

	C:/some/path/sprite%s%s.png

where `%s` and `%s` will be replaced by frame name and rotation step respectively.

### Step names
When rendering ZDoom compatible sprites, the following naming schemes need to be used.

* 8 steps, set step names to `12345678` (default)
* 16 steps, set step names to `192A3B4C5D6E7F8G`

## Installation
Written for Blender 2.76b.

1. Download [sprite_batch_render.py](https://raw.github.com/seece/SpriteBatchRender/master/sprite_batch_render.py) directly or as [a .zip archive.](https://github.com/seece/SpriteBatchRender/archive/master.zip). 
2. In Blender User Preferences, press the **Install from File...** button and pick the downloaded `sprite_batch_render.py`. You should now see the plugin under the Render section in the Add-on listing.
3. Enable the plugin by checking the small checkbox on the right hand side of the plugin name.

You should now see the `Sprite Batch Rendering` controls under the `Render` tab of the `Outliner`.

## License
MIT License, see `COPYING` for details.


