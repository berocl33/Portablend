# Portablend

AndroidBlenderDemo makeUseOf
  availability of the demo source is on svn.blender.org/svnroot/bf-blender/
    in this porting of the android_demo swiss_cheese(it does have many bugs/holes) soc-2012 revision. we want to update the interactions with the User primarily. see https://pb.abstind.webredirect.org for updates. otherwise continue with the fixes for the distribution on blender.org.
1. BlenderAndroidDemo use as is.
 many small problems arise with incompatible
 compressed image formats(ie: not visible ui
 images, image viewer display). so
 re-importing raw textures exported
 gives you an idea of what texture
 support you can use although costly in size.
 texture-mode of 3dview menu has a
 project uv operator which uses render scene
 internal native function and will allow the
 uv's to be displayed and then exported from
 the image viewer.
