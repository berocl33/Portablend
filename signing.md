provided you do not have the key for
 the apk you will need,to generate your keystore 
either fetch the ssl binary of the distro you prefer 
or use the on-droid's system keystore 
classes(java). Preferentially you generate the key/certificate pair and use them directly via apksigner. see <p> </href=http:pb.abstind.webredirect.org alt=bsh>bsh</a>repository for examples.
 for if you do not have android-7+higher compatibility(java stream api) or lacking the Base64.Encoder class apksig.ApksignerTool will not work.
 for this contingent you will need the openssl tool and libraries. 
 cmd% { printf %s\\r\\n Signature-Version:\ 1.0 Created-by:\ 1.0\ \(Android\ SignApk\) SHA1-Digest-Manifest:\ $(openssl sha1 -binary $MANIFEST.MF|openssl base64); export li=\  lo=0 { cat $MANIFEST.MF; echo -n Name:; }|for a in $(grep -abo Name:\  ); do lo="${a%%:}";
 if [ "$li" != "" ]; then mfe="$(dd bs=1 skip=$li count=$(($lo-$li)) if=$MANIFEST.MF)";
  mfn="${mfe%??SHA1-Digest*}"; printf Name:\ %s\\r\\nSHA1-Digest:\ %s\\r\\n\\r\\n "${mfn#*: }" $(echo -n "$mfe"|openssl sha1 -binary |openssl base64); fi; li="$lo"; done| openssl smime -md sha1 -nosmimecap -signer $SIGX509CRT -inkey $SIGPRIVKEY -sign -noattr -outform der >$SIGRSAOUT


