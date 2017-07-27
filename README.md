A mini-library to turn math functions to audio waveforms.

TODO
====

* create setup.py
* add an EvenPeriodicSignal class for even functions
  * document the "advantage" or desirability of ensuring `f'(-1) == f'(+1) == 0`
* create some more examples of interesting waveforms
  * given `threshold`, `lambda x: float(int(x >= threshold))`, non-odd
    generalization of square wave
  * even function: given `step_size`, `lamdba x: floor(x * step_size) /
    step_size`, crude approximation of sawtooth
  * even function: cube root
* current implementation of `OddPeriodicSignal.periodic_function` sort of
  assumes `half_arc_function` is zero at +/- 1, and symmetrical.
  * the symmetrical part is 100% not necessary and the function should be
    fixed to reflect that.
  * the zero-at-the-ends bit is probably valid: it should be documented, and
   possibly `assert`ed at `__init__()`.
  * note: neither requirement is needed for even functions!
  * verify whether the given requirements ensure that if `half_arc_function` is
   semi-differentiable (i.e. has a defined tangent, possibly vertical) from
   the right at -1 and from the left at +1, then the periodic function is
   likewise semi-differentiable at 0.5 and 1. if not, document what else is
   needed for this.
* allow instances/subclasses of {Even,Odd}PeriodicSignal to override our
  semi-arbitrary half-arc domain of [-1..1]
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
* add a feature to graph the waveforms!
* add an argument or envvar that imports a user library and adds its commands?
  * alt: document how to create your own command.
* Document:
  * how to create your own waveforms
  * when to use general periodic functions vs odd vs even
  * installing `ffmpeg` in order to export to non-wav
  * using `sox` to generate spectrogram, include examples
* create some GIFs to demonstrate even and odd functions by animating rot180
 and reflection around x = 1
