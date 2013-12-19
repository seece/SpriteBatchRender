"""
Sprite Batch Renderer, a Blender addon
Copyright (C) 2013 Pekka Väänänen

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

See COPYING for details.
"""

"""
Renders the scene from multiple directions and saves the results in separate files.
The "front" direction is the same as Blender's front view, in other words your model
should face to the negative y direction.

Multiple frames can be rendered. The animation Frame Range is read from the regular
Start Frame and End Frame rendering properties.

Usage:
	Set your camera (called "Camera") to track an object placed at the origo. 
	Place your camera to the distance and height you'd like it to render the object from.
	
	See Sprite Batch Rendering section of the Render-tab for controls.
	
	Note: the rendering process can't be canceled once started, so make sure your
	Frame Range and image resolution are correct.

"""

import bpy
import math
import sys
import time
import mathutils as mu

from bpy.props import *

bl_info = \
	{
		"name" : "Sprite Batch Render",
		"author" : "Pekka Väänänen <pekka.vaananen@iki.fi>",
		"version" : (1, 0, 0),
		"blender" : (2, 6, 8),
		"location" : "Render",
		"description" :
			"Renders the scene from multiple directions.",
		"warning" : "There's currently no way to cancel rendering",
		"wiki_url" : "",
		"tracker_url" : "",
		"category" : "Render",
	}

class SpriteRenderOperator(bpy.types.Operator):
	bl_idname = "render.spriterender_operator"
	bl_label = "Sprite Render Operator"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		renderframes(
			context.scene,
			context.scene.sprite_render_path, 
			context.scene.sprite_render_steps,
			context.scene.sprite_render_framenames,
			context.scene.frame_start, 
			context.scene.frame_end
		)
		return {'FINISHED'}

	   

class SpriteRenderPanel(bpy.types.Panel):
	bl_idname = 'sprite_panel'
	bl_label = 'Sprite Batch Rendering'
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = "render"
	
	def draw(self, context):
		l = self.layout
		framerow = l.row()
		
		l.row().prop(context.scene, "sprite_render_steps", text="Rotation steps")
		l.row().prop(context.scene, "sprite_render_custom_framenames")
		#l.column().label("Custom frame names:")
		
		if context.scene.sprite_render_custom_framenames:
			l.column().prop(context.scene, "sprite_render_framenames", text="Frame names")
		
		l.row().prop(context.scene, "sprite_render_path", text="Path format")
		row = l.row()
		row.operator("render.spriterender_operator", text="Render Batch", icon='RENDER_ANIMATION')

		
def renderframes(scene, filepath, steps, framenames, startframe=0, endframe=0):
	camera = scene.camera
	oldframe = scene.frame_current

	stepnames = [x for x in range(1,steps+1)]
	
	if not scene.sprite_render_custom_framenames:
		framenames = [chr(ord("A") + x) for x in range(startframe,endframe+1)]

	if endframe-startframe > len(framenames)-1:
		raise Exception("Not enough frames in custom framenames")
	
	print("stepnames: " + str(stepnames))
	print("framenames: " + str(framenames))
	
	frame = startframe
	count = 0
	
	for f in range(startframe, endframe+1):
		scene.frame_current = f
		
		for i in range(0, steps):
			angle = ((math.pi*2.0) / steps) * i
			angle -= math.pi*0.5 # we rotate 90 degrees in counter-clockwise direction
								 # so the first rotation angle will face straight to camera
			
			# we want to ignore the z-coordinate of the camera in the distance calculation,
			# that's why we set loc.z = 0.0
			loc = mu.Vector((camera.location.x, camera.location.y, 0.0))
			distance = loc.magnitude
			
			camera.location.x = math.cos(angle) * distance
			camera.location.y = math.sin(angle) * distance
			
			stepname = stepnames[i]
			name = framenames[f]
			
			scene.render.filepath = filepath % (name, i+1)
			bpy.ops.render.render(animation=False, write_still=True)
			
			print ("%d:%d: %f,%f" % (f, stepname, camera.location.x, camera.location.y))
			count += 1
			
	print ("Rendered %d shots" % (count))
	scene.frame_current = oldframe
	
		
	

def register():
	bpy.utils.register_class(SpriteRenderOperator)
	bpy.utils.register_class(SpriteRenderPanel)
	
	bpy.types.Scene.sprite_render_path = StringProperty (
		name = "Sprite render path",
		description = """Where to save the sprite frames.\
 %s = frame name\
 %d = rotation number""",
		default = "C:/temp/sprite/sprite%s%d.png"
	)
	
	bpy.types.Scene.sprite_render_steps = IntProperty (
		name = "Steps",
		description = "The number of different angles to render",
		default = 8
	)
	
	bpy.types.Scene.sprite_render_framenames = StringProperty (
		name = "Frame names",
		description = """The naming scheme for all frames.
 Each letter corresponds to a single frame.""",
		default = "ABCDEFGH"
	)
	
	bpy.types.Scene.sprite_render_custom_framenames = BoolProperty (
		name = "Use custom frame names",
		description = "Use generated alphabetical names instead of custom defined characters.",
		default = False
	)
	
def unregister():
	bpy.utils.unregister_class(SpriteRenderOperator)
	bpy.utils.unregister_class(SpriteRenderPanel)
	del bpy.types.Scene.sprite_render_path
	del bpy.types.Scene.sprite_render_steps
	del bpy.types.Scene.sprite_render_framenames
	del bpy.types.Scene.sprite_render_custom_framenames

	
if __name__ == "__main__":  
	register()  
