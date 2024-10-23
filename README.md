# Portablend

AndroidBlenderDemo
  availability of the demo source is on
svn.blender.org/svnroot/bf-blender/
 in this porting of the android_demo
 swiss_cheese, soc-2012 rev/branch.
 see https://pb.abstind.webredirect.org
 for updates. otherwise continue with the
 fixes for the distribution on blender.org.
 
Compiling
  gcc -o libmain.so -ldl mEvent.c main.c 
  <code>javac -cp ${ANDROIDSDK} -d ${OUTPATH} R.java GhostActivity.java ControlCenterActivity.java BlenderNativeAPI.java... </code>
