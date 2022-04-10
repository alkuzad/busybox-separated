# Busybox Separated scoop bucket

This is special scoop bucket generated from binaries from original busybox manifest:

`separate.py` python3 script takes `busybox.json` from ScoopInstaller scoop bucket and creates entry in bucket/busybox-XYZ.json
for each binary separatelly. For sha256 generation, valid unxutils folder has to exist for reference.

# Add to Scoop

```
scoop bucket add unxutils-separated https://github.com/alkuzad/busybox-separated.git
```

Then install any package, prefixed by unxutils:

```
scoop install busybox-tee
```

And use:

```batch
rem Note the lack of \ at the end, it's important
grep test "C:\Users\%USERNAME%.%USERDOMAIN%" -r
```

Or for ones that have same Windows command, use l-prefixed command:

```batch
ltee C:\Users -type d
```

# Linux prefix

Scoop will install original and aliased version with `l` prefix (from Linux). This way you can easily do `lsort` or `lfind` instead of mangling windows path.
