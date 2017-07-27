import functools
import os.path

import click

from .base import PeriodicSignal, OddPeriodicSignal

@click.group()
def cli():
    pass


def validate_bit_depth(ctx, param, value):
    if value not in (8, 16, 32):
        raise click.BadParameter('must be one of 8/16/32')
    return value


def make_command(f, odd=True):
    cls = OddPeriodicSignal if odd else PeriodicSignal
    @cli.command()
    @click.option('--ffmpeg-params', nargs='+')
    @click.option('-b', '--bit-depth', type=int,
                  default=32, callback=validate_bit_depth,
                  help='sample width (bytes)')
    @click.option('-s', '--sample-rate', type=float,
                  help='sample rate (hz)', default=48000)
    @click.option('--volume', type=float, help='volume in dB', default=0.0)
    @click.option('-d', '--duration', type=float,
                  help='length of sample (millis)', default=1000.0)
    @click.option('--fmt', help='audio format', default=None)
    @click.option('-o', '--out', type=click.Path(
        dir_okay=False, writable=True, readable=False, resolve_path=True
    ), help=(
        'output file. Must have a valid format extension. If omitted, --fmt'
        ' must be specified, and the file is written in /tmp.'
    ))
    @click.argument('frequency', type=float, metavar='FREQUENCY_IN_HZ')
    @functools.wraps(f)
    def inner(frequency, out, fmt, duration, volume, sample_rate,
              bit_depth, ffmpeg_params):
        if fmt is None:
            if out:
                fmt = os.path.splitext(out)
            if not fmt:
                raise click.BadParameter('Unable to determine format.',
                                         param_hint=('fmt', 'out'))
        if not out:
            out = '/tmp/%s_%d.%s' % (cls.__name__, int(frequency), fmt)

        gen = cls(frequency, f, sample_rate=sample_rate, bit_depth=bit_depth)
        gen.to_audio_segment(duration=duration, volume=volume).export(
            click.open_file(out, 'wb+'), format=fmt, parameters=ffmpeg_params)
        click.echo('wrote sample to %s' % out)


