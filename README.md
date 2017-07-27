A mini-library to turn math functions to audio waveforms.

TODO
====

* create setup.py
* create some examples of interesting non-odd waveforms
* document public methods in cli.py
* look harder at click stuff:
  * should specs like duration, frequency, volume, be specified on the command
    line before the waveform itself? I.e. attached as `@click.argument` to the
    `cli` group and accessed via command context (`ctx.params`)
  * add `--outdir`, settable via envvar `WFGEN_TMPDIR`; checks regular `TMPDIR` if
    set to `:ENV` ; if none of these is a valid writeable dir, use /tmp
  * Some sort of container class that can hold a waveform function and defer
    handling audio parameters till initialized by `click`?
  * Allow `PeriodicSignal` subclasses to register themselves as commands
    (provided they have overridden the appropriate method)
