import os
import subprocess
import sys
from timeit import default_timer as timer #for timing purposes

if __name__ == '__main__':
    path = sys.argv[1]
    try:
        os.chdir(path)
        videos = os.listdir(path)
        os.chdir(path)
    except:
        to_render = [path]
    for r in to_render:
        start = timer()
        print(f'rendering {r}...')
        subprocess.call(['blender', '-b', r, '-P', 'render_with_gpu.py', '-o', '//rendered_frames/frame_####', '-a'])
        end = timer()
        print('time elapsed: {}'. format((end-start)))