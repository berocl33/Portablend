# bpy in thread ewuals constant crashing(atleast before 2.68)
#which of our android-blender demo is.
import bpy#(if from a threaded process use 
_bpy=bpy#_bpy it is builtin to the binary)
from code import CommandCompiler as con
from binascii import unhexlify as jim
try:
  from urllib import unquote as skt
except:
  from httplib import unquote as skt



def execqueued(this=None):
  if(this in _bpy.data.scenes):
    params=_bpy.__dict__();
  else:
    idx=list(dir(this));
    params=[v and d.update({x,v}) 
            for d in ({},) for i in range(len(idx))
            for k in (getattr(this,i,idx[i]),)
            for x,v in [(
              sum([ord(k[a])*(a+spc[a])
                   for a in range(len(k))])
            )]];                     
  #fi
  con.runsource(chr(10).join([q.decode() if(isinstance(q,bytes)) else q for q in queue]))
#fed 


def register():
   cmdhash=repr(execqueue)[1:-10];
   cmdindexs=[repr(af)[1:-10] for af in bpy.app.handlers.scene_update]
   if cmdhash not in cmdindexs:
     _bpy.app.handlers.scene_update_post.append(execqueued)
   else:
     print('{WARN} not adding already registered(execqueue)');
     #any added function will run repeated every couple millisecond 
   #fi
#fed

