import os
import subprocess
import sys
from timeit import default_timer as timer #for timing purposes

if __name__ == '__main__':
    path = sys.argv[1]
    frame_start = sys.argv[2]

    if len(sys.argv) > 3:
        frame_end = sys.argv[3]
        frames = f'{frame_start}..{frame_end}'
    else:
        frames = frame_start

    to_render = [path]
    for r in to_render:
        start = timer()
        print(f'rendering {r}...')
        subprocess.call(['mkdir', f'{r}_rendered_frames'])
        # subprocess.call(['blender', '-b', r, '-P', 'render_with_gpu.py', '-o', f'//{r}_rendered_frames/frame_####', '-f', frames])
        print(frames)
        end = timer()
        print('time elapsed: {}'. format((end-start)))